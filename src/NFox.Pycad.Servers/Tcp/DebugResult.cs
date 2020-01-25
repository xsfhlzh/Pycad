using System.Runtime.Serialization;

namespace NFox.Pycad.Servers.Tcp
{

    public enum StatusType
    {
        Start,
        Continue,
        SetpIn,
        Next,
        SetpOut,
        Wait,
        Stop,
        Close
    }

    [DataContract]
    public class DebugResult
    {

        [DataMember]
        public StatusType Status { get; set; }

        [DataMember]
        public BreakPoint BreakPoint { get; set; }

        private DebugResult() { }

        public DebugResult(StatusType status, BreakPoint point = null)
        {
            Status = status;
            BreakPoint = point;
        }

    }
}
