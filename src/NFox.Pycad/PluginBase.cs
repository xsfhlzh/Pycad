using System;
using System.Collections.Generic;
using System.Reflection;

namespace NFox.Pycad
{
    public abstract class PluginBase
    {
        
        public PluginInfo Info { get; set; }

        public virtual string Name
        {
            get { return GetType().Namespace; }
        }

        public static string HostAppName{ get; protected set; }

        public static string CurrSystem { get; protected set; }

        public Assembly Assembly { get; set; }

        public static PluginBase Root { get; internal set; }

        protected static Dictionary<string, PluginBase> _plugins;

        public static PluginBase GetPlugin(string name)
        {
            return _plugins[name];
        }

        public dynamic Parent { get; internal set; }


        public Dictionary<string, PluginBase> Children { get; } 
            = new Dictionary<string, PluginBase>();

        protected virtual void OnLoading() { }
        protected virtual void OnLoaded() { }

        protected virtual void OnUnloading() { }
        protected virtual void OnUnloaded() { }

        protected virtual void OnInitializing() { }
        protected virtual void OnInitializd() { }
        protected virtual void OnTerminating() { }
        protected virtual void OnTerminated() { }

        public void Add(PluginBase p)
        {
            p.Parent = this;
            Children.Add(p.Name, p);
        }

        public void Remove(PluginBase p)
        {
            Children.Remove(p.Name);
        }

        public void Start()
        {
            OnLoading();
            foreach (var p in Children)
                p.Value.Start();
            OnLoaded();
        }

        public void End()
        {
            OnUnloading();
            foreach (var p in Children)
                p.Value.End();
            OnUnloaded();
        }

        private bool _initialized;
        public void Initialize()
        {
            if (!_initialized)
            {
                _initialized = true;
                OnInitializing();
                foreach(var p in Children)
                    p.Value.Initialize();
                OnInitializd();
            }
        }

        private bool _terminated;
        public void Terminate()
        {
            if (!_terminated)
            {
                _terminated = true;
                OnTerminating();
                foreach (var p in Children)
                    p.Value.Terminate();
                OnTerminated();
            }
        }

        public void SendMessage(string message, params dynamic[] args)
        {
            if (OnMessage(message, args)) return;
            foreach (var child in Children)
                child.Value.SendMessage(message, args);
        }

        protected virtual bool OnMessage(string message, dynamic [] args) => false;

    }

}
