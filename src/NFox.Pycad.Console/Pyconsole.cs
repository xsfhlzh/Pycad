using NFox.Pycad.Servers.Wcf;
using System;
using System.ServiceModel;

namespace NFox.Pycad
{

    public class Pyconsole : IConsoleCallback
    {
        public void Read()
        {
            string result = "\n";
            string previous = null;
            string current = null;
            for (int count = 0; count < 2 || previous != "" && current != ""; count++)
            {
                previous = current;
                current = Console.ReadLine();
                result += "\n" + current;
            }
            result.TrimEnd(' ', '\n');
            IConsoleServer proxy = ServUtils.CreateClient<IConsoleServer, WSDualHttpBinding, Pyconsole>("http://localhost/pycad/servers/console");
            string res = proxy.Exec(result);
            if (!string.IsNullOrEmpty(res)) res += "\r\n";
            Console.Write(res);
        }

        public void Write(string message)
        {
            Console.Write(message);
        }
    }



}
