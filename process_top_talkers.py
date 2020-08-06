import pyshark
import sys
from dpi.models import TopTalkers

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
    source = []
    destination = []
    counter1 = {}
    counter2 = {}
    for packet in capture:
        try:
            src_addr = packet.ip.src
            dst_addr = packet.ip.dst
            source.append(src_addr)
            destination.append(dst_addr)
        except AttributeError as e:
            print(str(e))
    for i in source:
        if i in counter1:
            counter1[i] += 1
        else:
            counter1[i] = 1
    for j in destination:
        if j in counter2:
            counter2[j] += 1
        else:
            counter2[j] = 1
    pop1 = sorted(counter1, key=counter1.get, reverse=True)
    pop2 = sorted(counter2, key=counter2.get, reverse=True)
    top_5_src = pop1[:5]
    top_5_dst = pop2[:5]
    zip_object = zip(top_5_src, top_5_dst)
    for i1, i2 in zip_object:
        print("Adding Top Talkers")
        TopTalkers.add(i1, i2)

if __name__ == '__main__':
    main()
