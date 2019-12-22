using System;
using System.Net;
using System.Net.NetworkInformation;
using System.Net.Sockets;
using System.Threading;

namespace NFox.Pycad.Servers.Tcp
{

    /// <summary>
    /// 监听器
    /// </summary>
    public class Lister
    {
        private static Socket _server = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
        public const string IP = "127.0.0.1";
        private const int MaxNumOfClient = 1024;

        private static int FindAvailableTCPPort()
        {
            int port = 1219;
            bool isAvailable = true;
            IPGlobalProperties ipGlobalProperties =
                IPGlobalProperties.GetIPGlobalProperties();
            IPEndPoint[] endPoints =
                ipGlobalProperties.GetActiveTcpListeners();

            do
            {
                if (!isAvailable)
                {
                    port++;
                    isAvailable = true;
                }
                foreach (IPEndPoint endPoint in endPoints)
                {
                    if (endPoint.Port != port) continue;
                    isAvailable = false;
                    break;
                }

            } while (!isAvailable && port < IPEndPoint.MaxPort);
            if (!isAvailable)
                throw new ApplicationException("Not able to find a free TCP port.");
            return port;
        }

        internal Lister()
        {
            var port = FindAvailableTCPPort();
            Application.SetVariable("servers.tcp.port", port);
            _server.Bind(new IPEndPoint(IPAddress.Parse(IP), port));
            _server.Listen(MaxNumOfClient);
            _server.BeginAccept(EndAccept, null);
        }

        public void Close()
        {
            _server.Close();
        }

        private void EndAccept(IAsyncResult ar)
        {
            Distributor link = new Distributor(_server.EndAccept(ar));
            _server.BeginAccept(EndAccept, null);
        }

    }
}
