using System;
using SysApp = System.Windows.Forms.Application;

namespace NFox.Pycad.Setup
{
    static class Program
    {
        /// <summary>
        /// 应用程序的主入口点。
        /// </summary>
        [STAThread]
        static void Main()
        {
            SysApp.EnableVisualStyles();
            SysApp.SetCompatibleTextRenderingDefault(false);
            SysApp.Run(new frmSetup());
        }
    }
}
