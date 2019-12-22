using IronPython.Runtime.Exceptions;
using Microsoft.Scripting;
using Newtonsoft.Json.Linq;
using System;

namespace NFox.Pycad.Servers.Tcp
{
    public class BreakPoint : IEquatable<BreakPoint>
    {

        public string FileName { get; }
        public int Line { get; }

        SourceSpan _span;
        TraceBackFrame _backFrame;

        public BreakPoint BackPoint
        {
            get { return new BreakPoint(_backFrame); }
        }

        public BreakPoint(JObject obj)
        {
            FileName = obj.Property("filename").Value.Value<string>().ToLower();
            Line = obj.Property("line").Value.Value<int>();
        }

        public BreakPoint(TraceBackFrame frame)
        {
            FileName = frame.f_code.co_filename.ToLower();
            Line = (int)frame.f_lineno;
            _span = frame.f_code.Span;
            _backFrame = frame.f_back;
        }

        //public BreakPoint(string filename, int line)
        //{
        //    FileName = filename;
        //    Line = line;
        //}

        public override string ToString()
        {
            JObject obj =
                new JObject(
                    new JProperty("filename", FileName),
                    new JProperty("line", Line));
            return obj.ToString();
        }

        public bool Equals(BreakPoint other)
        {
            return FileName == other.FileName && Line == other.Line;
        }

        public bool IsNext(BreakPoint pt)
        {
            return
                FileName == pt.FileName && _span == pt._span && Line != pt.Line ||
                Equals(pt.BackPoint);
        }

    }
}
