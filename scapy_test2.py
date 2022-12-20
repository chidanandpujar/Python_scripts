from scapy.all import *
#packet test1
def test1():
    packet = IP()/TCP()/DNS() 
    packet[TCP].dport = 55
    packet.show()

#traceroute test2
def test2():
    res = traceroute(["target_ip"],maxttl=20)
    print(res)

#ARP ping
def test3():
    res = arping("target_ip")
    print(res)

#ICMP ping
def test4():
    ans, unans = sr(IP(dst="target_ip")/ICMP(), timeout=3)
    ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )

#UDP ping
def test5():
    ans, unans = sr(IP(dst="target_ip")/UDP(dport=0))
    ans.summary(lambda s,r: r.sprintf("%IP.src% is alive") )

#DNS request
def test6():
    ans = sr1(IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1,qd=DNSQR(qname="secdev.org",qtype="A")))
    print(ans.an.rdata)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
#    test5()
    test6()
