using NFox.Pycad.Servers.Tcp;
using System;
using System.IO;
using System.Net;
using System.Net.Sockets;

namespace NFox.DebugTest
{
    public class DebugClient : LinkBase
    {

        public DebugClient()
        {
            _maxlengthofdata = int.Parse(GetResponse("maxlengthofdata"));
            _socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            _socket.Connect(new IPEndPoint(IPAddress.Parse("127.0.0.1"), int.Parse(GetResponse("port"))));
            Send(MessageType.DebugStart);
        }

        private string GetResponse(string par)
        {
            var request = WebRequest.Create($"http://localhost/pycad/servers/debug/{par}") as HttpWebRequest;
            request.Method = "get";
            request.ContentType = "application/json";
            using (HttpWebResponse response = request.GetResponse() as HttpWebResponse)
            {
                //以流的形式读取，返回的就是字符串的json格式
                var reader = new StreamReader(response.GetResponseStream());
                return reader.ReadToEnd();
            }
        }

        protected override bool Response(Message message)
        {
            switch(message.Type)
            {
                case MessageType.DebugWait:
                    Console.WriteLine(message.Content);
                    break;
                case MessageType.DebugGetGlobals:
                case MessageType.DebugGetLocals:
                case MessageType.DebugGetClosures:
                    Console.Write(message.Content);
                    break;
            }
            bool b = true;
            while (b)
            {
                var res = Console.ReadKey();
                switch (res.Key)
                {
                    case ConsoleKey.G:
                        Send(MessageType.DebugGetGlobals);
                        b = false;
                        break;
                    case ConsoleKey.L:
                        Send(MessageType.DebugGetLocals);
                        b = false;
                        break;
                    case ConsoleKey.O:
                        Send(MessageType.DebugGetClosures);
                        b = false;
                        break;
                    case ConsoleKey.N:
                        Send(MessageType.DebugNext);
                        b = false;
                        break;
                    case ConsoleKey.S:
                        Send(MessageType.DebugSetp);
                        b = false;
                        break;
                    case ConsoleKey.R:
                        Send(MessageType.DebugReturn);
                        b = false;
                        break;
                    case ConsoleKey.C:
                        Send(MessageType.DebugContinue);
                        b = false;
                        break;
                    case ConsoleKey.Q:
                        Send(MessageType.End);
                        b = false;
                        return false;
                    default:
                        Console.WriteLine("\nError Key!");
                        break;
                }
                Console.Write("\n");
            }
            return true;
        }

    }
}
