from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object("dpi.settings")

db = SQLAlchemy(app)

from .models import HTTPrequest, TCPPacket, UDPPacket, ICMPPacket, TCPStream, TopTalkers

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/http")
def http():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("http.html", requests = HTTPrequest.get_requests(page, per_page), page=int(page))

@app.route("/tcps")
def tcp():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("tcp.html", tcps = TCPPacket.get_tcp(page, per_page), page=int(page))

@app.route("/udps")
def udp():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("udp.html", udps = UDPPacket.get_udp(page, per_page), page=int(page))

@app.route("/icmps")
def icmp():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("icmp.html", icmps = ICMPPacket.get_icmp(page, per_page), page=int(page))

@app.route("/tcpstream")
def tcp_stream():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("tcp_stream.html", tcp_streams = TCPStream.get_tcp_stream(page, per_page), page=int(page))
