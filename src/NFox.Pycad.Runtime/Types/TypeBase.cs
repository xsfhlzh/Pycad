using System;

namespace NFox.Pycad.Types
{
    public class TypeBase : IComparable<TypeBase>
    {

        public virtual string Description { get; }

        public string Name { get; protected set; }

        public virtual int Order { get { return -1; } }

        public int CompareTo(TypeBase other)
        {

            int comp = Order.CompareTo(other.Order);
            if (comp == 0)
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
            return comp;
        }

    }

    public class Statement : TypeBase
    {
        public override string Description { get { return $"输入?{Name}以获取更多信息"; } }

        public Statement(string name)
        {
            Name = name;
        }

    }



}
