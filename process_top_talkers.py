import pyshark
import sys
from collections import Counter
from dpi.models import TopTalkers

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
    source=[]
    destination=[]
    for packet in capture:
        src_addr = packet.ip.src
        dst_addr = packet.ip.dst
        source.append(src_addr)
        destination.append(dst_addr)
        
    top_5_src = Counter(source).most_common(5)
    top_5_dst = Counter(destination).most_common(5)

    TopTalkers.add(top_5_src, top_5_dst)



if __name__ == '__main__':
    main()