import pyshark
import sys
from dpi.models import TCPPacket

def main():
    #file_name = "smallFlows.pcap"
    if sys.argv[1]=="FileCapture":
        file_name = sys.argv[2]
        capture = pyshark.FileCapture(file_name)
    elif sys.argv[1]=="LiveCapture":
        capture = pyshark.LiveCapture(interface="ens33")
        capture.sniff(timeout=10)
    #if len(sys.argv) == 2:
        #file_name = sys.argv[1]
    #capture = pyshark.FileCapture(file_name)
    #capture = pyshark.LiveCapture(interface="ens33")
    #capture.sniff(timeout=10)
    num_http_request = 0
    for packet in capture:
        if "tcp" in packet:
            tcp = packet.tcp
            ip = packet.ip
            srcPort = int(tcp.srcPort)
            dstPort = int(tcp.dstPort)
            srcIP = ip.src
            dstIP = ip.dst
            stream_index = packet.tcp.stream
            print("Adding TCP packet ({srcIP}:{srcPort}) --> ({dstIP}:{dstPort})")
            TCPPacket.add(stream_index, srcPort, dstPort, srcIP, dstIP)

if __name__ == '__main__':
    main()
