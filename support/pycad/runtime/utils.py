
__all__ = ['getvalue', 'setvalue', 'getcomobject', 'zipto', 'unzipfrom']

_dict = {}

def getvalue(key):
    global _dict
    return _dict.get(key)

def setvalue(key, value = None):
    global _dict
    _dict[key] = value

def getcomobject(progid):
    import System
    t = System.Type.GetTypeFromProgID(progid)
    return System.Activator.CreateInstance(t)

def zipto(dirname, zipfilename):
    import os, os.path
    import zipfile
    z = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    if os.path.isfile(dirname):
        filename = os.path.basename(dirname)
        z.write(filename, dirname)
    else:
        if dirname[-1] in ('\\', '/'):
            dirname = dirname[:-1]
        d = len(dirname)
        for filename in (
            os.path.join(root, filename)
            for root, _, files in os.walk(dirname) 
            for filename in files):
            z.write(filename[d:], filename)
    z.close()

def unzipfrom(zipfilename, dirname):
    import os, os.path
    import zipfile
    if not os.path.exists(dirname): os.mkdir(dirname)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        if name.endswith('/'):
            os.mkdir(os.path.join(dirname, name))
        else:            
            ext_filename = os.path.join(dirname, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir): os.mkdir(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


