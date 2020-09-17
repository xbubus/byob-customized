

import util

# globals
command = True
packages = ['util']
platforms = ['win32','linux2','darwin']
usage = 'screenshot [imgur/ftp] [option=value, ...]'
description = """
Capture a screenshot on the client and optionally upload anonymously to
Imgur or to a remote FTP server (default: save image on local host machine)
"""
#util.log('HELLO FROM TEST LOG')
#print('TEST PRINT')

def print():
    try:
        print('TEST PRINT2')
        util.log('HELLO FROM TEST LOG2')
    
        return 'TEST PRINT RETURN ok'
    except:
        return 'TEST PRINT RETURN bad'