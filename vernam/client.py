import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
print ("\nVERNAM CIPHER")
mes=input("\nenter your message: ")
key = ""
while(len(mes)!=len(key)):
	key = input("\nenter the Key : ")
	if len(mes)!=len(key):
		print("\nlength of key is not equal to message")
em=""
for i in range(len(mes)):
	a=(ord(mes[i])+ord(key[i]))%128
	em=em+chr(a)
print("\nencypted message is  %s"%em)
s.connect((host, port))
s.send(str.encode(em))
s.close