import xml_generator.xml_schema.binding as bin
import datetime

issue1 = bin.issue()
issue1.tool = "w3af"
issue1.text = "test1"

issue2 = bin.issue()
issue2.tool = "nmap"
issue2.text = "test2"

port1 = bin.port()
port1.issue = [issue1]
port1.port = 1337

port2 = bin.port()
port2.issue = [issue2]
port2.port = 42

host = bin.host()
host.ip = "192.168.56.3"
host.port = [port1, port2]

scan = bin.scan()
scan.dateTime = datetime.datetime.now()
scan.host = [host]

xml = scan.toDOM(None).toprettyxml(indent="  ")

with open('output.xml', 'w') as f:
    f.write(xml)
