using NFox.Expression.SymbolValues;
using System.IO;
using System.Xml.Linq;

namespace NFox.Expression.DataSystem
{

    public class ConfigDictionary : SimpleDictionary<ConfigItem>
    {

        XElement _xe = new XElement("Config");

        private Database _database;
        public Database Database
        {
            set
            {
                _database = value;
                if (_database.FileName != null && File.Exists(_database.FileName))
                {
                    _xe = ZipUtils.Extract(_database.FileName, "Config");
                }
            }
            get
            {
                return _database;
            }
        }

        public override ConfigItem this[string key]
        {
            get
            {
                if (Has(key))
                {
                    return base[key];
                }
                else
                {
                    var e = _xe.Element(key);
                    var value = new ConfigItem();
                    if (e == null)
                        _xe.Add(value.ToX(key));
                    else
                        value.FromX(e);
                    Add(key, value);
                    return value;
                }
            }
            set
            {
                base[key] = value;
                _xe.Element(key).Remove();
                _xe.Add(value.ToX());
            }
        }

        public XElement ToX()
        {
            return _xe;
        }

    }

}
