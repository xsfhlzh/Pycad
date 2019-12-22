using NFox.Pycad.Servers.Wcf;
using System;
using System.ServiceModel;

namespace NFox.Pycad.ConsoleApplication
{

    class Program
    {

        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write(">>>");
                string code = Console.ReadLine();
                IConsoleServer proxy = ServUtils.CreateClient<IConsoleServer, WSDualHttpBinding, Pyconsole>("http://localhost/pycad/servers/console");
                string res = proxy.Exec(code);
                if (!string.IsNullOrEmpty(res)) res += "\r\n";
                Console.Write(res);
            }
        }
    }
}
