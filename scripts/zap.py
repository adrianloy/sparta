#!/usr/bin/env python

import os
import sys
import time
from pprint import pprint
from zapv2 import ZAPv2
import atexit
import subprocess
import signal


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
process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)

#def kill_thread():
#    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
#
#atexit.register(kill_thread)

print 'wait 30 sec...'
time.sleep(30)

zap = ZAPv2(proxies={'http': 'http://' + host + ':' + port})

target_url = protocol + '://' + target_ip + ':' + target_port

print 'Accessing target %s' % target_url
# try have a unique enough session...
zap.urlopen(target_url)
# Give the sites tree a chance to get updated
time.sleep(2)

print 'Spidering target %s' % target_url
scanid = zap.spider.scan(target_url, apikey=api_key)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status(scanid)) < 100):
    print 'Spider progress %: ' + zap.spider.status(scanid)
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)

print 'Scanning target %s' % target_url
scanid = zap.ascan.scan(target_url, apikey=api_key)
while (int(zap.ascan.status(scanid)) < 100):
    print 'Scan progress %: ' + zap.ascan.status(scanid)
    time.sleep(5)

print 'Scan completed'

# Report the results

print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint(zap.core.alerts())
