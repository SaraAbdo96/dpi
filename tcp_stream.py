import pyshark
import sys

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    cap = pyshark.FileCapture(file_name)
    stream_index = []
    for pkt in cap:
        try:
            stream_index.append(pkt.tcp.stream)
        except:
            pass
    stream_index = list(dict.fromkeys(stream_index))
    print(stream_index)
    for item in stream_index:
        pcap = pyshark.FileCapture(file_name, display_filter='tcp.stream eq %s' % item)
        print("Stream Index: " + str(item))
        while True:
            try:
                p = pcap.next()
            except StopIteration:
                break
            try:
                value = p.tcp.payload.binary_value
                if len(value)==0:
                    print("No TCP Stream")
                else:
                    print(value)
            except AttributeError:
                pass


if __name__ == '__main__':
    main()