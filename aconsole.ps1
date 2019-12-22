# 控制台程序路径
$key = Get-Item HKLM:\Software\Autodesk\Hardcopy
$arr = @()
foreach($value in $key.Property){
    $arr += Get-Item HKLM:\Software\$value
}
$arr = $arr | sort
$_values = Get-ItemProperty $arr[$arr.Count - 1].PSPath
$MyConsole = $_values.Location + "\accoreconsole.exe"

# 设置进程启动信息
$psi= New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $MyConsole
# 设置进程自动重定向输入
$psi.UseShellExecute = $false
$psi.RedirectStandardInput = $true
$process = New-Object System.Diagnostics.Process
$process.StartInfo = $psi

$null = $process.Start()
$process.StandardInput.WriteLine("netload")
$dir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$process.StandardInput.WriteLine($dir + "\NFox.Pycad.Acad.dll")

while($true){
    $process.StandardInput.WriteLine([Console]::ReadLine())
}







