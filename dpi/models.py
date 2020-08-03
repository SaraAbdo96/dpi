from .app import db
class TopTalkers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src_ip = db.Column(db.String(15))
    dest_ip = db.Column(db.String(15))


    @classmethod
    def add(cls, src_ip, dest_ip):
        data = {
            "src_ip": src_ip,
            "dest_ip": dest_ip
        }
        top = cls(**data)
        db.session.add(top)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    @classmethod
    def get_top_talkers(cls, page=0, per_page=20):
        return cls.query.offset(page).limit(per_page).all()



class ICMPPacket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    src_ip = db.Column(db.String(15))
    dest_ip = db.Column(db.String(15))
    type = db.Column(db.Integer)
    code = db.Column(db.Integer)
    checksum_status = db.Column(db.Integer)

    @classmethod
    def add(cls, src_ip, dest_ip, typee, code, checksum_status):
        data = {
            "src_ip": src_ip,
            "dest_ip": dest_ip,
            "type": typee,
            "code": code,
            "checksum_status": checksum_status
        }
        icmp = cls(**data)
        db.session.add(icmp)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
    @classmethod
    def get_icmp(cls, page=0, per_page=20):
        return cls.query.offset(page).limit(per_page).all()

class UDPPacket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    srcPort = db.Column(db.Integer)
    dstPort = db.Column(db.Integer)
    srcIP = db.Column(db.String(15))
    dstIP = db.Column(db.String(15))
    @classmethod
    def add(cls, srcPort, dstPort, srcIP, dstIP):
        data = {
            "srcPort": srcPort,
            "dstPort": dstPort,
            "srcIP": srcIP,
            "dstIP": dstIP
        }
        udp = cls(**data)
        db.session.add(udp)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    @classmethod
    def get_udp(cls, page=0, per_page=20):
        return cls.query.offset(page).limit(per_page).all()


class TCPPacket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    stream_index = db.Column(db.Integer)
    srcPort = db.Column(db.Integer)
    dstPort = db.Column(db.Integer)
    srcIP = db.Column(db.String(15))
    dstIP = db.Column(db.String(15))

    @classmethod
    def add(cls,stream_index, srcPort, dstPort, srcIP, dstIP):
        data = {
            "stream_index" :stream_index,
            "srcPort": srcPort,
            "dstPort": dstPort,
            "srcIP": srcIP,
            "dstIP": dstIP
        }
        tcp = cls(**data)
        db.session.add(tcp)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    @classmethod
    def get_tcp(cls, page=0, per_page=20):
        return cls.query.offset(page).limit(per_page).all()

class HTTPrequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    host = db.Column(db.String(100))
    url = db.Column(db.String(1000))
    version = db.Column(db.String(10))
    response_code_desc = db.Column(db.String(100))
    response_code = db.Column(db.Integer)
    @classmethod
    def add(cls, method, host, url, version="HTTP/1.1",response_code_desc="OK", response_code="200"):
        data = {
            "method": method,
            "host": host,
            "url": url,
            "version": version,
            "response_code_desc": response_code_desc,
            "response_code": response_code
        }
        request = cls(**data)
        db.session.add(request)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise
    @classmethod
    def get_num(cls):
        return cls.query.count()
    @classmethod
    def get_requests(cls, page=0, per_page=20):
        return cls.query.offset(page).limit(per_page).all()
