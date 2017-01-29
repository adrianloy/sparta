#!/usr/bin/python

'''this module used to parse w3af xml report'''
__author__ = 'adrian'

import xml.dom.minidom
import re
import datagraph.node as gnode

class W3afParser:

    def __init__(self,data_graph, xml_input):
        '''constructor function, need a w3af xml file name as the argument. Adds vulnNodes to the gui dom'''
        self.__vulnodes = []

        try:
            self.__dom = xml.dom.minidom.parse(xml_input)
            targetstr = self.__dom.getElementsByTagName('scan-info')[0].getAttribute('target')
            ipfinds = re.findall(r'[0-9]+(?:\.[0-9]+){3}', targetstr)
            if len(ipfinds) > 0:
                self.host = ipfinds[0]
            ipportfinds = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', targetstr)
            if len(ipportfinds) == 0:
                #if port 80 is specified, w3af omits printing the port at target
                self.port = '80'
            else:
                split = ipportfinds[0].split(":")
                self.port = split[1]
            for vul_xml_node in self.__dom.getElementsByTagName('vulnerability'):
                severity = vul_xml_node.getAttribute('severity')
                url = vul_xml_node.getAttribute('url')
                name = vul_xml_node.getAttribute('name')
                descr = vul_xml_node.getElementsByTagName('description')[0].firstChild.data
                if len(vul_xml_node.getElementsByTagName('long-description')) == 0:
                    longdescr = ''
                else:
                    longdescr = vul_xml_node.getElementsByTagName('long-description')[0].firstChild.data
                if len(vul_xml_node.getElementsByTagName('fix-guidance')) == 0:
                    fixstr = ''
                else:
                    fixstr = vul_xml_node.getElementsByTagName('fix-guidance')[0].firstChild.data
                newnode = gnode.VulNode(data_graph, severity, url,name, descr, longdescr, fixstr)
                self.__vulnodes.append(newnode)
        except Exception as ex:
            print "\t[-] Parser error! Invalid w3af xml output file!"
            print(str(ex))
            raise

    def getVulNodes(self):
        return self.__vulnodes

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port


class HydraParser:

    def __init__(self,data_graph, hydraoutstr):
        '''constructor function, need a w3af xml file name as the argument. Adds vulnNodes to the gui dom'''
        self.__vulnodes = []
        self.host = re.findall(r'[0-9]+(?:\.[0-9]+){3}', targetstr)[0]
        portstr = re.findall(r'port [0-9]+', targetstr)[0]
        self.port = portstr[5:]
        split = finds[0].split(":")

        for line in hydraoutstr.split('\n'):
            for vul_xml_node in self.__dom.getElementsByTagName('vulnerability'):
                severity = vul_xml_node.getAttribute('severity')
                url = vul_xml_node.getAttribute('url')
                name = vul_xml_node.getAttribute('name')
                descr = vul_xml_node.getElementsByTagName('description')[0].firstChild.data
                if len(vul_xml_node.getElementsByTagName('long-description')) == 0:
                    longdescr = ''
                else:
                    longdescr = vul_xml_node.getElementsByTagName('long-description')[0].firstChild.data
                if len(vul_xml_node.getElementsByTagName('fix-guidance')) == 0:
                    fixstr = ''
                else:
                    fixstr = vul_xml_node.getElementsByTagName('fix-guidance')[0].firstChild.data
                newnode = gnode.VulNode(data_graph, severity, url,name, descr, longdescr, fixstr)
                self.__vulnodes.append(newnode)
        #except Exception as ex:
        #    print "\t[-] Parser error! Invalid w3af xml output file!"
        #    print(str(ex))
        #    raise

    def getVulNodes(self):
        return self.__vulnodes

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port


def test():
    print('start test')
    myparser = W3afParser('/home/adrian/Documents/WS16/security/w3afScanAsus.xml')
    #myparser = W3afParser(path)

if __name__ == '__main__':
    myparser = W3afParser(None,'/home/adrian/Documents/WS16/security/w3afScanAsus.xml')
