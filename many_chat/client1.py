import socket
import select
import sys
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
port=8081
s.connect((host,port))
while 1:
	sockets_list = [sys.stdin,s]
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
	for socks in read_sockets:
		if socks ==s:
			message = socks.recv(2048).decode('utf-8')
			print(message)
		else:
			message = sys.stdin.readline()
			s.send(message)
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()
s.close()


