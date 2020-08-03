import pyshark
import sys
from collections import Counter
from dpi.models import TopTalkers


def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
    source = []
    destination = []
    for packet in capture:
        try:
            src_addr = packet.ip.src
            dst_addr = packet.ip.dst
            source.append(src_addr)
            destination.append(dst_addr)
        except AttributeError as e:
            print(str(e))
    top_5_src = Counter(source).most_common(5)
    top_5_dst = Counter(destination).most_common(5)
    #items = list(zip(top_5_src, top_5_dst))
    #for item in top_5_src:
        #try:
            #print("Adding top talkers")
            #TopTalkers.add(item)
        #except:
            #pass


if __name__ == '__main__':
    main()
