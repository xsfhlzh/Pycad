from pycad.system import *
from pycad.runtime import *

_filename = None


@command()
def pyrun(doc):
    pfo = aced.PromptOpenFileOptions("选择Python脚本")
    pfo.Filter = "Python脚本文件(*.py)|*.py"
    pfo.PreferCommandLine = acapp.GetSystemVariable("FILEDIA") == 0
    pfo.InitialDirectory = pye.extensionspath + "\\.scripts\\"
    global _filename
    pfo.InitialFileName = _filename
    pr = doc.Editor.GetFileNameForOpen(pfo)
    if pr.Status == aced.PromptStatus.OK:
        try:
            pye.executefile(pr.StringResult)
            _filename = pr.StringResult.rsplit('\\',1)[1]
        except: pass


@command()
def pyreference(doc):
    pfo = aced.PromptOpenFileOptions("选择.Net类库")
    pfo.Filter = ".Net类库(*.dll)|*.dll"
    pfo.PreferCommandLine = acapp.GetSystemVariable("FILEDIA") == 0
    pr = doc.Editor.GetFileNameForOpen(pfo)
    if pr.Status == aced.PromptStatus.OK:
        pye.reference(pr.StringResult)


def isvarname(name):
    b = name[0].isalpha() or name[0] == '_'
    if b:
        for i in name[1:]:
            if not (i.isalnum() or i == '_'):
                return False
    return b


lastindex = 0


@command()
def pyedit(doc):
    from ctypes import windll
    windll.user32.keybd_event(0x71, 0, 0, 0)
    exts = pye.extensions
    print("\n编辑或创建项目\n已创建%s个项目:" % exts.Count)
    i = 0
    for ext in exts:
        i += 1
        print("%s. %s" % (i, ext))
    global lastindex
    opts = aced.PromptIntegerOptions("\n请输入要打开项目的序号或[创建新项目(E)/编辑支持模块(O)/创建支持模块(S)]", "E O S")
    opts.DefaultValue = lastindex + 1
    opts.AllowNone = True
    res = edx.getint(opts)
    while res.ok() and (res.value < 1 or res.value > exts.Count):
        print("警告! 序号索引超出范围.")
        res = edx.getint(opts)
    if res.ok():
        lastindex = res.value - 1
        pye.open_extension(exts[lastindex].Name)
    elif res.keyword('E'):
        res2 = edx.getstr("\n请输入新建项目名称")
        names = [e.Name for e in exts]
        while res2.ok():
            if res2.value in names:
                print("警告! 名称与现有项目重名.")
            elif isvarname(res2.value):
                break
            else:
                print("警告! 不合法的项目名.")
            res2 = edx.getstr("\n请重新输入新建项目名称")
        if res2.ok():
            print("成功创建新项目: %s" % res2.value)
            pye.create_extension(res2.value)
    elif res.keyword('S'):
        res2 = edx.getstr("\n请输入支持模块名称")
        mods = pye.supportmodules
        names = [m.Name for m in mods]
        while res2.ok():
            if res2.value in names:
                print("警告! 名称与现有模块重名.")
            elif isvarname(res2.value):
                break
            else:
                print("警告! 不合法的模块名.")
                res2 = edx.getstr("\n请重新输入支持模块名称")
        if res2.ok():
            pye.create_supportmodule(res2.value)
            print("成功创建支持模块: %s" % res2.value)
    elif res.keyword('O'):
        pye.open_support()


@command()
def pyrelease(doc):
    from ctypes import windll
    windll.user32.keybd_event(0x71, 0, 0, 0)
    exts = [e for e in pye.extensions if e.Name != "pycad"]
    print("\n发布项目\n已创建%s个项目:" % len(exts))
    i = 0
    for ext in exts:
        i += 1
        print("%s. %s" % (i, ext))
    global lastindex
    opts = aced.PromptStringOptions("\n请输入要发布项目的序号, 以逗号分隔(默认全选)")
    opts.UseDefaultValue = True
    opts.DefaultValue = ""
    res = edx.getstr(opts)
    ids = set(range(1, len(exts) + 1))
    while res.ok():
        if res.value == "":
            sels = ids
            break
        try:
            sels = set(eval("[%s]" % res.value))
            if sels.issubset(ids): break
        except:
            pass
        print("警告! 输入错误")
        res = edx.getstr(opts)
    if not res.ok(): return
    import System
    opts = aced.PromptStringOptions("\n请输入安装包名称")
    opts.UseDefaultValue = True
    opts.DefaultValue = System.Environment.MachineName
    res = edx.getstr(opts)
    if res.ok():
        pye.release(res.value, tuple(exts[i - 1] for i in sels))
