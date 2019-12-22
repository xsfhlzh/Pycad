using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using ICSharpCode.TextEditor;
using ICSharpCode.TextEditor.Document;
using ICSharpCode.TextEditor.Gui.CompletionWindow;
using System.Text.RegularExpressions;
using NFox.Expression.Runtime;
using NFox.Expression.SymbolValues;


namespace NFox.TFunc
{

    class TFuncProvider : ICompletionDataProvider
    {

        TextArea _area;
        Form _form;
        private List<ICompletionData> _vars = new List<ICompletionData>();
        private List<ICompletionData> _args = new List<ICompletionData>();
        private List<ICompletionData> _datas = new List<ICompletionData>();

        public TFuncProvider(Form form, TextEditorControl editor, ImageList imageList)
        {
            _form = form;
            _area = editor.ActiveTextAreaControl.TextArea;
            _area.KeyEventHandler += TextArea_KeyEventHandler;
            _area.ToolTipRequest += TextArea_ToolTipRequest;
            _imageList = imageList;
        }

        public void ResetArgs(ParameterizedPart part)
        {
            _args.Clear();
            foreach (var arg in part.TypeTable)
                _args.Add(new VariateData(arg.Key, arg.Value));
        }

        #region Events

        void TextArea_ToolTipRequest(object sender, ToolTipRequestEventArgs e)
        {
            if (e.ToolTipShown) return;
            if (e.InDocument)
            {
                var area = sender as TextArea;
                var pos = e.LogicalPosition;
                var doc = area.Document;
                LineSegment seg = doc.GetLineSegment(pos.Y);
                var txt = seg.GetWord(pos.X);
                if (txt != null && !string.IsNullOrEmpty(txt.Word))
                    e.ShowToolTip(GetDescription(txt.Word));
            }
        }

        public string GetDescription(string name)
        {
            var q =
                _words
                .SelectMany(words => words.Value)
                .Union(_vars)
                .Where(word => word.Text == name)
                .FirstOrDefault();
            if (q != null && !string.IsNullOrEmpty(q.Description))
                return q.Description;
            return null;
        }

        CodeCompletionWindow completionWindow;

        bool TextArea_KeyEventHandler(char key)
        {

            var doc = _area.Document;
            int row = _area.Caret.Line;
            int col = _area.Caret.Column;

            if (completionWindow != null)
            {
                // If completion window is open and wants to handle the key, don't let the text area
                // handle it
                if (completionWindow.ProcessKeyEvent(key))
                    return true;
            }
            else if (char.IsLetter(key) || key == '_')
            {

                LineSegment seg = doc.GetLineSegment(row);
                TextWord word = seg.GetWord(col);

                if (!IsNullWord(word) && IsVariateOrDigit(word.Word))
                    return false;

                //获取前一个单词
                while (IsNullWord(word) && col > 0) word = seg.GetWord(--col);

                //如果有单词，将本句的单词加入队列
                Queue<TextWord> allWords = new Queue<TextWord>();
                if (!IsNullWord(word))
                {
                    for (int i = seg.Words.IndexOf(word); i > -1; i--)
                    {
                        word = seg.Words[i];
                        if (!string.IsNullOrEmpty(word.Word))
                            allWords.Enqueue(word);
                    }
                }

                //加入之前的所有单词
                for (int i = row - 1; i > -1; i--)
                {
                    seg = doc.GetLineSegment(i);
                    for (int j = seg.Words.Count - 1; j > -1; j--)
                    {
                        word = seg.Words[j];
                        if (!string.IsNullOrEmpty(word.Word))
                            allWords.Enqueue(word);
                    }
                }

                List<TextWord> pWords = new List<TextWord>();
                List<TextWord> cWords = new List<TextWord>();

                //找到当前语句
                while (allWords.Count > 0)
                {
                    if (IsRangeEnd(allWords.Peek())) break;
                    cWords.Add(allWords.Dequeue());
                }

                //找到之前的所有语句
                while (allWords.Count > 0)
                    pWords.Insert(0, allWords.Dequeue());

                _vars.Clear();

                int num;

                //确定当前单词的类型
                string typeName = null;
                bool isDataType = false;
                if (cWords.Count == 0 || (cWords[0].Word == "(" && cWords[1].Word == "for"))
                {
                    isDataType = true;
                }
                else
                {
                    List<TextWord> words = new List<TextWord>();
                    bool hasDataType = false;
                    for (int i = 0; i < cWords.Count; i++)
                    {
                        words.Add(cWords[i]);
                        if (IsKeyWord("DataType", cWords[i]))
                        {
                            typeName = cWords[i].Word;
                            hasDataType = true;
                            break;
                        }
                    }

                    //如果当前句有声明语句，在变量表中加入声明过的变量
                    if (hasDataType)
                    {
                        num = 0;
                        for (int i = 0; i < words.Count; i++)
                        {

                            string s = words[i].Word;
                            if (s == "(")
                            {
                                num++;
                            }
                            else if (s == ")")
                            {
                                num--;
                            }

                            if (num == 0 && IsDataType(words[i]))
                            {
                                if (i != words.Count - 1)
                                    AddVariate(words[i + 1], typeName);
                            }

                        }

                        if (num == 0 && (IsDataType(words[0]) || IsDataType(words[1])))
                            return false;
                    }
                }

                //找到之前的所有语句中搜索变量声明，并加入变量表
                num = 0;
                bool atDataType = false;
                for (int i = 0; i < pWords.Count; i++)
                {
                    string s = pWords[i].Word;
                    if (IsKeyWord("DataType", pWords[i]))
                    {
                        typeName = pWords[i].Word;
                        atDataType = true;
                        num = 0;
                    }
                    else if (s == "(")
                    {
                        num++;
                    }
                    else if (s == ")")
                    {
                        num--;
                    }
                    else if (IsRange(pWords[i]))
                    {
                        atDataType = false;
                    }

                    if (atDataType && num == 0 && IsDataType(pWords[i]))
                    {
                        AddVariate(pWords[i + 1], typeName);
                    }

                }

                //为智能提示准备单词
                _datas.Clear();
                if (isDataType) _datas.AddRange(_words["DataType"]);
                _datas.AddRange(_args);
                _datas.AddRange(_vars);
                _datas.AddRange(_words["KeyWord"]);
                _datas.AddRange(_words["Method"]);
                _datas.AddRange(_words["Constant"]);

                //显示智能提示窗口
                completionWindow =
                    CodeCompletionWindow.ShowCompletionWindow(
                        _form,
                        _area.MotherTextEditorControl,
                        "",
                        this,
                        key);
                if (completionWindow != null)
                {

                    // ShowCompletionWindow can return null when the provider returns an empty list
                    completionWindow.Closed += new EventHandler(CloseCodeCompletionWindow);
                }
            }
            return false;
        }

