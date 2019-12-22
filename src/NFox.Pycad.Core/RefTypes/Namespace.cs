using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Text;
using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal class Namespace
    {

        public string Name { get; private set; }

        public static Namespace Root { get; } = new Namespace();

        public Namespace Parent { get; private set; }

        public List<Namespace> Children { get; } = new List<Namespace>();

        public ItemDictionary<Type> Types { get; }

        public ItemDictionary<Type> ExtensionTypes { get; }


        private const string _clrclasses = "__clrclasses__";
        private const string _initfilename = "__init__.py";
        private readonly static DirectoryInfo _stubsroot = DirectoryEx.Root.CreateSubdirectory("stubs").CreateSubdirectory("clrclasses");
        private readonly static string _nsroot = _stubsroot.GetFileFullName("namespace.zip");
        private readonly static DirectoryInfo _clrroot = _stubsroot.CreateSubdirectory(_clrclasses);

        private Namespace(string name): this()
        {
            Name = name;
        }

        private Namespace()
        {
            Types = new ItemDictionary<Type>();
            ExtensionTypes = new ItemDictionary<Type>();
        }

        public static Namespace FromString(string ns)
        {
            if (string.IsNullOrEmpty(ns))
            {
                return Namespace.Root;
            }
            else if (ns.Contains("."))
            {
                int i = ns.LastIndexOf(".");
                var parent = FromString(ns.Substring(0, i));
                var name = ns.Substring(i + 1);
                if(name == "")
                    return parent;
                return parent.GetChild(name);
            }
            else
            {
                return Root.GetChild(ns);
            }
        }

        public static void SaveAll()
        {
            var path = _clrroot.GetFileFullName(_initfilename);
            if(!File.Exists(path))
                File.Create(path).Dispose();
            foreach (var ns in Root.Children)
                ns.Save();
            Root.Children.Clear();
        }

        private DirectoryInfo StubPath
        {
            get
            {
                if (Parent == null)
                    return _stubsroot;
                else
                    return Parent.StubPath.CreateSubdirectory(Name);
            }
        }

        private DirectoryInfo ClrPath
        {
            get
            {
                if (Parent == null)
                    return _clrroot;
                else
                    return Parent.ClrPath.CreateSubdirectory(Name);
            }
        }


        public Type GetType(string name)
        {
            var names = name.Split('.');
            var type = Types[names[0]];
            foreach (var tname in names.Skip(1))
                type = type.Types[tname];
            return type;
        }

        public Type GetExtype(string name, bool create = false)
        {

            var names = name.Split('.');
            if (!ExtensionTypes.ContainsKey(names[0]))
            {
                if (create)
                    ExtensionTypes.Add(new Type(this, null, names[0]));
                else
                    return null;
            }
            var type = ExtensionTypes[names[0]];
            foreach (var tname in names.Skip(1))
            {
                if (!type.Types.ContainsKey(tname))
                {
                    if (create)
                        type.Types.Add(new Type(this, type, tname));
                    else
                        return null;
                }
                type = type.Types[tname];
            }
            return type;
        }

        private IEnumerable<string> GetNames()
        {
            if (File.Exists(_nsroot))
            {
                using (FileStream fs = new FileStream(_nsroot, FileMode.Open))
                using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                {
                    foreach (var ent in zip.Entries)
                    {
                        if(ent.Name.StartsWith(Fullname + "."))
                            yield return ent.Name.Substring(Fullname.Length + 1).Split('.')[0];
                    }
                }
            }
        }

        public static Namespace Curr { get; private set; }
        public static Type CurrType { get; private set; }

        public SortedList<string, List<string>> Imports { get; private set; }
        private List<string> _paramnames;

        private void Import(Type type)
        {

            //加载泛型类型
            foreach(var par in type.GenericParams)
            {
                if (par.Kind == TypeIndexKind.GenericParam && !_paramnames.Contains(par.Name))
                    _paramnames.Add(par.Name);
            }

            //遍历该类型中包含的所有变量的类型索引
            foreach (var bt in type.BaseTypes)
                Import(bt);
            foreach (var field in type.Fields)
                Import(field.Value.TypeIndex);
            foreach (var @event in type.Events)
                Import(@event.Value.TypeIndex);
            foreach (var property in type.Properties)
                Import(property.Value.TypeIndex);
            foreach (var method in type.Methods)
            {
                foreach (var define in method.Value.Defines)
                {
                    Import(define.TypeIndex);
                    foreach (var param in define.Params)
                        Import(param.TypeIndex);
                }
            }

            //遍历子类型
            foreach (var st in type.Types)
                Import(st.Value);

        }

        /// <summary>
        /// 获取类型索引中包含的所有类型
        /// </summary>
        /// <param name="ti">类型索引</param>
        private void Import(TypeIndex ti)
        {

            //把信息存入Imports字典中,以在索引的Fullname属性中解析

            switch (ti.Kind)
            {
                case TypeIndexKind.System:
                case TypeIndexKind.GenericParam:
                    return;
                case TypeIndexKind.GenericType:
                    foreach (var tp in ti.GenericParams)
                        Import(tp);
                    break;
            }

            if (ti.Namespace == Fullname || ti.Namespace == "typing")
                return;

            if (!Imports.ContainsKey(ti.Namespace))
                Imports.Add(ti.Namespace, new List<string>());
            var lst = Imports[ti.Namespace];

            var name = ti.Name.Split(new char[] { '.' }, 2)[0];
            if (!lst.Contains(name))
                lst.Add(name);

        }

        private void Save()
        {
            if (this == Root)
            {
                foreach (var child in Children)
                    child.Save();
            }
            else if (Children.Count + Types.Count + ExtensionTypes.Count > 0)
            {

                //保存当前加载的子命名空间
                foreach (var child in Children)
                    child.Save();

                using (var csw = new StreamWriter(ClrPath.GetFileFullName(_initfilename)))
                using (var ssw = new StreamWriter(StubPath.GetFileFullName(_initfilename)))
                {

                    //加载所有子命名空间
                    foreach (var name in GetNames().Distinct())
                    {
                        csw.WriteLine($"import {_clrclasses}.{Fullname}.{name} as {name}");
                        ssw.WriteLine($"import {_clrclasses}.{Fullname}.{name} as {name}");
                    }

                    if (Types.Count + ExtensionTypes.Count > 0)
                    {

                        //有类型或者扩展函数时才需要保存为Xml,并压缩
                        var xe = new XElement("Namespace");
                        var ee = new XElement("Types");
                        xe.Add(ee);
                        foreach (var t in Types)
                            ee.Add(t.Value.ToXml());
                        ee = new XElement("ExtensionTypes");
                        xe.Add(ee);
                        foreach (var t in ExtensionTypes)
                            ee.Add(t.Value.ToXml());
                        using (FileStream fs = new FileStream(_nsroot, FileMode.OpenOrCreate))
                        using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Update))
                        {
                            var ent = zip.GetEntry(Fullname);
                            if (ent != null) ent.Delete();
                            ent = zip.CreateEntry(Fullname);
                            using (var sw = new StreamWriter(ent.Open(), Encoding.UTF8))
                                xe.Save(sw);
                        }

                        if (Types.Count > 0)
                        {

                            //有类型才需要写入模块

                            //将所有非本模块的类型名都设置别名
                            Curr = this;
                            Imports = new SortedList<string, List<string>>();
                            _paramnames = new List<string>();
                            foreach (var type in Types)
                                Import(type.Value);
                            foreach (var type in ExtensionTypes)
                                Import(type.Value);
                            for (int i = 0; i < Imports.Count; i++)
                            {
                                var lst = Imports.Values[i];
                                for (int j = 0; j < lst.Count; j++)
                                    csw.WriteLine($"from {_clrclasses}.{Imports.Keys[i]} import {lst[j]} as _n_{i}_t_{j}");
                            }

                            //设置泛型参数
                            csw.WriteLine("import typing");
                            foreach (var par in _paramnames)
                                csw.WriteLine($"{par} = typing.TypeVar('{par}')");

                            //遍历所有类型,并写入感知文件
                            foreach (var type in Types)
                            {
                                CurrType = type.Value;
                                type.Value.Desc(csw, 0);
                                CurrType = null;
                                ssw.WriteLine($"from {_clrclasses}.{Fullname} import {type.Value.Name}");
                            }

                            Curr = null;
                            Imports = null;
                            _paramnames = null;

                        }

                    }
                }
            }

        }
        

        private bool _loaded;

        private void Load()
        {
            if (!_loaded)
            {
                _loaded = true;
                if (File.Exists(_nsroot))
                {
                    using (FileStream fs = new FileStream(_nsroot, FileMode.Open))
                    using (ZipArchive zip = new ZipArchive(fs, ZipArchiveMode.Read))
                    {
                        var ent = zip.GetEntry(Fullname);
                        if (ent != null)
                        {
                            using (var sr = new StreamReader(ent.Open()))
                            {
                                var xe = XElement.Load(sr);
                                foreach (var e in xe.Element("Types").Elements("Type"))
                                    Types.Add(Item.Parse<Type>(e));
                                foreach (var e in xe.Element("ExtensionTypes").Elements("Type"))
                                    ExtensionTypes.Add(Item.Parse<Type>(e));
                                SetTo(Types);
                                SetTo(ExtensionTypes);
                            }
                        }
                    }

                }
            }
        }

        private void SetTo(ItemDictionary<Type> types)
        {
            foreach (var type in types)
            {
                type.Value.Namespace = Fullname;
                SetTo(type.Value.Types);
            }
        }

        public Namespace GetChild(string name)
        {
            foreach (var child in Children)
            {
                if (child.Name == name)
                    return child;
            }
            var n = new Namespace(name) { Parent = this };
            n.Load();
            Children.Add(n);
            return n;
        }

        public string Fullname
        {
            get
            {
                if (this == Root)
                    return "";
                else if (Parent == Root)
                    return Name;
                else
                    return $"{Parent.Fullname}.{Name}";
            }
        }


    }
}



