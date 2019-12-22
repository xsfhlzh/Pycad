using Microsoft.Scripting.Hosting;
using NFox.Expression.DataSystem;
using NFox.Geometry;
using System.Collections.Generic;
using System.Data;
using System.Xml.Linq;
using System.Linq;

namespace NFox.Expression.SymbolValues
{
    public class Function : ISymbolValue
    {

        ScriptScope _scope;
        Image _image;

        public List<Entity2D> __call__(params string[] pars)
        {
            if (_scope == null)
            {
                _scope = Database.Engine.CreateScope();
                Database.Engine.Execute("from NFox.Geometry import *", _scope);
                foreach(var dict in Database.FunctionTable)
                    _scope.SetVariable(dict.Name, dict);
                _scope.SetVariable("image", _image = new Image());
            }
            if (ParamNames.Count == pars.Length)
            {
                var ents = new List<Entity2D>();
                _image.SetData(ents);
                for (int i = 0; i < ParamNames.Count; i++)
                    _scope.SetVariable(ParamNames[i], pars[i]);
                Database.Engine.Execute(Code, _scope);
                return ents;
            }
            else
            {
                throw new System.Exception("参数错误!");
            }
        }

        #region Member

        public string Name { get; set; }

        public Database Database{ set; get; }

        public SymbolIndex Index
        {
            set
            {
                Dict = value.DictionaryName;
                Name = value.Key;
            }
            get
            {
                return new SymbolIndex(Dict, Name);
            }
        }

        public string Dict { get; set; }

        public List<string> ParamNames
        { private set; get; }

        public string Code
        { private set; get; }

        public List<string> DefaultParams
        {
            get
            {
                var pars = new List<string>();
                if (Data != null)
                {
                    foreach (string s in Data.Rows[0].ItemArray)
                    {
                        if (s.Contains(","))
                            pars.Add(s.Split(',')[0]);
                        else
                            pars.Add(s);
                    }
                }
                return pars;
            }
        }

        public DataTable Data
        { private set; get; }

        #endregion

        #region ISave

        public void ToX(XElement xe)
        {
            xe.Add(new XAttribute("Name", Name));
            if (ParamNames.Count > 0)
                xe.Add(new XAttribute("Pars", string.Join(",", ParamNames)));
            xe.Add(new XElement("Code", Code));
            if (Data != null)
            {
                var s = string.Join("|", Data.Select().Select(dr => string.Join(";", dr.ItemArray)));
                xe.Add(new XElement("Data", s));
            }
        }

        public string XName
        {
            get { return "Func"; }
        }

        public void FromX(XElement xe)
        {
            Name = xe.Attribute("Name").Value;
            ParamNames = new List<string>();
            if (xe.Attribute("Pars") != null)
                ParamNames.AddRange(xe.Attribute("Pars").Value.Split(','));
            Code = xe.Element("Code").Value;

            if (xe.Element("Data") != null)
            {
                Data = new DataTable();
                foreach (var name in ParamNames)
                    Data.Columns.Add(name);
                foreach (var r in xe.Element("Data").Value.Split('|'))
                {
                    DataRow dr = Data.NewRow();
                    int i = 0;
                    foreach (var c in r.Split(';'))
                        dr[i++] = c;
                    Data.Rows.Add(dr);
                }

            }
        }

        #endregion

    }

}
