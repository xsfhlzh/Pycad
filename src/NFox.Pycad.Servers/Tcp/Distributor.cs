using System.Net.Sockets;

namespace NFox.Pycad.Servers.Tcp
{

    /// <summary>
    /// 服务分发器
    /// </summary>
    public class Distributor : LinkBase
    {

        public Distributor(Socket socket)
        {
            _socket = socket;
            BegineReceive();
        }

        protected override bool Response(Message message)
        {
            switch (message.Type)
            {
                case MessageType.DebugStart:
                    DebugServer.Instance.LinkTo(_socket);
                    break; 
            }
            return false;
        }

    }
}
