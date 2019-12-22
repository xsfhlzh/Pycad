using System;

namespace NFox.Pycad.Types
{
    public class TypeBase : IComparable<TypeBase>
    {

        public virtual int ImageIndex { get; }

        public virtual string Title { get; }

        public virtual string Description { get; }

        public string Name { get; protected set; }

        public int CompareTo(TypeBase other)
        {

            if (Name[0] == '_')
            {
                if (other.Name[0] == '_')
                    return Name.CompareTo(other.Name);
                else
                    return 1;
            }
            else
            {
                if (other.Name[0] == '_')
                    return -1;
                else
                    return Name.CompareTo(other.Name);
            }
        }
    }

    public class Statement : TypeBase
    {

        public override string Title { get { return $"{Name}语句"; } }
        public override string Description { get { return $"输入?{Name}以获取更多信息"; } }
        public override int ImageIndex { get { return 0; } }

        public Statement(string name)
        {
            Name = name;
        }

    }



}
