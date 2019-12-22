namespace NFox.Pycad.Core.Modules
{

    public class io
    {

        private static io _obj;
        public static io instance => _obj ?? (_obj = new io());

        private io() { }

        private dynamic _console;
        public dynamic ed { get; set; }

        public void redirect(dynamic console = null)
        {
            _console = console;
        }

        public string readline()
        {
            var opts = Engine.Instance.Execute("aced.PromptStringOptions")("");
            opts.AllowSpaces = true;
            var res = ed.GetString(opts);
            var buf = System.Environment.NewLine;
            if (res.Status == Engine.Instance.Execute("aced.PromptStatus.OK"))
                buf = res.StringResult + buf;
            return buf;
        }

        public void write(string s)
        {
            if (_console != null)
                _console.write(s);
            else
                ed.WriteMessage(s);
        }

        public bool softspace { get; set; }

    }

}
