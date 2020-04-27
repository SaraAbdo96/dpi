import pyshark
import sys 
from dpi.models import ICMPPacket

def main():
   file_name = "smallFlows.pcap"
   if len(sys.argv) == 2:
        file_name = sys.argv[1]
   capture = pyshark.FileCapture(file_name)
   for packet in capture:
       if "icmp" in packet:
           icmp = packet.icmp
           type = icmp.type
           code = icmp.code
           checksum = icmp.checksum_status
           ICMPPacket.add(type, code, checksum)


if __name__ == '__main__':
    main()
