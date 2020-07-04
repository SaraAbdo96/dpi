PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tcp_packet (
	id INTEGER NOT NULL, 
	stream_index INTEGER, 
	"srcPort" INTEGER, 
	"dstPort" INTEGER, 
	"srcIP" VARCHAR(15), 
	"dstIP" VARCHAR(15), 
	PRIMARY KEY (id)
);
CREATE TABLE tcp_stream (
	id INTEGER NOT NULL, 
	stream_index INTEGER, 
	value VARCHAR(1000), 
	PRIMARY KEY (id)
);
CREATE TABLE udp_packet (
	id INTEGER NOT NULL, 
	"srcPort" INTEGER, 
	"dstPort" INTEGER, 
	"srcIP" VARCHAR(15), 
	"dstIP" VARCHAR(15), 
	PRIMARY KEY (id)
);
CREATE TABLE icmp_packet (
	id INTEGER NOT NULL, 
	type INTEGER, 
	code INTEGER, 
	checksum_status INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE htt_prequest (
	id INTEGER NOT NULL, 
	method VARCHAR(10), 
	host VARCHAR(10), 
	url VARCHAR(1000), 
	version VARCHAR(10), 
	response_code_desc VARCHAR(100), 
	response_code VARCHAR(100), 
	PRIMARY KEY (id)
);
INSERT INTO "htt_prequest" VALUES(1,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(2,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(3,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(4,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(5,'POST','ocsp.digicert.com','http://ocsp.digicert.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(6,'POST','ocsp.digicert.com','http://ocsp.digicert.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(7,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(8,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(9,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(10,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(11,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(12,'POST','ocsp.digicert.com','http://ocsp.digicert.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(13,'POST','ocsp.int-x3.letsencrypt.org','http://ocsp.int-x3.letsencrypt.org/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(14,'POST','ocsp.int-x3.letsencrypt.org','http://ocsp.int-x3.letsencrypt.org/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(15,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(16,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(17,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(18,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt?ipv4','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(19,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(20,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(21,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(22,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(23,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(24,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(25,'POST','ocsp.sca1b.amazontrust.com','http://ocsp.sca1b.amazontrust.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(26,'POST','ocsp.sca1b.amazontrust.com','http://ocsp.sca1b.amazontrust.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(27,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(28,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt?ipv4','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(29,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt?ipv4','HTTP/1.1','Bad Request','400');
INSERT INTO "htt_prequest" VALUES(30,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(31,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(32,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(33,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(34,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(35,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(36,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(37,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(38,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(39,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(40,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(41,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(42,'POST','ocsp.digicert.com','http://ocsp.digicert.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(43,'POST','ocsp.digicert.com','http://ocsp.digicert.com/','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(44,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(45,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(46,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(47,'GET','detectportal.firefox.com','http://detectportal.firefox.com/success.txt?ipv4','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(48,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(49,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(50,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(51,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(52,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
INSERT INTO "htt_prequest" VALUES(53,'POST','ocsp.pki.goog','http://ocsp.pki.goog/gts1o1core','HTTP/1.1','OK','200');
COMMIT;
