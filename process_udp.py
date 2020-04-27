import pyshark
import sys
from dpi.models import UDPPacket

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
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
