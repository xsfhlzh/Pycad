using Microsoft.Scripting;
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

    [ServiceBehavior]
    public class ConsoleServer : IConsoleServer
    {

        static string _code = null;
        static bool _eof = false;

        public string Exec(string code)
        {
            bool eof = false;
            dynamic stdio = null;
            try
            {
                stdio = Engine.Instance.Execute("pycad.system.stdio");
                stdio.redirect(this);
                if (eof = _eof)
                {
                    _eof = false;
                    code = _code + code;
                    _code = null;
                }
                return Engine.Instance.GetStr(Engine.Instance.Execute(code));
            }
            catch (Exception ex)
            {

                if (ex is SyntaxErrorException && ex.Message == "unexpected EOF while parsing" && !eof)
                {
                    _eof = true;
                    _code = code;
                    OperationContext
                    .Current
                    .GetCallbackChannel<IConsoleCallback>()
                    .Read();
                    return null;
                }

                var name = ex.GetType().Name;
                if (name.EndsWith("Exception") && name.Length > 9)
                    name = name.Substring(0, name.Length - 9);
                try
                {
                    dynamic temp = ex;
                    write($"{name}: {temp.Message}\n");
                    write($"at: {temp.RawSpan}\n");
                }
                catch { }
                return null;
            }
            finally
            {
                stdio?.redirect(null);
            }

        }

        public void write(string message)
        {
            OperationContext
            .Current
            .GetCallbackChannel<IConsoleCallback>()
            .Write(message);
        }

        public void hide()
        {
            
        }

        public void show()
        {

        }

    }

}
