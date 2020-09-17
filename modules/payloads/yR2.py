
import urllib,json
from urllib import request
urlopen = urllib.request.urlopen
pure_tasks=urlopen('https://raw.githubusercontent.com/xbubus/http-mqtt-requests-generator-sender/master/http_out.json').read().decode('utf-8')
print(pure_tasks)
pure_tasks=json.loads(pure_tasks)
print(pure_tasks)