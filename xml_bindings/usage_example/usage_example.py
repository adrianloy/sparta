import xml_schema.binding as bind
import datetime

issue1 = bind.issue()
issue1.tool = "w3af"
issue1.text = "test1"

issue2 = bind.issue()
issue2.tool = "nmap"
issue2.text = "test2"

port1 = bind.port()
port1.issue = [issue1]
port1.port = 1337

port2 = bind.port()
port2.issue = [issue2]
port2.port = 42

host = bind.host()
host.ip = "192.168.56.3"
host.port = [port1, port2]

scan = bind.scan()
scan.dateTime = datetime.datetime.now()
scan.host = [host]

xml = scan.toDOM(None).toprettyxml(indent="  ")

with open('output.xml', 'w') as f:
    f.write(xml)
