#!/usr/bin/env python

import os
import nessrest.ness6rest as ness
import sys

def run_standard_test(ip,port,outputpath):
    login = os.getenv("NESSUS_USER")
    password = os.getenv("NESSUS_PASSWORD")
    url = "https://%s:%s" % (os.getenv("NESSUS_SERVER"), os.getenv("NESSUS_PORT", "8834"))

    login = "A_Student"
    password = "nessus3141"
    url = "https://192.168.1.180:8834"

    scan = ness.Scanner(url=url, login=login, password=password, insecure=True)
    #scan._policy_template_uuid("basic")
    if not scan.policy_exists("sparta scan123"):
        scan.policy_add(name="sparta scan123", plugins="22373", template="basic")
    scan.policy_set(name="sparta scan")
    scan.scan_add(targets=ip, template="basic", name="SPARTA scan")
    scan.scan_run()

if __name__ == '__main__':
    #target_ip = sys.argv[1]
    #target_port = sys.argv[2]
    #output = sys.argv[3]
    run_standard_test('192.168.1.151', '8080', '/tmp/')
