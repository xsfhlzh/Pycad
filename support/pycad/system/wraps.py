from pycad.system.mgdnss import *

def guid(gid = None):
    from System import Guid
    return gid and Guid(gid) or Guid.NewGuid()

def help(o):
    import pydoc
    pydoc.help(o)

class switch(object):
    def __init__(self, value):
        self.value = value
    def __call__(self, *args):
        return self.value in args
    def __getitem__(self, *args):
        return isinstance(self.value, args)
    def __lt__(self, other):
        return self.value < other
    def __gt__(self, other):
        return self.value > other
    def __le__(self, other):
        return self.value <= other
    def __ge__(self, other):
        return self.value >= other
    def match(self, func):
        return func(self.value)

def flatten(nested):
    case = switch(nested)
    if case[str]:
        yield nested
    else:
        try:
            for sublist in nested:
                for element in flatten(sublist):
                    yield element
        except TypeError:
            yield nested


        