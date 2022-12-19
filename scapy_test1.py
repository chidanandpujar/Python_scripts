from scapy.all import *
packet = IP()/TCP()/DNS() 
packet[TCP].dport = 55
packet.show()
print(scapy.__file__)
