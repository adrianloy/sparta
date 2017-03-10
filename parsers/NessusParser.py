#!/usr/bin/python

from datagraph.node import *
import re

'''this module is used to parse a Nessus csv report'''
__author__ = 'adrian'


class NessusParser(object):

    @staticmethod
    def create_issue_nodes(tool_node):
        data_graph = tool_node.data_graph

        #if tool_node.file_output == '':
        #    print 'tool file output is empty'
        #    return


        output_file = tool_node.outputfile +".csv"
        with open (output_file, "r") as myfile:
            data=myfile.read()
        data = data[102::] #skip first line
        datasplit = data.split("\"\r\n\"") #one entry is one vulnerability
        for entry in datasplit:
            fields = entry.split("\",\"")
            pluginID = fields[0].replace("\"","")
            CVE = fields[1].replace("\"","")
            CVSS = fields[2].replace("\"","")
            risk = fields[3].replace("\"","")
            host = fields[4].replace("\"","")
            protocol = fields[5].replace("\"","")
            port = fields[6].replace("\"","")
            name = fields[7].replace("\"","")
            synopsis = fields[8].replace("\"","")
            descr = fields[9].replace("\"","")
            solution = fields[10].replace("\"","")
            seeAlso = fields[11].replace("\"","")
            pluginOutput = fields[12].replace("\"","")

            issue_node = IssueNode(data_graph, risk, "", name="NessusIssue", descr=name,
                              longdescr="CVE: " + CVE + "\n Description: " + descr + "\n Result: " + pluginOutput,
                              fixstr=solution)
            issue_node_id = tool_node.add_child(issue_node)
            data_graph.view.ui.addNodeTo(tool_node.node_id, issue_node_id, name, "issues")
            data_graph.issue_dict[issue_node_id] = issue_node


if __name__ == '__main__':
        with open ("/home/adrian/Documents/WS16/security/nessusPI.csv", "r") as myfile:
            data=myfile.read()
        #encode newlines (in description strings), then split by the field separator and go through them
        #Plugin ID,CVE,CVSS,Risk,Host,Protocol,Port,Name,Synopsis,Description,Solution,See Also,Plugin Output
        data = data[102::] #skip first line
        datasplit = data.split("\"\r\n\"") #one entry is now one vulnerability
        for entry in datasplit:
            fields = entry.split("\",\"")
            pluginID = fields[0].replace("\"","")
            CVE = fields[1].replace("\"","")
            CVSS = fields[2].replace("\"","")
            risk = fields[3].replace("\"","")
            host = fields[4].replace("\"","")
            protocol = fields[5].replace("\"","")
            port = fields[6].replace("\"","")
            name = fields[7].replace("\"","")
            synopsis = fields[8].replace("\"","")
            descr = fields[9].replace("\"","")
            solution = fields[10].replace("\"","")
            seeAlso = fields[11].replace("\"","")
            pluginOutput = fields[12].replace("\"","")