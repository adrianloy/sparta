#!/usr/bin/env python

import sys
import time
from zapv2 import ZAPv2
import subprocess
import socket
import dicttoxml


target_ip = sys.argv[1]
target_port = sys.argv[2]
output = sys.argv[3] + '.xml'
if target_port == '443':
    protocol = 'https'
else:
    protocol = 'http'

zap = '/opt/ZAP_2.5.0/zap.sh'
host = '127.0.0.1'
port = '8080'
api_key = 'ZAPROXY-PLUGIN'

port_number = int(port)
s = socket.socket()
connected = False
try:
    s.connect((host, port_number))
    print "Connected!"
    connected = True
except Exception as e:
    print "Couldn't connect to ZAP daemon..."
finally:
    s.close()

if not connected:
    command = 'bash ' + zap + ' -daemon -host ' + host + ' -port ' + port + ' -config api.key=' + api_key + ' > /dev/null'
    print 'Starting ZAP daemon...'
    print '!!! Remember to shutdown the ZAP daemon after all scans are done !!!'
    process = subprocess.Popen(command, shell=True)
    print 'pkill -TERM -P ' + str(process.pid)

while not connected:
    s = socket.socket()
    try:
        s.connect((host, port_number))
        print "Connected!"
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
print '(Report every 10 sec)'
scan_id = zap.ascan.scan(target_url, apikey=api_key)
while int(zap.ascan.status(scan_id)) < 100:
    print 'Scan progress %: ' + zap.ascan.status(scan_id)
    time.sleep(10)

print 'Scan completed'
print 'Results written in ' + output

with open(output, 'w') as f:
    f.write('<?xml version="1.0" ?>')
    f.write('<zap>')
    for alert in zap.core.alerts():
        xml = dicttoxml.dicttoxml(alert, root=False)
        f.write('<issue>')
        f.write(xml)
        f.write('</issue>')
    f.write('</zap>')
