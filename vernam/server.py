import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(5)
while True:
	b,address=s.accept()
	print("Connection Success from ",address)
	em=(b.recv(2048)).decode('utf-8')
	print("encrypted message is %s"%em)
	key=""
	while (len(key)!=len(em)):
		key=input("\nenter the Key : ")
		if (len(em)!=len(key)):
			print("\nlength of key is not equal to message")
	dm=""
	for i in range(len(em)):
		a=(ord(em[i])-ord(key[i]))%128
		dm=dm+chr(a)
	print("\ndecrypted message is %s"%dm)
	b.close()
s.close
s.close