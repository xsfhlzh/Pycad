using GrxCAD.Runtime;

[assembly: ExtensionApplication(typeof(NFox.Pycad.Gcad.Application))]

namespace NFox.Pycad.Gcad
{
    public class Application: Pycad.Application, IExtensionApplication
    {
        protected override void OnInitializing()
        {
            GrxCAD.ApplicationServices.Application.DocumentManager.MdiActiveDocument.Editor.WriteMessage("\nPycad Loading......");
            HostAppName = "gcad";
            base.OnInitializing();
        }

    }

}
