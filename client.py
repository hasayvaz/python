                                    # istemci programi
from socket import *
# soket parametlerini belirle
host = "192.168.1.3"
port = 7777
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)          # soket olustur

print "gondermek istediginiz iletinizi yazin\n"
# iletileri gonderme kismi
while (1):
	data = raw_input('>>> ')
	if not data:
		break
	else:
		if(UDPSock.sendto(data, addr)):
			print "gonderilen ileti : ", data
# soketi kapat
UDPSock.close()
