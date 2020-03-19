import socket
import sys
import base64
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)
pesan = ("upload gambar.jpg")

namafile = "".join(pesan.split() [1])


f = open(namafile, "rb")
panjang = len(namafile)+1
isifile = base64.encodestring(f.read())
f.close()
f = open("base64encode","wb")
f.write(isifile)
f.close

f = open("base64encode","rb")

l = pesan.encode()+(b" ")+f.read(1024-panjang)
#semua = f.read()
#print(base64.encodestring(semua))
print(l)
#print(f.read())
#print(l)
while (l):
 #   print(l)
    sock.send(l)
    l =f.read(1024)

#sock.recv(1024)
sock.close()