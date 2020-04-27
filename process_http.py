import pyshark
import sys
from dpi.models import HTTPrequest

def main():
    file_name = "smallFlows.pcap"
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    capture = pyshark.FileCapture(file_name)
    num_http_request = 0
    num_http_response = 0 
    for packet in capture:
        protocol = packet.transport_layer
        if protocol == "TCP":
            dst_port = int(packet.tcp.dstport)
            src_port = int(packet.tcp.srcport)
            if dst_port == 80:
               #num_http_request += 1
                http = packet.http
                method = http.request_method
                host = http.host
                uri = http.request_full_uri
                version = http.request_version
            if src_port == 80:
                num_http_response += 1
                http = packet.http
                response =http.response_code_desc
        HTTPrequest.add(method, host, uri, version, response)

if __name__ == '__main__':
    main()
