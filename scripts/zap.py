#!/usr/bin/env python

import os
import sys
import time
from pprint import pprint
from zapv2 import ZAPv2
import subprocess
import socket


target_ip = sys.argv[1]
target_port = sys.argv[2]
output = sys.argv[3]
if target_port == '443':
    protocol = 'https'
else:
    protocol = 'http'

zap = '/opt/ZAP_2.5.0/zap.sh'
host = '127.0.0.1'
port = '8080'
api_key = 'ZAPROXY-PLUGIN'

command = 'bash ' + zap + ' -daemon -host ' + host + ' -port ' + port + ' -config api.key=' + api_key + ' > ' + output
print 'Starting ZAP daemon...'
print '!!! Remember to shutdown the ZAP daemon after all scans are done !!!'
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

connected = False
port_number = int(port)
while not connected:
    s = socket.socket()
    try:
        s.connect((host, port_number))
        connected = True
    except Exception as e:
        print 'Retrying to connect in 10 sec...'
        time.sleep(10)
    finally:
        s.close()

zap = ZAPv2(proxies={'http': 'http://' + host + ':' + port})
target_url = protocol + '://' + target_ip + ':' + target_port
zap.urlopen(target_url)
time.sleep(10)
print 'Scanning target %s' % target_url
print '(report every 10 sec)'
scan_id = zap.ascan.scan(target_url, apikey=api_key)
while int(zap.ascan.status(scan_id)) < 100:
    print 'Scan progress %: ' + zap.ascan.status(scan_id)
    time.sleep(10)

print 'Scan completed'

print 'Alerts: '
for alert in zap.core.alerts():
    pprint(alert)
