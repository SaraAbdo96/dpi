import pyshark
import sys 
from dpi.models import ICMPPacket

def main():
   #file_name = "smallFlows.pcap"
   #if len(sys.argv) == 2:
        #file_name = sys.argv[1]
   #capture = pyshark.FileCapture(file_name)
   capture = pyshark.LiveCapture(interface="ens33")
   capture.sniff(timeout=10)
   for packet in capture:
       if "icmp" in packet:
           icmp = packet.icmp
           typee = icmp.type
           code = icmp.code
           checksum = icmp.checksum_status
           print("Adding ICMP packet")
           ICMPPacket.add(typee, code, checksum)


if __name__ == '__main__':
    main()
