#! /usr/bin/evn python3
import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP()
    arp_req.pdst = ip
    broadcast  = scapy.Ether()
    broadcast.dst= "ff:ff:ff:ff:ff:ff"
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast,timeout = 1,verbose = False)[0]
    print("\n\n___________________________________________")
    print("IP Address\t\t\tMAC Address")
    print("-------------------------------------------\n")
    
    for elements in answered_list:
        print(elements[1].psrc +"\t\t" + elements[1].hwsrc )    
    print("\n")
    
ip = input("Enter ip address : ")
scan(ip)
