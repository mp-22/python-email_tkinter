import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
	data=raw_input()
	if data == 'exit' or not data:
		break
	s.sendto(data,('127.0.0.1',9999))
	print s.recv(1024)
s.close()