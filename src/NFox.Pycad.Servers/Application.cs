using System.Diagnostics;
using System.ServiceModel;

namespace NFox.Pycad.Servers
{
    public class Application : PluginBase
    {

        private Tcp.Lister _lister;

        //Console Exec Serv
        private ServiceHost _pychost;

        //Debug Serv
        private ServiceHost _pydhost;

        protected override void OnInitializing()
        {

            _lister = new Tcp.Lister();
            
            //普通用户启动WCF服务
            string args = @"http add urlacl url=http://+:80/ user=everyone";
            var psi = new ProcessStartInfo("netsh", args);
            psi.Verb = "runas";
            psi.CreateNoWindow = true;
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            psi.UseShellExecute = true;
            Process.Start(psi).WaitForExit();

            _pychost = Wcf.ServUtils.OpenServ<Wcf.ConsoleServer, WSDualHttpBinding>(GetVariable("servers.wcf.console"));
            _pydhost = Wcf.ServUtils.OpenRestServ<Wcf.DebugServer>(GetVariable("servers.wcf.debug"));

        }

        protected override bool OnMessage(string message, params dynamic[] args)
        {
            switch(message)
            {
                case "BeforeCommand":
                    if(Tcp.DebugServer.Instance.Enabled)
                        Engine.Instance.SetTrace(Tcp.DebugServer.Instance.Trace);
                    else
                        Engine.Instance.SetTrace(null);
                    return true;
                case "AfterCommand":
                    Engine.Instance.SetTrace(null);
                    return true;
            }
            return false;
        }

    }

}
