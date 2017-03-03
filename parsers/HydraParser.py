#!/usr/bin/python

'''this module used to parse w3af xml report'''
__author__ = 'adrian'

import xml.dom.minidom
import re
import datagraph.node as gnode


class HydraParser:

    def __init__(self,data_graph, hydraoutstr):
        '''constructor function, need a w3af xml file name as the argument. Adds vulnNodes to the gui dom'''
        self.__vulnodes = []
        ipfinds = re.findall(r'[0-9]+(?:\.[0-9]+){3}', hydraoutstr)
        if len(ipfinds) > 0:
            self.host = ipfinds[0]
        portfinds = re.findall(r'port [0-9]+', hydraoutstr)
        if len(portfinds) > 0:
            self.port = portfinds[0][5:]
        if 'password: ' in hydraoutstr:
            login = re.findall(r'login: [a-z]+',hydraoutstr)[0]
            pw = re.findall(r'password: [a-z]+',hydraoutstr)[0]
            login = login[7:]
            pw = pw[10:]

            descr = 'Unsafe credentials used'
            longdescr = 'The service uses these unsafe credentials: login: ' + login + ' \t password: ' + pw
            severity = '5.0'
            name = 'Unsafe credentials'
            newnode = gnode.VulNode(data_graph, severity, '',name, descr, longdescr, '')
            self.__vulnodes.append(newnode)

    def getVulNodes(self):
        return self.__vulnodes

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port