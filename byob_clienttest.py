import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
print(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWJgYCgtyskvSM3TUM8oKSmw0tc3NNCz1DM0NNIztrAyNTU109fXLy5JTE8tKtYvDDDRK6hU19QrSk1M0dAEAC0iEbo='))))