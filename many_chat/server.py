import socket
import select
import sys
from _thread import *
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host=socket.gethostname()
port=8081
s.bind((host,port))
s.listen(5)
list= []
def cthread(conn, addr):
	conn.send(str.encode("Welcome to the chat"))
	while 1:
		try:
			message = conn.recv(2048)
			if message:
				print("<" + addr[0] + "> " + message)
				message2= "<" + addr[0] + "> " + message
				for clients in list:
					if clients!=conn:
						try:
							clients.send(message2)
						except:
							clients.close()
							if clients in list:
								list.remove(clients)
					else:
						if conn in list:
							list.remove(conn)
		except:
			continue
while True:
	conn, addr = s.accept()
	list.append(conn)
	print(addr[0] + " connected")
	start_new_thread(cthread,(conn,addr))    
conn.close()
server.close()