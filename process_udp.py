import pyshark
import sys
from dpi.models import UDPPacket

def main():
    #file_name = "smallFlows.pcap"
    if sys.argv[1]=="FileCapture":
        file_name = sys.argv[2]
        capture = pyshark.FileCapture(file_name)
    elif sys.argv[1]=="LiveCapture":
        capture = pyshark.LiveCapture(interface="ens33")
        capture.sniff(timeout=10)
    for packet in capture:
        if "udp" in packet:
            udp = packet.udp
            ip = packet.ip
            srcPort = int(udp.srcPort)
            dstPort = int(udp.dstPort)
            srcIP = ip.src
            dstIP = ip.dst
            print("Adding UDP packet ({srcIP}:{srcPort}) --> ({dstIP}:{dstPort})")
            UDPPacket.add(srcPort, dstPort, srcIP, dstIP)

if __name__ == '__main__':
    main()
