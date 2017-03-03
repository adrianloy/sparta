#!/usr/bin/env python

import os
import sys
import subprocess

ip = sys.argv[1]
port = sys.argv[2]
output = sys.argv[3]

script1 = '''
# -----------------------------------------------------------------------------------------------------------
#                                              W3AF AUDIT SCRIPT FOR WEB APPLICATION
# -----------------------------------------------------------------------------------------------------------
#This script will be run by Sparta when web vulnerability scanning is enabled
#You can customize this script.
#It must be valid w3af scripting syntax and have the string [[VAR_TARGET_URL]] whereever a target URL would be inserted.
#Configure HTTP settings
http-settings
set timeout 30
back
#Configure scanner global behaviors
misc-settings
set max_discovery_time 20
set fuzz_cookies True
set fuzz_form_files True
set fuzz_url_parts True
set fuzz_url_filenames True
back
plugins
#Configure entry point (CRAWLING) scanner
crawl web_spider
crawl config web_spider
set only_forward False
set ignore_regex (?i)(logout|disconnect|signout|exit)+
back
#Configure vulnerability scanners
##Specify list of AUDIT plugins type to use
audit blind_sqli, buffer_overflow, cors_origin, csrf, eval, file_upload, ldapi, lfi, os_commanding, phishing_vector, redos, response_splitting, sqli, xpath, xss, xst
##Customize behavior of each audit plugin when needed
audit config file_upload
set extensions jsp,php,php2,php3,php4,php5,asp,aspx,pl,cfm,rb,py,sh,ksh,csh,bat,ps,exe
back
##Specify list of GREP plugins type to use (grep plugin is a type of plugin that can find also vulnerabilities or informations disclosure)
grep analyze_cookies, click_jacking, code_disclosure, cross_domain_js, csp, directory_indexing, dom_xss, error_500, error_pages,
html_comments, objects, path_disclosure, private_ip, strange_headers, strange_http_codes, strange_parameters, strange_reason, url_session, xss_protection_header
##Specify list of INFRASTRUCTURE plugins type to use (infrastructure plugin is a type of plugin that can find informations disclosure)
infrastructure server_header, server_status, domain_dot, dot_net_errors
#Configure target authentication
auth detailed
auth config detailed
set username admin
set password password
set method POST
set auth_url [[VAR_TARGET_URL]]/login.php
set username_field user
set password_field pass
set check_url [[VAR_TARGET_URL]]/index.php
set check_string 'admin'
set data_format username=%U&password=%P&Login=Login
back
#Configure reporting in order to generate an HTML report
output console, xml_file
output config xml_file
set output_file [[VAR_OUTFILE]]
set verbose False
back
output config console
set verbose False
back
back
#Set target informations, do a cleanup and run the scan
target
set target [[VAR_TARGET_URL]]
#set target_os windows
#set target_framework php
back
cleanup
start
exit
'''

script2 = '''
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

script = script2
script_file_path = "/tmp/script.w3af"
script = script.replace('[[VAR_TARGET_URL]]', ip + ":" + port)
script = script.replace('[[VAR_OUTFILE]]', output + ".xml")
moddedFile = open(script_file_path, 'w')
moddedFile.write(script)
moddedFile.close()

if os.path.exists('/home/cedric/git/w3af/w3af_console'):
    command = "/home/cedric/git/w3af/w3af_console -s " + script_file_path
else:
    command = "w3af_console -s " + script_file_path

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
for line in iter(process.stdout.readline, ''):
    print line.rstrip()

