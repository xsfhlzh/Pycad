namespace NFox.Pycad
{

    public enum MessageType
    {

        Start = 0,
        End = 1,
        BigData = 2,

        DebugStart = 100,
        DebugContinue = 101,
        DebugNext = 102,
        DebugSetpIn = 103,
        DebugSetpBack = 104,
        DebugReturn = 105,
        DebugWait = 106,

        BreakPointAdd = 200,
        BreakPointRemove = 201,

        DebugGetGlobals = 300,
        DebugGetLocals = 301,
        DebugGetFrames = 302,

        ConsoleStart = 400,
        ConsoleExec = 401,

    }

    public class Message
    {

        public MessageType Type { get; set; }

        public string Content { get; set; }

    }

}
