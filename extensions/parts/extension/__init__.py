# 引用.net程序集
import clr, pycad.system
clr.AddReferenceToFileAndPath(pycad.system.findfile('NFox.Expression.dll'))

#Overrule支持
import extension.overrules
