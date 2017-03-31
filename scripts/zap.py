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

zap = 'zap.sh'
host = '127.0.0.1'
port = '8080'
api_key = 'ZAPROXY'
spidering = True

port_number = int(port)
s = socket.socket()
connected = False
print 'Trying to connect to ZAP daemon...'
try:
    s.connect((host, port_number))
    print "Connected!"
    connected = True
except Exception as e:
    print "Couldn't connect!"
    command = zap + ' -daemon -host ' + host + ' -port ' + port + ' -config api.nokeyforsafeops=true'
    print 'You need to start a ZAP daemon first:'
    print command
finally:
    s.close()

if connected:
    zap = ZAPv2(proxies={'http': 'http://' + host + ':' + port})
    target_url = protocol + '://' + target_ip + ':' + target_port
    zap.urlopen(target_url)
    time.sleep(5)

    # TODO: remove bug
    if spidering:
		print 'Spidering target %s' % target_url
		print '(Report every 10 sec)'
		scan_id = zap.spider.scan(target_url, apikey=api_key)
		time.sleep(5)
		while int(zap.spider.status(scan_id)) < 100:
			print 'Spider progress %: ' + zap.spider.status(scan_id)
			time.sleep(10)
		print 'Spider completed!'
		time.sleep(5)

    print 'Scanning target %s' % target_url
    print '(Report every 10 sec)'
    scan_id = zap.ascan.scan(target_url, apikey=api_key)
    time.sleep(5)
    while int(zap.ascan.status(scan_id)) < 100:
        print 'Scan progress %: ' + zap.ascan.status(scan_id)
        time.sleep(10)
    print 'Scan completed!'

    with open(output, 'w') as f:
        f.write('<?xml version="1.0" ?>')
        f.write('<zap>')
        for alert in zap.core.alerts():
            xml = dicttoxml.dicttoxml(alert, root=False)
            f.write('<issue>')
            f.write(xml)
            f.write('</issue>')
        f.write('</zap>')
    print 'Results written in ' + output
