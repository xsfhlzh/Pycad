import _ast

mros = (
    reversed(t.mro())
    for t in (eval("_ast." + name) for name in dir(_ast))
    if hasattr(t, "mro"))
tree = {}
for m in mros:
    d = tree
    for t in m:
        name = t.__name__
        if name not in d: d[name] = {}
        d = d[name]

for key, value in tree['object']['AST'].items():
    if hasattr(eval("_ast." + key), "body"):
        print('case "%s":' % key)
    for skey in value:
        if hasattr(eval("_ast." + skey), "body"):
            print('case "%s":' % skey)


def f(tree):
    s = ''
    for key, value in tree.items():
        if len(value) > 0:
            s += 'if (name == "%s"))\n{\n%s\n}\n' % (key, f(value))
        else:
            s += 'if (name == "%s"))\nreturn new %s(tree);\n' % (key, key[0].upper() + key[1:].lower())
    return s


s = f(tree['object']['AST'])
print(s)
