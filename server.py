                                # Sunucu programi
from socket import *
# soket parametlerini belirle
host = "192.168.1.3"
port = 7777
buf = 1024
addr = (host, port)
# soketi olustur ve adresle bindle
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
# mesajlari al
while 1:
	data, addr = UDPSock.recvfrom(buf)
	if not data:
		print "istemci ayrildi."
		break
	else:
		print "\nAlinan ileti : ", data
# soketi kapat
UDPSock.close()
