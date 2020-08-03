import pyshark
import sys
from dpi.models import HTTPrequest


def main():
   #file_name = "smallFlows.pcap"
    #if len(sys.argv) == 2:
        #file_name = sys.argv[1]
    if sys.argv[1] == "FileCapture":
       file_name = sys.argv[2]
       capture = pyshark.FileCapture(file_name)
    elif sys.argv[1] == "LiveCapture":
       capture = pyshark.LiveCapture(interface="lo")
       capture.sniff(timeout=10)
    num_http_request = 0
    num_http_response = 0
    res=""
    ress=""
    for packet in capture:
        try:
            protocol = packet.transport_layer
            if protocol == "TCP":
                dst_port = int(packet.tcp.dstport)
                src_port = int(packet.tcp.srcport)
                if dst_port == 5000:
                    num_http_request += 1
                    http = packet.http
                    method = http.request_method
                    host = http.host
                    uri = http.request_full_uri
                    version = http.request_version
                if src_port == 5000:
                    num_http_response += 1
                    http = packet.http
                    res = http.response_code_desc
                    ress = http.response_code
                    HTTPrequest.add(method, host, uri, version, res, ress)
        except AttributeError as e:
            print(str(e))


if __name__ == '__main__':
    main()

