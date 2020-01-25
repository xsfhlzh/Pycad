using IronPython.Runtime.Exceptions;
using Microsoft.VisualStudio.Shared.VSCodeDebugProtocol;
using Microsoft.VisualStudio.Shared.VSCodeDebugProtocol.Messages;
using NFox.Pycad.Types;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Threading;
using vsThread = Microsoft.VisualStudio.Shared.VSCodeDebugProtocol.Messages.Thread;

namespace NFox.Pycad.Servers.Tcp
{
    public class DebugServer : DebugAdapterBase
    {

        private AutoResetEvent _resetEvent = new AutoResetEvent(false);

        //单例类
        public static DebugServer Instance { get; private set; } 

        public bool Enabled { get; private set; }

        public static void Wait(Socket socket)
        {
            using (var stdio = new NetworkStream(socket))
            {
                Instance = new DebugServer();
                Instance.InitializeProtocolClient(stdio, stdio);
                Instance.Protocol.Run();
                Instance.Protocol.WaitForReader();
            }
        }

        #region Server

        public string ThreadName { get; set; }

        public StatusType Status { get; private set; }

        private Dictionary<string, List<BreakPoint>> _points = new Dictionary<string, List<BreakPoint>> ();
        private BreakPoint _mainpoint;
        private BreakPoint _currpoint;

        public TracebackDelegate Trace(TraceBackFrame frame, string result, object payload)
        {
            if (Enabled)
            {
                var bt = new BreakPoint(frame);
                if (_mainpoint != null && _mainpoint.BackPoint.Equals(bt))
                {
                    Status = StatusType.Start;
                    _mainpoint = null;
                }
                else if (!bt.Path.StartsWith("<"))
                {
                    switch (Status)
                    {
                        case StatusType.Start:
                            if (_mainpoint == null)
                            {
                                if (bt.Path.StartsWith(Workspace))
                                {
                                    _mainpoint = bt;
                                    Wait(frame, result, payload);
                                    break;
                                }
                            }
                            break;
                        case StatusType.Continue:
                            if (_points.ContainsKey(bt.Path) && _points[bt.Path].Contains(bt))
                                Wait(frame, result, payload);
                            break;
                        case StatusType.SetpIn:
                            Wait(frame, result, payload);
                            break;
                        case StatusType.SetpOut:
                            if (bt.Equals(_currpoint.BackPoint))
                                Wait(frame, result, payload);
                            break;
                        case StatusType.Next:
                            if (bt.IsNext(_currpoint))
                                Wait(frame, result, payload);
                            break;
                    }
                }
            }
            return Trace;
        }



        private void Wait(TraceBackFrame frame, string result, object payload)
        {

            _currpoint = new BreakPoint(frame);

            var pt = _currpoint;
            _frames = new List<StackFrame>();
            int i = 1000;
            while(pt != null)
            {
                var path = pt.Path;
                _frames.Add(
                    new StackFrame
                    {
                        Id = i++,
                        Name = pt.FunctionName,
                        Line = pt.Line,
                        Source = new Source { Name = Path.GetFileName(path), Path = path }
                    });
                pt = pt.BackPoint;
            }

            _values = ValueTree.GetValues(frame);

            Status = StatusType.Wait;
            Stop(StoppedEvent.ReasonValue.Step);
            _resetEvent.WaitOne();

            if (Status == StatusType.Stop)
                throw new System.Exception("调试中断!");

        }

        #endregion

        #region Adapter

        private ValueTree _values;

        private List<StackFrame> _frames;

        public string Workspace { get; private set; }

        public void Stop(StoppedEvent.ReasonValue reason)
        {
            Protocol.SendEvent(new StoppedEvent { Reason = reason, ThreadId = 0 });
        }


        protected override AttachResponse HandleAttachRequest(AttachArguments arguments)
        {
            Workspace = ((string)arguments.ConfigurationProperties["workspaceFolder"]).ToLower();
            return new AttachResponse();
        }

        protected override InitializeResponse HandleInitializeRequest(InitializeArguments arguments)
        {
            Protocol.SendEvent(new InitializedEvent());
            Protocol.SendEvent(new ThreadEvent(ThreadEvent.ReasonValue.Started, 0));
            return
                new InitializeResponse
                {
                    SupportsConfigurationDoneRequest = true,
                    SupportsSetVariable = false,
                    SupportsDebuggerProperties = false,
                    SupportsModulesRequest = false,
                    SupportsSetExpression = false,
                    SupportsExceptionOptions = false,
                    SupportsExceptionConditions = false,
                    SupportsExceptionInfoRequest = false,
                    SupportsValueFormattingOptions = false,
                    SupportsEvaluateForHovers = true,
                    SupportsConditionalBreakpoints = false,
                    SupportsCompletionsRequest = false,
                    SupportsDataBreakpoints = false,
                    SupportsDelayedStackTraceLoading = false,
                    SupportsDisassembleRequest = false,
                    SupportsFunctionBreakpoints = false,
                    SupportsGotoTargetsRequest = false,
                    SupportsHitConditionalBreakpoints = false,
                    SupportsLoadedSourcesRequest = false,
                    SupportsLoadSymbolsRequest = false,
                    SupportsLogPoints = false,
                    SupportsModuleSymbolSearchLog = false,
                    SupportsReadMemoryRequest = false,
                    SupportsRestartFrame = false,
                    SupportsRestartRequest = false,
                    SupportsSetSymbolOptions = false,
                    SupportsStepBack = false,
                    SupportsStepInTargetsRequest = false,
                    SupportsTerminateRequest = false,
                    SupportsTerminateThreadsRequest = false,
                    SupportTerminateDebuggee = false
                };
        }

