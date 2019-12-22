using IronPython.Runtime;
using IronPython.Runtime.Exceptions;
using NFox.Pycad.Types;
using System;
using System.Collections.Generic;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace NFox.Pycad.Servers.Tcp
{
    public class DebugServer : LinkBase
    {

        //单例类
        public static DebugServer Instance { get; } = new DebugServer();

        public bool Enabled { get; private set; }

        private DebugServer()
        {
            Status = StatusType.Start;
            Enabled = false;
        }

        private Socket _tmpsocket;

        public void LinkTo(Socket socket)
        {
            if (_socket != null & Status == StatusType.Wait)
            {
                //如果连接存在,并处于数据等待
                lock (_socket)
                {
                    //关闭一个等待数据的连接会引发异常
                    _tmpsocket = socket;
                    _socket.Close();
                    _socket = socket;
                }
            }
            else
            {
                _socket = socket;
                Application.GetPlugin("NFox.Pycad.Core").Start();
                Enabled = true;
            }
        }

        
        protected override bool Response(Message message)
        {
            switch (message.Type)
            {
                case MessageType.End:
                    //用户端关闭时抛出异常
                    throw new Exception("用户退出!");
                case MessageType.DebugContinue:
                    Status = StatusType.Continue;
                    return false;
                case MessageType.DebugNext:
                    Status = StatusType.Next;
                    return false;
                case MessageType.DebugSetpOut:
                    Status = StatusType.SetpOut;
                    return false;
                case MessageType.DebugSetpIn:
                    Status = StatusType.SetpIn;
                    return false;
                case MessageType.DebugGetGlobals:
                    Send(MessageType.DebugGetGlobals, $"{Globals.ToJson()}\n");
                    break;
                case MessageType.DebugGetLocals:
                    Send(MessageType.DebugGetLocals, $"{Locals[0].ToJson()}\n");
                    break;
                case MessageType.DebugGetClosures:
                    Send(MessageType.DebugGetClosures, $"{Locals[1].ToJson()}\n");
                    break;
                case MessageType.BreakPointAdd:
                    var obj = JsonConvert.DeserializeObject(message.Content);
                    if(obj is JArray)
                    {
                        foreach (JObject o in (JArray)obj)
                            AddBreakPoint(o);
                    }
                    else
                    {
                        AddBreakPoint((JObject)obj);
                    }
                    break;
                case MessageType.BreakPointRemove:
                    obj = JsonConvert.DeserializeObject(message.Content);
                    if (obj is JArray)
                    {
                        foreach (JObject o in (JArray)obj)
                            RemoveBreakPoint(o);
                    }
                    else
                    {
                        RemoveBreakPoint((JObject)obj);
                    }
                    break;
            }
            return true;
        }

        private void AddBreakPoint(JObject obj)
        {
            var cbp = new BreakPoint(obj);
            foreach (var bp in _points)
            {
                if (bp.Equals(cbp))
                    return;
            }
            _points.Add(cbp);
        }

        private void RemoveBreakPoint(JObject obj)
        {
            var bp = new BreakPoint(obj);
            for (int i = 0; i< _points.Count; i++)
            {
                if (_points[i].Equals(bp))
                {
                    _points.RemoveAt(i);
                    return;
                }
            }
        }

        public StatusType Status { get; private set; }

        public ValueList Globals;
        public ValueList[] Locals;

        private List<BreakPoint> _points = new List<BreakPoint>();
        private BreakPoint _mainpoint;
        private BreakPoint _currpoint;

        [DllImport("user32.dll")]
        static extern IntPtr SetActiveWindow(IntPtr hWnd);

        [DllImport("user32.dll")]
        private static extern bool SetForegroundWindow(IntPtr hWnd);

        [DllImport("User32.dll")]
        public static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        private static extern int GetWindowTextW(IntPtr hWnd, [MarshalAs(UnmanagedType.LPWStr)]StringBuilder lpString, int nMaxCount);

        [DllImport("user32.dll")]
        private static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

        private void ActiveEditor()
        {
            string eclass = Application.GetVariable("editor.class");
            string ename = Application.GetVariable("editor.name");
            IntPtr ip = FindWindowEx(IntPtr.Zero, IntPtr.Zero, eclass, null);
            while (ip != IntPtr.Zero)
            {
                StringBuilder sb = new StringBuilder(256);
                GetWindowTextW(ip, sb, sb.Capacity);
                string name = sb.ToString();
                if (name.Contains(ename))
                {
                    ShowWindow(ip, 3);
                    SetActiveWindow(ip);
                    SetForegroundWindow(ip);
                    return;
                }
                ip = FindWindowEx(IntPtr.Zero, ip, eclass, null);
            }
        }

        private static string _prjdir = DirectoryEx.Extensions.FullName.ToLower(); 

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
                else if (!bt.FileName.StartsWith("<"))
                {
                    switch (Status)
                    {
                        case StatusType.Start:
                            if (_mainpoint == null)
                            {
                                if (bt.FileName.StartsWith(_prjdir))
                                {
                                    //ActiveEditor();
                                    _mainpoint = bt;
                                    Wait(frame, result, payload);
                                    break;
                                }
                            }
                            break;
                        case StatusType.Continue:
                            if (_points.Contains(bt))
                                Wait(frame, result, payload);
                            break;
                        case StatusType.SetpIn:
                            Wait(frame, result, payload);
                            break;
                        case StatusType.Next:
                            if (bt.IsNext(_currpoint))
                                Wait(frame, result, payload);
                            break;
                        case StatusType.SetpOut:
                            if (bt.Equals(_currpoint.BackPoint))
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
            Globals = ValueList.GetGlobals(frame.f_globals);
            Locals = ValueList.GetLocals((PythonDictionary)frame.f_locals);
            Status = StatusType.Wait;
            Wait();
        }

        private void Wait()
        {
            Send(MessageType.DebugWait, _currpoint.ToString());
            try
            {
                Receive();
            }
            catch
            {
                if (_tmpsocket == null)
                {
                    //用户端关闭时停止服务
                    Enabled = false;
                    Status = StatusType.Start;
                    _socket?.Close();
                    _socket = null;
                    _mainpoint = null;
                    _points = new List<BreakPoint>();
                    throw new Exception("客户端断开连接!");
                }
                else
                {
                    //新连接接入,断线重连
                    _socket.Close();
                    _socket = _tmpsocket;
                    _tmpsocket = null;
                    Wait();
                }
            }
        }
       

    }

}
