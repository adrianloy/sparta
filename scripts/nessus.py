#!/usr/bin/env python

import os
import nessrest.ness6rest as ness
import sys


def run_standard_test(ip,port,outputpath):
    login = os.getenv("NESSUS_USER")
    password = os.getenv("NESSUS_PASSWORD")
    url = "https://%s:%s" % (os.getenv("NESSUS_SERVER"), os.getenv("NESSUS_PORT", "8834"))

    scan = ness.Scanner(url=url, login=login, password=password, insecure=True)
    #scan._policy_template_uuid("basic") #no policy needed if nessrest is bleeding edge (compiled source
    #if not scan.policy_exists("sparta scan123"):
    #    scan.policy_add(name="sparta scan123", plugins="22373", template="basic")
    #scan.policy_set(name="sparta scan")
    scan.scan_add(targets=ip, template="basic", name="SPARTA scan")
    scan.scan_run()
    scan.scan_results() #somehow doesnt do anything
    result = scan.download_scan(export_format="csv") #allowed values are [\"nessus\",\"csv\",\"db\",\"html\",\"pdf\"]"

    moddedFile = open(outputpath + ".csv", 'w')
    moddedFile.write(result)
    moddedFile.close()

if __name__ == '__main__':
    target_ip = sys.argv[1]
    #target_port = sys.argv[2]
    output = sys.argv[2]
    run_standard_test(target_ip, "", output)
