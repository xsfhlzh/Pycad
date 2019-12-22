using System.Collections.Generic;
using System.Reflection;
using System.IO;

namespace NFox.Pycad.RefTypes
{
    internal class Event : Variable
    {

        public List<string> Methodnames { get; } = new List<string>();

        public Event() { }

        public Event(EventInfo @event) 
            : base(@event.Name, @event.EventHandlerType)
        {
            Methodnames.Add(@event.AddMethod.Name);
            Methodnames.Add(@event.RemoveMethod.Name);
            if (@event.RaiseMethod != null)
                Methodnames.Add(@event.RaiseMethod.Name);
        }

        public override void Desc(StreamWriter sw, int space)
        {
            var pre = GetPrefixSpace(space);
            sw.WriteLine($"{pre}@property");
            sw.WriteLine($"{pre}def {Name}(self) -> {TypeIndex.Fullname}:");
            sw.WriteLine($"{pre}    \"\"\"{Name} Event: {TypeIndex.Name}\"\"\"");
        }

    }
}
