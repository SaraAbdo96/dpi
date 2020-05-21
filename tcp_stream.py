import pyshark
import sys
from dpi.models import TCPStream

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    cap = pyshark.FileCapture(file_name, display_filter='tcp')
    stream_indexes = []
    for pkt in cap:
        try:
            stream_indexes.append(pkt.tcp.stream)
        except:
            pass
    stream_indexes = list(dict.fromkeys(stream_indexes))
    #stream_index.sort()
    print(stream_indexes)
    for stream_index in stream_indexes:
        pcap = pyshark.FileCapture(file_name, display_filter='tcp.stream eq %s' % stream_index)
        print("Stream Index: " + str(stream_index))
        while True:
            try:
                p = pcap.next()
            except StopIteration:
                break
            try:
                value = p.tcp.payload.binary_value
                print(value)
            except AttributeError:
                pass
        #TCPStream.add(stream_index, value)

if __name__ == '__main__':
    main()