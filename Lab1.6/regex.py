import ipaddress
import re

def parseme(data):
    if re.match("(interface)", data):
       iDict.append({"int":d.split(" ")[1]})
    m = re.match("(ip address) ((?:[0-9]{1,3}[\.]){1,3}[0-9]{1,3}) ((?:[0-9]{1,3}[\.]){3}[0-9]{1,3})", data.lower())
    if m:
        iDict.append({"ip":ipaddress.IPv4Interface(m.group(2)+"/"+m.group(3))})
    if re.match("(hostname)", data):
        hDict.append({"host": d.split(" ")[1]})

data = [line.strip() for line in open('k2-sat1-asw1_10.12.230.90.txt')]

aDict = []
iDict = []
hDict = []

for d in data:
    parseme(d)

print(iDict, hDict, iDict)