        void CloseCodeCompletionWindow(object sender, EventArgs e)
        {
            if (completionWindow != null)
            {
                completionWindow.Closed -= new EventHandler(CloseCodeCompletionWindow);
                completionWindow.Dispose();
                completionWindow = null;
            }
        }

        #endregion

        #region ICompletionDataProvider

        public int DefaultIndex
        {
            get { return -1; }
        }

        public ICompletionData[] GenerateCompletionData(string fileName, TextArea textArea, char charTyped)
        {
            return _datas.ToArray();
        }

        ImageList _imageList;
        public ImageList ImageList
        {
            get { return _imageList; }
        }

        public bool InsertAction(ICompletionData data, TextArea textArea, int insertionOffset, char key)
        {
            textArea.Caret.Position = textArea.Document.OffsetToPosition(insertionOffset);
            return data.InsertAction(textArea, key);
        }

        public string PreSelection
        {
            get { return ""; }
        }

        public CompletionDataProviderKeyResult ProcessKey(char key)
        {
            if (char.IsLetterOrDigit(key) || key == '_')
            {
                return CompletionDataProviderKeyResult.NormalKey;
            }
            else
            {
                // key triggers insertion of selected items
                return CompletionDataProviderKeyResult.InsertionKey;
            }
        }

        #endregion

        #region Word

        private void AddVariate(TextWord word, string type)
        {
            string name = word.Word;
            foreach (var data in _vars.Union(_args))
                if (data.Text == name) return;
            if (!IsDataType(word) && IsVariate(name))
                _vars.Add(new TFunc.VariateData(name, type));
        }

        private bool IsVariate(string name)
        {
            char c = name[0];
            return char.IsLetter(c) || c == '_';
        }

        private bool IsVariateOrDigit(string name)
        {
            char c = name[0];
            return char.IsLetterOrDigit(c) || c == '_';
        }

        private bool IsDataType(TextWord word)
        {
            return IsKeyWord("DataType", word) || word.Word == ",";
        }


        private bool IsRangeEnd(TextWord word)
        {
            return _rangeEnds.Contains(word.Word);
        }

        public bool IsRange(TextWord word)
        {
            return _ranges.Contains(word.Word);
        }

        private bool IsKeyWord(string typeName, TextWord word)
        {
            return
                _words[typeName]
                .Select(d => d.Text)
                .Contains(word.Word);
        }

        private bool IsNullWord(TextWord word)
        {
            if (word == null) return true;
            string s = Regex.Replace(word.Word, "\\s", "");
            if (string.IsNullOrEmpty(s)) return true;
            return false;
        }

