using System;
using System.ServiceModel;
using System.ServiceModel.Channels;
using System.ServiceModel.Description;

namespace NFox.Pycad.Servers.Wcf
{
    public static class ServUtils
    {

        public static ServiceHost OpenServ<TServ, TBinding>(string uri)
            where TBinding : Binding, new()
        {
            Type t = typeof(TServ);
            var host = new ServiceHost(t, new Uri(uri));
            host.AddServiceEndpoint(t.GetInterface($"I{t.Name}"), CreateBinding<TBinding>(), "");
            host.Description.Behaviors.Add(new ServiceMetadataBehavior { HttpGetEnabled = true });
            host.Open();
            return host;
        }

        public static ServiceHost OpenRestServ<TServ>(string uri)
        {
            Type t = typeof(TServ);
            var host = new ServiceHost(t, new Uri(uri));
            var endpoint = host.AddServiceEndpoint(t.GetInterface($"I{t.Name}"), CreateBinding<WebHttpBinding>(), "");
            endpoint.EndpointBehaviors.Add(new WebHttpBehavior());
            host.Description.Behaviors.Add(new ServiceMetadataBehavior { HttpGetEnabled = true });
            host.Open();
            return host;
        }

        private static BasicHttpBinding CreateBasicHttpBinding()
        {
            var instance = new BasicHttpBinding();
            instance.MaxBufferSize = 2147483647;
            instance.MaxBufferPoolSize = 2147483647;
            instance.MaxReceivedMessageSize = 2147483647;
            instance.ReaderQuotas.MaxStringContentLength = 2147483647;
            instance.CloseTimeout = new TimeSpan(0, 10, 0);
            instance.OpenTimeout = new TimeSpan(0, 10, 0);
            instance.ReceiveTimeout = new TimeSpan(0, 10, 0);
            instance.SendTimeout = new TimeSpan(0, 10, 0);
            return instance;
        }

        private static WSHttpBinding CreateWSHttpBinding()
        {
            var instance = new WSHttpBinding(SecurityMode.None);
            instance.MaxBufferPoolSize = 2147483647;
            instance.MaxReceivedMessageSize = 2147483647;
            instance.ReaderQuotas.MaxStringContentLength = 2147483647;
            instance.Security.Message.ClientCredentialType = MessageCredentialType.Windows;
            instance.Security.Transport.ClientCredentialType = HttpClientCredentialType.Windows;
            instance.CloseTimeout = new TimeSpan(0, 10, 0);
            instance.OpenTimeout = new TimeSpan(0, 10, 0);
            instance.ReceiveTimeout = new TimeSpan(0, 10, 0);
            instance.SendTimeout = new TimeSpan(0, 10, 0);
            return instance;
        }

        private static WSDualHttpBinding CreateWSDualHttpBinding()
        {
            var instance = new WSDualHttpBinding();
            instance.MaxBufferPoolSize = 2147483647;
            instance.MaxReceivedMessageSize = 2147483647;
            instance.ReaderQuotas.MaxStringContentLength = 2147483647;
            instance.MessageEncoding = WSMessageEncoding.Mtom;
            instance.CloseTimeout = new TimeSpan(0, 10, 0);
            instance.OpenTimeout = new TimeSpan(0, 10, 0);
            instance.ReceiveTimeout = new TimeSpan(0, 10, 0);
            instance.SendTimeout = new TimeSpan(0, 10, 0);
            return instance;
        }

        private static NetTcpBinding CreateNetTcpBinding()
        {
            var instance = new NetTcpBinding();
            instance.MaxBufferSize = 2147483647;
            instance.MaxBufferPoolSize = 2147483647;
            instance.MaxReceivedMessageSize = 2147483647;
            instance.ReaderQuotas.MaxStringContentLength = 2147483647;
            return instance;
        }

        private static NetNamedPipeBinding CreateNetNamedPipeBinding()
        {
            var instance = new NetNamedPipeBinding();
            instance.MaxBufferSize = 2147483647;
            instance.MaxBufferPoolSize = 2147483647;
            instance.MaxReceivedMessageSize = 2147483647;
            instance.ReaderQuotas.MaxStringContentLength = 2147483647;
            return instance;
        }

        private static Binding CreateBinding<T>()
            where T : Binding, new()
        {

            Type t = typeof(T);
            if (t == typeof(BasicHttpBinding))
            {
                return CreateBasicHttpBinding();
            }
            else if (t == typeof(WSHttpBinding))
            {
                return CreateWSHttpBinding();
            }
            else if (t == typeof(WSDualHttpBinding))
            {
                return CreateWSDualHttpBinding();
            }
            else if (t == typeof(NetTcpBinding))
            {
                return CreateNetTcpBinding();
            }
            else if (t == typeof(NetNamedPipeBinding))
            {
                return CreateNetNamedPipeBinding();
            }
            else
            {
                T instance = new T();
                return instance;
            }
        }


        public static IServ CreateClient<IServ, TBinding>(string uri)
            where TBinding : Binding, new()
        {
            ChannelFactory<IServ> proxy = 
                new ChannelFactory<IServ>(
                    CreateBinding<TBinding>(),
                    new EndpointAddress(uri));
            return proxy.CreateChannel();
        }

        public static IServ CreateClient<IServ, TBinding, TCallback>(string uri)
            where TBinding : Binding, new()
            where TCallback : new()
        {
            DuplexChannelFactory<IServ> proxy =
                new DuplexChannelFactory<IServ>(
                    new InstanceContext(new TCallback()),
                    CreateBinding<TBinding>());
            return proxy.CreateChannel(new EndpointAddress(uri));
        }

    }
}
