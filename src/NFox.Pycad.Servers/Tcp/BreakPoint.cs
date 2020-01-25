using IronPython.Runtime.Exceptions;
using Microsoft.Scripting;
using Newtonsoft.Json.Linq;
using System;

namespace NFox.Pycad.Servers.Tcp
{
    public class BreakPoint : IEquatable<BreakPoint>
    {

        public string Path { get; }
        public int Line { get; }

        public string FunctionName { get; }

        SourceSpan _span;
        TraceBackFrame _backFrame;

        public BreakPoint BackPoint
        {
            get
            {
                if (_backFrame != null)
                    return new BreakPoint(_backFrame);
                return null;
            }
        }

        public BreakPoint(TraceBackFrame frame)
        {
            FunctionName = frame.f_code.co_name;
            Path = frame.f_code.co_filename.ToLower();
            Line = (int)frame.f_lineno;
            _span = frame.f_code.Span;
            _backFrame = frame.f_back;
        }

        public BreakPoint(string path, int line)
        {
            Path = path;
            Line = line;
        }

        public bool Equals(BreakPoint other)
        {
            return Path == other.Path && Line == other.Line;
        }

        public bool IsNext(BreakPoint pt)
        {
            return
                Path == pt.Path && _span == pt._span && Line != pt.Line ||
                Equals(pt.BackPoint);
        }

    }
}
