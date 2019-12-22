using System;
using System.ServiceModel;

namespace NFox.Pycad.Servers.Wcf
{

    [ServiceContract(SessionMode = SessionMode.Required, CallbackContract = typeof(IConsoleCallback))]
    public interface IConsoleServer
    {

        [OperationContract]
        string Exec(string code);

    }

    public interface IConsoleCallback
    {

        [OperationContract(IsOneWay = true)]
        void Write(string message);

        [OperationContract(IsOneWay = true)]
        void Read();

    }

}
