using Autodesk.AutoCAD.DatabaseServices;
using Autodesk.AutoCAD.Geometry;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace NFox.Pycad.Core
{
    public class EntityBox
    {

        double X => Box.MinPoint.X;
        double Y => Box.MinPoint.Y;
        double Width => Box.MaxPoint.X - X;
        double Height => Box.MaxPoint.Y - Y;

        public List<Entity> Ents { private set; get; } = new List<Entity>();
        public Extents3d Box { get; private set; }
        bool IsEmpty => Ents.Count == 0;
        public override string ToString()
        {
            return $"{Width}x{Height}";
        }

        private Vector3d _vec = new Vector3d(1, 1, 0);

        public EntityBox(Entity ent, double add)
        {
            Ents.Add(ent);
            var vec = _vec * add;
            Box = ent.GeometricExtents;
            Box.ExpandBy(-vec);
            Box.ExpandBy(vec);
        }

        bool Intersect(EntityBox b)
        {
            return 
                (b.X < Box.MaxPoint.X) &&
                (X < b.Box.MaxPoint.X) &&
                (b.Y < Box.MaxPoint.Y) &&
                (Y < b.Box.MaxPoint.Y);
        }

        public bool Join(EntityBox other)
        {
            if (Intersect(other))
            {
                Ents.AddRange(other.Ents);
                Box.AddExtents(other.Box);
                return true;
            }
            return false;
        }

    }

    public class EntityBoxList : IEnumerable<EntityBox>
    {

        private LinkedList<EntityBox> _lst = new LinkedList<EntityBox>();

        public EntityBoxList GetRealList()
        {
            EntityBoxList lsta = new EntityBoxList();
            EntityBoxList lstb = new EntityBoxList();
            EntityBoxList lstc;
            foreach (var box in _lst)
                lsta.Add(box);
            int oldcount = Count;
            int newcount = lsta.Count;

            while (oldcount != newcount)
            {
                oldcount = newcount;
                lstb = new EntityBoxList();
                foreach (var box in lsta._lst)
                    lstb.Add(box);
                lstc = lsta;
                lsta = lstb;
                lstb = lstc;
                newcount = lsta.Count;
            }
            return lsta;
        }

        public int Count => _lst.Count;

        public void Add(EntityBox newbox)
        {
            var node = _lst.First;
            while(node != null)
            {
                var next = node.Next;
                if (newbox.Join(node.Value))
                    _lst.Remove(node);
                node = next;
            }
            _lst.AddLast(newbox);
        }

        public IEnumerator<EntityBox> GetEnumerator()
        {
            return _lst.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }


}
