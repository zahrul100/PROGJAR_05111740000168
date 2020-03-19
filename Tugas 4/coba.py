import base64

f=open("gambar.jpg","rb")
data = f.read()

print(data)
data = f.read(4)
print(data)
data = f.read(4)
print(data)
#print(base64.encodestring(data))