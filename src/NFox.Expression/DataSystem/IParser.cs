

using System.Xml.Linq;
using System;

namespace NFox.Expression.DataSystem
{
    public interface IParser
    {
        string XName { get; }
        void FromX(XElement xe);
        void ToX(XElement xe);
    }

    public static class XParser
    {
        public static T Parse<T>(XElement xe)
            where T : IParser, new()
        {
            T obj = new T();
            obj.FromX(xe);
            return obj;
        }

        public static T Parse<T>(XElement xe, Action<T> init)
            where T : IParser, new()
        {
            T obj = new T();
            init(obj);
            obj.FromX(xe);
            return obj;
        }

        public static XElement ToX(this IParser obj, string name)
        {
            XElement xe = new XElement(name);
            obj.ToX(xe);
            return xe;
        }

        public static XElement ToX(this IParser obj)
        {
            return ToX(obj, obj.XName);
        }

    }

}
