#!/usr/bin/env python

import os
import nessrest.ness6rest as ness
import sys

def run_standard_test(ip,port,outputpath):
    login = os.getenv("NESSUS_USER")
    password = os.getenv("NESSUS_PASSWORD")
    #url = "https://%s:%s" % (os.getenv("NESSUS_SERVER"), os.getenv("NESSUS_PORT", "8834"))

    login = "A_Student"
    password = "nessus3141"
    url = "https://192.168.1.180:8834"

    scan = ness.Scanner(url=url, login=login, password=password)

    hosts = [{'hostname': 'host1', 'host_id': '1'},
             {'hostname': 'host1', 'host_id': '1'},
             {'hostname': 'host2', 'host_id': '2'}]
    unique_hosts = scan._deduplicate_hosts(hosts=hosts)
    assert unique_hosts  == \
        [{'hostname': 'host2', 'host_id': '2'},
         {'hostname': 'host1', 'host_id': '1'}]

    assert scan._deduplicate_hosts(hosts=[]) == []

if __name__ == '__main__':
    #target_ip = sys.argv[1]
    #target_port = sys.argv[2]
    #output = sys.argv[3]
    run_standard_test('192.168.1.151','8080','/tmp/')