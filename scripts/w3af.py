#!/usr/bin/env python

import os
import sys
import subprocess

ip = sys.argv[1]
port = sys.argv[2]
output = sys.argv[3]

script = '''
profiles
    use OWASP_TOP10
back

plugins
    output console, xml_file
    output config xml_file
        set output_file [[VAR_OUTFILE]]
    back
back

target
    set target [[VAR_TARGET_URL]]
back

start
exit
'''

script_file_path = "/tmp/script.w3af"
script = script.replace('[[VAR_TARGET_URL]]', ip + ":" + port)
script = script.replace('[[VAR_OUTFILE]]', output + ".xml")
moddedFile = open(script_file_path, 'w')
moddedFile.write(script)
moddedFile.close()

command = "w3af_console -s " + script_file_path

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
for line in iter(process.stdout.readline, ''):
    print line.rstrip()

