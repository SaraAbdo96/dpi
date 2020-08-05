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

def get_pages(page, per_page, x):
    num = x.get_num()
    num_pages = math.ceil(num / per_page) + 1
    pages = [x for x in range(1, num_pages+1)]
    xs = x.get(page, per_page)
    max_page = len(pages) - 1
    if max_page > 10:
        if page > 5:
            first_5 = pages[page-5:page]
        else:
            first_5 = pages[0:5]
        if page > max_page - 5:
            last_5 = pages[-1:-5:-1]
            last_5.reverse()
        else:
            last_5 = pages[page: page+5]
        pages = first_5 + ['.', '.', '.'] + last_5
    return (xs, pages, max_page)

@app.route("/http")
def http():
    page = int(request.args.get("page", 0))
    per_page = int(request.args.get("per_page", 20))
    (requests, pages, max_page) = get_pages(page, per_page, HTTPrequest)
    return render_template("http.html", requests=requests, pages=pages, page=page, max_page=max_page)

@app.route("/tcps")
def tcp():
    page = int(request.args.get("page", 0))
    per_page = int(request.args.get("per_page", 20))
    (tcps, pages, max_page) = get_pages(page, per_page, TCPPacket)
    return render_template("tcp.html", tcps = tcps, page=page, max_page=max_page, pages=pages)

@app.route("/udps")
def udp():
    page = int(request.args.get("page", 0))
    per_page = int(request.args.get("per_page", 20))
    (udps, pages, max_page) = get_pages(page, per_page, UDPPacket)
    return render_template("udp.html", udps = udps, page=page, pages=pages, max_page=max_page)

@app.route("/icmps")
def icmp():
    page = int(request.args.get("page", 0))
    per_page = int(request.args.get("per_page", 20))
    (icmps, pages, max_page) = get_pages(page, per_page, ICMPPacket)
    return render_template("icmp.html", icmps = icmps, page=page, pages=pages, max_page=max_page)

@app.route("/TopTalkers")
def Top():
    page = int(request.args.get("page", 0))
    per_page = int(request.args.get("per_page", 20))
    (top, pages, max_page) = get_pages(page, per_page, TopTalkers)
    return render_template("TopTalkers.html", top = top, page=page, pages=pages, max_page=max_page)