        protected override SetBreakpointsResponse HandleSetBreakpointsRequest(SetBreakpointsArguments arguments)
        {
            List<Breakpoint> result = new List<Breakpoint>();
            var path = arguments.Source.Path.ToLower();
            var pts = _points[path] = new List<BreakPoint>();
            foreach (var bt in arguments.Breakpoints)
            {
                pts.Add(new BreakPoint(path, bt.Line));
                result.Add(new Breakpoint(true) { Source = arguments.Source, Line = bt.Line });
            }
            return new SetBreakpointsResponse(result);
        }

        protected override ConfigurationDoneResponse HandleConfigurationDoneRequest(ConfigurationDoneArguments arguments)
        {
            Enabled = true;
            Protocol.SendEvent(new ThreadEvent(ThreadEvent.ReasonValue.Started, 0));
            return new ConfigurationDoneResponse();
        }

        protected override DisconnectResponse HandleDisconnectRequest(DisconnectArguments arguments)
        {
            Enabled = false;
            Status = StatusType.Stop;
            _resetEvent.Set();
            return new DisconnectResponse();
        }

        protected override ThreadsResponse HandleThreadsRequest(ThreadsArguments arguments)
        {
            if (!Enabled)
                throw new ProtocolException("非命令模式!");
            return new ThreadsResponse(new List<vsThread> { new vsThread(0, ThreadName) });
        }

        protected override StackTraceResponse HandleStackTraceRequest(StackTraceArguments arguments)
        {
            IEnumerable<StackFrame> enumFrames = _frames;
            if (arguments.StartFrame.HasValue)
                enumFrames = enumFrames.Skip(arguments.StartFrame.Value);
            if (arguments.Levels.HasValue)
                enumFrames = enumFrames.Take(arguments.Levels.Value);
            return new StackTraceResponse
            {
                StackFrames = enumFrames.ToList(),
                TotalFrames = _frames.Count
            };
        }
        
        protected override ScopesResponse HandleScopesRequest(ScopesArguments arguments)
        {
            return
                new ScopesResponse(
                    _values
                    .Select(t => new Scope(t.Name, t.Id, true))
                    .ToList());
        }

        private List<Variable> GetVariables(int id)
        {
            List<Variable> variables = new List<Variable>();
            foreach(var item in _values.GetTree(id))
            {
                variables.Add(
                    new Variable
                    {
                        Name = item.Name,
                        Value = item.Value.Description,
                        VariablesReference = item.Id,
                        Type = item.Value.TypeName
                    });
            }
            return variables;
        }

        protected override void HandleVariablesRequestAsync(IRequestResponder<VariablesArguments, VariablesResponse> responder)
        {
            responder.SetResponse(
                new VariablesResponse(
                    GetVariables(responder.Arguments.VariablesReference)));
        }

        protected override EvaluateResponse HandleEvaluateRequest(EvaluateArguments arguments)
        {
            try
            {
                var tree = _values.GetTree(arguments.Expression);
                if (tree == null)
                {
                    try
                    {
                        var value = Engine.Instance.Execute(arguments.Expression, ValueTree.Scope);
                        return new EvaluateResponse(Engine.Instance.GetStr(value), 0);
                    }
                    catch
                    {
                        return new EvaluateResponse("解析失败!", 0);
                    }
                }
                else if (tree.Value == null)
                {
                    return new EvaluateResponse(tree.Name, 0);
                }
                else
                {
                    return new EvaluateResponse(tree.Value.Description, tree.Id) { Type = tree.Value.TypeName };
                }
            }
            catch
            {
                return new EvaluateResponse("解析失败!", 0);
            }
        }

        protected override ContinueResponse HandleContinueRequest(ContinueArguments arguments)
        {
            Status = StatusType.Continue;
            _resetEvent.Set();
            return new ContinueResponse();
        }

        protected override StepInResponse HandleStepInRequest(StepInArguments arguments)
        {
            Status = StatusType.SetpIn;
            _resetEvent.Set();
            return new StepInResponse();
        }

        protected override StepOutResponse HandleStepOutRequest(StepOutArguments arguments)
        {
            Status = StatusType.SetpOut;
            _resetEvent.Set();
            return base.HandleStepOutRequest(arguments);
        }

        protected override NextResponse HandleNextRequest(NextArguments arguments)
        {
            Status = StatusType.Next;
            _resetEvent.Set();
            return new NextResponse();
        }

        protected override SetExceptionBreakpointsResponse HandleSetExceptionBreakpointsRequest(SetExceptionBreakpointsArguments arguments)
        {
            return new SetExceptionBreakpointsResponse();
        }

        #endregion

    }

}
