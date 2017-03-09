#!/usr/bin/python

from datagraph.node import *
import re

'''this module is used to parse a Nessus csv report'''
__author__ = 'adrian'


class NessusParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph

        if tool_node.file_output == '':
            print 'tool file output is empty'
            return


        output_file = tool_node.outputfile #+ '.xml'
        with open (output_file, "r") as myfile:
            data=myfile.read()
            data.replace("\n","?&%$16527")
            data.replace(",","\n")
        #encode newlines (in description strings), then split by the field separator and go through them
        #Plugin ID,CVE,CVSS,Risk,Host,Protocol,Port,Name,Synopsis,Description,Solution,See Also,Plugin Output
        datasplit = data.split("\n")
        for i in range(1,len(datasplit)-12):
           if i%13==0:
               pluginID = data[i].replace("?&%$16527","\n").replace("\"","")
               CVE = data[i+1].replace("?&%$16527","\n").replace("\"","")
               CVSS = data[i+2].replace("?&%$16527","\n").replace("\"","")
               risk = data[i+3].replace("?&%$16527","\n").replace("\"","")
               host = data[i+4].replace("?&%$16527","\n").replace("\"","")
               protocol = data[i+5].replace("?&%$16527","\n").replace("\"","")
               port = data[i+6].replace("?&%$16527","\n").replace("\"","")
               name = data[i+7].replace("?&%$16527","\n").replace("\"","")
               synopsis = data[i+8].replace("?&%$16527","\n").replace("\"","")
               descr = data[i+9].replace("?&%$16527","\n").replace("\"","")
               solution = data[i+10].replace("?&%$16527","\n").replace("\"","")
               seeAlso = data[i+11].replace("?&%$16527","\n").replace("\"","")
               pluginOutput = data[i+12].replace("?&%$16527","\n").replace("\"","")

               issue_node = IssueNode(data_graph, risk, "", name="NessusIssue", descr=name,
                                      longdescr="CVE: " + CVE + "\n Description: " + descr, fixstr=solution)
               issue_node_id = tool_node.add_child(issue_node)
               data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
               data_graph.issue_dict[issue_node_id] = issue_node

           i+= 1


if __name__ == '__main__':
        with open ("/home/adrian/Documents/WS16/security/nessusPI.csv", "r") as myfile:
            data=myfile.read()
            data.replace("\n","?&%$16527")
            data.replace(",","\n")
        #encode newlines (in description strings), then split by the field separator and go through them
        #Plugin ID,CVE,CVSS,Risk,Host,Protocol,Port,Name,Synopsis,Description,Solution,See Also,Plugin Output
        datasplit = data.split("\n")
        for i in range(1,len(datasplit)-12):
           if i%13==0:
               pluginID = data[i].replace("?&%$16527","\n").replace("\"","")
               CVE = data[i+1].replace("?&%$16527","\n").replace("\"","")
               CVSS = data[i+2].replace("?&%$16527","\n").replace("\"","")
               risk = data[i+3].replace("?&%$16527","\n").replace("\"","")
               host = data[i+4].replace("?&%$16527","\n").replace("\"","")
               protocol = data[i+5].replace("?&%$16527","\n").replace("\"","")
               port = data[i+6].replace("?&%$16527","\n").replace("\"","")
               name = data[i+7].replace("?&%$16527","\n").replace("\"","")
               synopsis = data[i+8].replace("?&%$16527","\n").replace("\"","")
               descr = data[i+9].replace("?&%$16527","\n").replace("\"","")
               solution = data[i+10].replace("?&%$16527","\n").replace("\"","")
               seeAlso = data[i+11].replace("?&%$16527","\n").replace("\"","")
               pluginOutput = data[i+12].replace("?&%$16527","\n").replace("\"","")

           i+= 1