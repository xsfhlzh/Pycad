using Newtonsoft.Json;
using System;
using System.Net.Sockets;
using System.Text;

namespace NFox.Pycad.Servers.Tcp
{
    public abstract class LinkBase
    {

        protected Socket _socket;

        protected static int _maxlengthofdata;
        protected byte[] _buffer;

        static LinkBase()
        {
            _maxlengthofdata = 1024;
        }

        public void Close()
        {
            _socket.Close();
        }

        private static byte[] GetBytes(MessageType type, string content)
        {
            Message m = new Message() { Type = type, Content = content };
            var json = JsonConvert.SerializeObject(m);
            return Encoding.UTF8.GetBytes(json);
        }

        private static Message GetMessage(byte[] bytes, int count)
        {
            var json = Encoding.UTF8.GetString(bytes, 0, count);
            return JsonConvert.DeserializeObject<Message>(json);
        }

        public void Send(MessageType type, string content = null)
        {
            var bytes = GetBytes(type, content);
            int count = bytes.Length;

            if (count > _maxlengthofdata)
            {
                int rest = 0;
                int n = Math.DivRem(count, _maxlengthofdata, out rest);
                int num = rest > 0 ? n + 1 : n;
                var nbytes = GetBytes(MessageType.BigData, $"{num};{count}");
                _buffer = new byte[_maxlengthofdata];
                nbytes.CopyTo(_buffer, 0);
                _socket.Send(_buffer);

                int i = 0;
                for (; i < n; i++)
                {
                    Array.Copy(bytes, i * _maxlengthofdata, _buffer, 0, _maxlengthofdata);
                    _socket.Send(_buffer);
                }

                if (rest > 0)
                {
                    _buffer = new byte[_maxlengthofdata];
                    Array.Copy(bytes, i * _maxlengthofdata, _buffer, 0, rest);
                    _socket.Send(_buffer);
                }

            }
            else
            {
                _buffer = new byte[_maxlengthofdata];
                bytes.CopyTo(_buffer, 0);
                _socket.Send(_buffer);
            }
        }

        public void Receive()
        {
            _buffer = new byte[_maxlengthofdata];
            int count = _socket.Receive(_buffer, _maxlengthofdata, SocketFlags.None);
            var m = GetMessage(_buffer, count);
            if (m.Type == MessageType.BigData)
            {
                var arr = m.Content.Split(';');
                int n = int.Parse(arr[0]);
                int total = int.Parse(arr[1]);

                byte[] buffer = new byte[n * _maxlengthofdata];
                for (int i = 0; i < n; i++)
                {
                    _socket.Receive(_buffer, _maxlengthofdata, SocketFlags.None);
                    _buffer.CopyTo(buffer, i * _maxlengthofdata);
                }
                m = GetMessage(buffer, total);
            }
            if (m.Type == MessageType.End)
            {
                Response(m);
                _socket.Close();
            }
            else if (Response(m))
            {
                Receive();
            }
        }

        int _num = 0;
        int _index = 0;
        int _total = 0;
        byte[] _bigbuffer;


        protected abstract bool Response(Message message);


        public void BegineReceive()
        {
            _buffer = new byte[_maxlengthofdata];
            _socket.BeginReceive(_buffer, 0, _maxlengthofdata, SocketFlags.None, EndReceive, null);
        }

        private void EndReceive(IAsyncResult ar)
        {
            int count = _socket.EndReceive(ar);
            if (_num > 0)
            {
                _buffer.CopyTo(_bigbuffer, _index++ * _maxlengthofdata);
                if (_index == _num)
                {
                    _num = _index = 0;
                    var m = GetMessage(_bigbuffer, _total);
                    _bigbuffer = null;
                    if (Response(m))
                        BegineReceive();
                }
            }
            else
            {
                var m = GetMessage(_buffer, count);
                if (m.Type == MessageType.BigData)
                {
                    var arr = m.Content.Split(';');
                    _num = int.Parse(arr[0]);
                    _total = int.Parse(arr[1]);
                    _index = 0;
                    _bigbuffer = new byte[_num * _maxlengthofdata];
                }
                else if (m.Type == MessageType.End)
                {
                    Response(m);
                    _socket.Close();
                }
                else if (Response(m))
                {
                    BegineReceive();
                }
            }
            
        }



    }
}
