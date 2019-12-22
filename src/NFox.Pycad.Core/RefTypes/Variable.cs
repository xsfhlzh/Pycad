using System.Xml.Linq;

namespace NFox.Pycad.RefTypes
{
    internal abstract class Variable : Item
    {

        public Variable() { }

        public TypeIndex TypeIndex { get; protected set; }

        public Variable(string name)
        {
            TypeIndex = new TypeIndex("None");
            Name = name;
        }

        public Variable(string name, System.Type type)
        {
            TypeIndex = TypeIndex.FromSystemType(type);
            Name = name;
        }

        public override void FromXml(XElement xe)
        {
            base.FromXml(xe);
            TypeIndex = Parse<TypeIndex>(xe.Element("TypeIndex"));
        }

        public override XElement ToXml()
        {
            var xe = base.ToXml();
            xe.Add(TypeIndex.ToXml());
            return xe;
        }

    }
}
