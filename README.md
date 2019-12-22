# Pycad
Python Extension for AutoCad
使用方法：
1、程序支持AutoCad2013-2020（2014版本以下需安装.Net4.5），将压缩文件下载后解压到任意目录，在AutoCad在用Netload命令选择解压目录中的NFox.Pycad.Acad.dll，同时支持浩辰Cad，对应加载文件为NFox.Pycad.Gcad.dll。
2、程序选用vscode作为编辑器，在Cad中键入pye命令，可以自动打开vscode，当然你需要安装vscode，以及vscode的Python扩展（微软）和Pythonv3.7+。
3、如果代码修改完成，在Cad中键入pyrb命令可以即时编译python的脚本。
4、pytest项目有很多例程可以参考。
5、vscode右下角有一个即时窗口，可以直接在这里键入或者从代码区拷贝代码直接执行看结果
6、发布功能和调试功能修改中。。。
感谢山人编写的文档，但是改版暂时只能借鉴了，我们一起把他顶出来写新版的吧：）
如果pye命令出现“系统找不到指定的文件”的错误，请按下面的目录找到配置文件，修改对应的参数为vscode的安装目录
