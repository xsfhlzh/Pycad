using System.ServiceModel;
using System.ServiceModel.Web;

namespace NFox.Pycad.Servers.Wcf
{
    [ServiceContract]
    public interface IDebugServer
    {

        [OperationContract]
        [WebGet(UriTemplate = "maxlengthofdata", ResponseFormat = WebMessageFormat.Json)]
        int GetMaxLengthOfData();

        [OperationContract]
        [WebGet(UriTemplate = "port", ResponseFormat = WebMessageFormat.Json)]
        int GetPort();

    }

    [ServiceBehavior]
    public class DebugServer : IDebugServer
    {
        public int GetMaxLengthOfData()
        {
            return (int)Application.GetVariable("servers.tcp.maxlengthofdata");
        }

        public int GetPort()
        {
            return (int)Application.GetVariable("servers.tcp.port");
        }
    }

}
