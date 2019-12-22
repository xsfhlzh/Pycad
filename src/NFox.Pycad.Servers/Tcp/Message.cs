namespace NFox.Pycad.Servers.Tcp
{

    public enum MessageType
    {


        Start = 0,
        End = 1,
        BigData = 2,

        DebugStart = 100,
        DebugContinue = 101,
        DebugSetpIn = 102,
        DebugNext = 103,
        DebugSetpOut = 104,
        DebugWait = 105,

        BreakPointAdd = 200,
        BreakPointRemove = 201,

        DebugGetGlobals = 300,
        DebugGetLocals = 301,
        DebugGetClosures = 302,

        ConsoleStart = 400,
        ConsoleExec = 401,

    }

    public class Message
    {

        public MessageType Type { get; set; }

        public string Content { get; set; }

    }

}
