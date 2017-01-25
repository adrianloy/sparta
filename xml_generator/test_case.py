import xml_generator.xml_schema.binding as bin

issue = bin.issue()
issue.text = "test"

port = bin.port()
port.issue = [issue, issue, issue, issue]

with open('output.xml', 'w') as f:
    f.write(port.toxml("utf-8"))
