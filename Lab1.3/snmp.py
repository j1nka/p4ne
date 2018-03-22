from pysnmp.hlapi import *

snmp_object = ObjectIdentity("SNMPv2-MIB", "sysDescr",0)
snmp_object2 = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

for i in  getCmd(SnmpEngine(),CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)), ContextData(), ObjectType(snmp_object)):
    for j in i:
        if type(j) == type([]):
            for k in j:
                print(k)

for i in nextCmd(SnmpEngine(),CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)), ContextData(), ObjectType(snmp_object2), lexicographicMode=False):
    for j in i:
        if type(j) == type([]):
            for k in j:
                print(k)

'''result = nextCmd(SnmpEngine(),CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.107", 161)), ContextData(), ObjectType(snmp_object2), lexicographicMode=False)

for i in list(result):
    for j in i[3]:
        print(j)'''