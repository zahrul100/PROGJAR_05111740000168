import socket
import sys
import base64
import os
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)


requestfile = "gambartugas.jpg"
request = (b"download "+requestfile.encode())
print(request)
f = open(requestfile,"wb")
file =(b"")
sock.send(request)
data = sock.recv(1024)
while True:
    file = file + data
   # print(file)
    #data = sock.recv(1024)
    #print(sys.getsizeof(data))
    if sys.getsizeof(data) != 1057:
        print(sys.getsizeof(data))
        break
    else :
        data = sock.recv(1024)


print(file)
#file = base64.decodestring(file)
#file = file.decode()
file = base64.decodestring(file)

f.write(file)
f.close()
f = open("direktori/gambar.jpg","rb")
print(f.read())
#print(base64.decode(data))
f.close()

sock.close()
