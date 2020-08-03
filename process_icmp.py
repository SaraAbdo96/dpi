import pyshark
import sys
from dpi.models import ICMPPacket
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
    for packet in capture:
        if "icmp" in packet:
            icmp = packet.icmp
            ip = packet.ip
            typee = icmp.type
            code = icmp.code
            checksum = icmp.checksum_status
            src_ip = ip.src
            dest_ip = ip.dst
            print("Adding ICMP packet")
            ICMPPacket.add(src_ip, dest_ip, typee, code, checksum)


if __name__ == '__main__':
    main()