        private static string[] _ranges = { "{", "}", "(", ")", ";" };

        private static string[] _rangeEnds = { "{", "}", ";" };


        private static Dictionary<string, ICompletionData[]> _words =
            new Dictionary<string, ICompletionData[]>
            {
                {
                    "KeyWord",
                    new ICompletionData[]
                    {
                        new KeyWordData("if"),
                        new KeyWordData("else"),
                        new KeyWordData("for"),
                        new KeyWordData("while"),
                        new KeyWordData("return"),
                        new KeyWordData("break"),
                        new KeyWordData("continue"),
                    }
                },
                {
                    "DataType",
                    new ICompletionData[]
                    {
                        new TypeData("var", ""),
                        new TypeData("int", "表示32位有符号的整数"),
                        new TypeData("long", "表示64位有符号的整数"),
                        new TypeData("double", "表示双精度浮点数"),
                        new TypeData("string", "表示文本，即一系列Unicode字符"),
                        new TypeData("bool", "表示布尔值"),
                        new TypeData("point", "表示二/三维点"),
                    }
                },
                {
                    "Method",
                    new ICompletionData[]
                    {
                        new MethodData("sin", "计算角度的正弦值")
                        { 
                            {"d", "double", "角度的弧度值"},
                        },
                        new MethodData("cos", "计算角度的余弦值")
                        { 
                            {"d", "double", "角度的弧度值"},
                        },
                        new MethodData("min", "求数列的最小值")
                        { 
                            {"d", "double", "双精度浮点数", false, true},
                        },
                        new MethodData("max", "求数列的最大值")
                        { 
                            {"d", "double", "双精度浮点数", false, true},
                        },
                        new MethodData("npoint", "按坐标创建点")
                        { 
                            {"x", "double", "横坐标"},
                            {"y", "double", "纵坐标"},
                        },
                        new MethodData("polar", "按极坐标移动点")
                        { 
                            {"base", "point", "基点"},
                            {"angle", "double", "角度"},
                            {"length", "double", "极长"},
                        },
                        new MethodData("moveto", "按笛卡尔坐标移动点")
                        { 
                            {"base", "point", "基点"},
                            {"value", "point", "移动向量"},
                        },
                        new MethodData("vertex", "返回多段线的顶点数据")
                        { 
                            {"vex", "point", "顶点数据"},
                            {"bulge", "double", "凸度"},
                            {"startWidth", "double", "起始宽度", true, false},
                            {"endWidth", "double", "结束宽度", true, false}
                        },
                        new MethodData("line", "绘制直线")
                        {
                            {"start", "point", "起点"},
                            {"end", "point", "终点"},
                            {"layer", "string", "图层", true, false}
                        },
                        new MethodData("circle", "绘制圆")
                        { 
                            {"center", "point", "圆心"},
                            {"radius", "double", "半径"},
                            {"layer", "string", "图层", true, false}
                        },
                        new MethodData("arc", "绘制圆弧")
                        { 
                            {"center", "point", "圆心"},
                            {"radius", "double", "半径"},
                            {"start", "double", "起始角度"},
                            {"end", "double", "终止角度"},
                            {"layer", "string", "图层", true, false}
                        },
                        new MethodData("ellipse", "绘制椭圆(弧)")
                        { 
                            {"center", "point", "椭圆中心"},
                            {"majorRadius", "double", "长半轴"},
                            {"minorRadius", "double", "短半轴"},
                            {"angle", "double", "偏转角度"},
                            {"start", "double", "起始角度", true, false},
                            {"end", "double", "终止角度", true, false},
                            {"layer", "string", "图层", true, false}
                        },
                        new MethodData("text", "绘制文字")
                        { 
                            {"center", "point", "中点"},
                            {"textString", "string", "文字内容"},
                            {"size", "double", "字高"},
                            {"layer", "string", "图层", true, false}
                        },
                        new MethodData("spline", "绘制样条曲线")
                        {
                            {"closed", "bool", "是否封闭"},
                            {"pnt", "point", "拟合点", false, true},
                            {"layer", "string", "图层", true, false}
                        },

                        new MethodData("pline", "绘制多段线")
                        {
                            {"closed", "bool", "是否封闭"},
                            {"vertex", "point", "顶点数据", true, false},
                            {"layer", "string", "图层", true, false}
                        },
                    }
                },
                {
                    "Constant",
                    new ICompletionData[]
                    {
                        new ConstantData("BasePt", "图形基点"),
                        new ConstantData("XAxis", "X方向单位向量"),
                        new ConstantData("YAxis", "Y方向单位向量"),
                        new ConstantData("ZAxis", "Z方向单位向量"),
                        new ConstantData("PI", "圆周率"),
                    }
                }
            };

        #endregion


    }
}
