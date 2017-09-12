import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='LocalHost'

port=5300
print("RSA Client Side \n")
p=int(input("Enter p(prime number) "))

q=int(input("Enter q(prime number) "))
n=p*q
print("First part of public key is %d"%n)
a=(p-1)*(q-1)
print("Euler Totient function is %d\n"%a)
e=int(input("Enter exponent e value such that 1<e<TF and is coprime: "))
print("Public key is n=%d , e=%d\n"%(n,e))
s.connect((host, port))
s.sendall(str.encode("\n".join([str(n), str(e)])))
m=int((s.recv(2048)).decode('utf-8'))
print("Recieved encrypted message is %d"%m)
s.close()

