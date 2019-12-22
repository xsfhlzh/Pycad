using System;
using System.Diagnostics;
using System.IO;
using System.Net;

namespace NFox.DebugTest
{
    class Program
    {
        static void Main(string[] args)
        {

            //Process process = new Process();
            //process.StartInfo.FileName = "C:\\Program Files\\Autodesk\\AutoCAD 2016\\accoreconsole.exe";
            //process.StartInfo.UseShellExecute = false;   // 是否使用外壳程序 
            //process.StartInfo.RedirectStandardInput = true;  // 重定向输入流 
            //process.Start();

            //process.StandardInput.WriteLine("netload");
            //process.StandardInput.WriteLine("d:\\pycad\\nfox.pycad.acad.dll");
            //while(true)
            //{
            //    process.StandardInput.WriteLine(Console.ReadLine());
            //}
            DebugClient client = new DebugClient();
            client.Receive();
        }

    }
}
