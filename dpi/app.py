from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

import math

app = Flask(__name__)
app.config.from_object("dpi.settings")

db = SQLAlchemy(app)

from .models import HTTPrequest, TCPPacket, UDPPacket, ICMPPacket, TopTalkers

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/http")
def http():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    num_requests = HTTPrequest.get_num()
    num_pages = math.ceil(num_requests / per_page) + 1
    pages = [x for x in range(1, num_pages+1)]
    requests = HTTPrequest.get_requests(page, per_page)
    max_page = len(pages) - 1
    return render_template("http.html", requests=requests, pages=pages, page=int(page), max_page=max_page)

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

@app.route("/TopTalkers")
def Top():
    page = request.args.get("page", 0)
    per_page = request.args.get("per_page", 20)
    return render_template("TopTalkers.html", TopTalkers = TopTalkers.get_top_talkers(page, per_page), page=int(page))
