
using Autodesk.AutoCAD.Runtime;

[assembly: ExtensionApplication(typeof(NFox.Pycad.Aconsole.Application))]

namespace NFox.Pycad.Aconsole
{
    public class Application : Pycad.Application, IExtensionApplication
    {
        protected override void OnInitializing()
        {
            HostAppName = "acad";
            base.OnInitializing();
        }

    }

}
