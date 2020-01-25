using NFox.Pycad.Servers.Tcp;
using System;
using System.Diagnostics;
using System.Net;
using System.Net.Sockets;
using System.ServiceModel;
using System.Threading;

namespace NFox.Pycad.Servers
{
    public class Application : PluginBase
    {


        //Console Exec Serv
        private ServiceHost _pychost;

        private static TcpListener _listener;
        private const string IP = "127.0.0.1";
        private const int Port = 5678;

        protected override void OnInitializing()
        {

            //普通用户启动WCF服务
            string args = @"http add urlacl url=http://+:80/ user=everyone";
            var psi = new ProcessStartInfo("netsh", args);
            psi.Verb = "runas";
            psi.CreateNoWindow = true;
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            psi.UseShellExecute = true;
            Process.Start(psi).WaitForExit();

            _pychost = Wcf.ServUtils.OpenServ<Wcf.ConsoleServer, WSDualHttpBinding>(Utils.GetVariable<string>("servers.wcf.console"));

            int port = Utils.GetFreePort(1219);
            foreach(var dir in DirectoryEx.Extensions.GetDirectories())
            {
                if (!dir.Name.StartsWith("."))
                {
                    var filename = dir.GetDirectory(".vscode").GetFile("launch.json").FullName;
                    Utils.UsingJsonFile(filename, obj => obj["configurations"][0]["port"] = port, true);
                }
            }
            _listener = new TcpListener(IPAddress.Parse("127.0.0.1"), port);
            _listener.Start();
            _listener.BeginAcceptSocket(EndAccept, null);

        }

        private void EndAccept(IAsyncResult ar)
        {
            new Thread(() => DebugServer.Wait(_listener.EndAcceptSocket(ar))).Start();
            _listener.BeginAcceptSocket(EndAccept, null);
        }

        protected override bool OnMessage(string message, params dynamic[] args)
        {
            switch (message)
            {
                case "BeforeCommand":
                    if (DebugServer.Instance != null)
                    {
                        Engine.Instance.SetTrace(DebugServer.Instance.Trace);
                        DebugServer.Instance.ThreadName = args[0];
                    }
                    return true;
                case "AfterCommand":
                    Engine.Instance.SetTrace(null);
                    return true;
            }
            return false;
        }

    }

}
