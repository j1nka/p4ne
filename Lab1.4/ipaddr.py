import random
import ipaddress

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        ipaddress.IPv4Network.__init__(self, (random.randint(0x0B000000, 0xDF000000), random.randint(8,24)), strict=False)
    def key_value(self):
        return [int(self.netmask), int(self.network_address._ip)]

ddos_nets = []
for i in range(50):
    ddos_nets.append(IPv4RandomNetwork())

for i in sorted(ddos_nets, key=IPv4RandomNetwork.key_value): print(i)