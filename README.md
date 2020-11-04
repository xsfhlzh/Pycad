# Pycad

Python Extension for AutoCad

Editor/Debuger

使用方法：

1、程序支持AutoCad2013-2020（2014版本以下需安装.Net4.5），将压缩文件下载后解压到任意目录，在AutoCad在用Netload命令选择解压目录中的NFox.Pycad.Acad.dll，同时支持浩辰Cad，对应加载文件为NFox.Pycad.Gcad.dll。

2、程序选用vscode作为编辑器，在Cad中键入pye命令，可以自动打开vscode，当然你需要安装vscode，以及vscode的Python扩展（微软）和Pythonv3.7+。

3、如果代码修改完成，在Cad中键入pyrb命令可以即时编译python的脚本。

4、pytest项目有很多例程可以参考。

5、vscode右下角有一个即时窗口，可以直接在这里键入或者从代码区拷贝代码直接执行看结果

6、修改py项目的组织形式,原项目组织形式为包，不能防止同名包覆盖的问题,新的项目组织形式与国际接轨, 根目录可随意命名, 保证目录下有个extension包即可, 该包不可重命名, 不可缺失；项目的data目录可放置数据文件，程序中可使用findfile(filename)获取文件路径；项目的cuix目录可放置Cad的cuix文件用于加载定制的菜单、工具条和Ribbon菜单；重写了发布功能, 命令pyrelease, 可选择多项目一起发布, 完成后会在temp目录下生成一个自解压安装包xxx.Setup.exe；可以在未安装Pycad的机器上安装Pycad的运行版本和开发的项目；pye命令名修改为pyedit。

7、调试器基本完成,提供测试，调试流程: 打开Cad->打开pytest项目->按下F5->在Cad中敲命令即可进入调试模式；退出调试只需要点vscode中的断开连接按钮。

8、修正发布功能，增加invokeArx模块以调用Arx函数，例子见pytest项目的runtime模块

感谢山人编写的文档，但是改版暂时只能借鉴了，我们一起把他顶出来写新版的吧：）

如果pye命令出现“系统找不到指定的文件”的错误，请在“Pycad\bin”目录下找到配置文件settings.json，修改“editor.path”参数为vscode的安装目录
