import shelve
import uuid
import socket
import os
import base64

class Dire:
    def __init__(self):
      #  self.data = shelve.open('mydata.dat')
        if not os.path.exists("direktori"):
            os.makedirs("direktori")
    def upload_data(self,nama=None,file=None):
       #====check nama direktori=======
        #print("masuk sini "+file)
        makan = file
        print("halo")
        print(base64.decodestring(makan))
        f = open("direktori/"+nama,"wb")
        f.write(base64.decodestring(makan))
        print("asd")
        #print("sudah masuk pesaanya adalah "+file.encode()+" Nama FIlenya"+nama)
       #print("endo"+base64.decodestring(file))
     #   print("inibro "+file)

       # file = base64.decodestring(file.encode())
       #print("filenya"+file)
        #print(f.read())
        #l = f.read()
        #f.close()
       #======Membuat file serupa =====
        #f = open("direktori/"+nama,"wb")
        #f.write(l)
        #f.close()
       # self.data[id]=data
        return True
    def download_data(self,nama=None):
        # ======Membaca file download =====
        are = []
        f = open("direktori/" + nama, "rb")
        l =f.read()
        f.close()
        print(l)
        # ======Mendownload file =====
       #f = open("download"+nama,"wb")
       #f.write(l)
       #f.close()
        hasil = base64.encodestring(l)
        print(hasil)
        are.append(hasil.decode())
        print(are)
 #       print("bisakah")
        return are

    def list_data(self):
        file_list = os.listdir("direktori")
        f = []
        for filename in file_list:
            f.append(filename)
        return f
           #with open(os.path.join('direktori',filename),"r") as src_file:
           #     yield src_file.read()

if __name__=='__main__':
    dire = Dire()
    input = "pesan.txt"
    ini = dire.download_data(input)
    print(ini)
   # dire.upload_data("gambartugas.jpg")
    #dire.download_data("gambartugas.jpg")
    print(dire.list_data())
    #print(tes)
   # p.create_data("vanPersie","621235")
   # p.create_data("vanNistelroy","621236")
   # p.create_data("vanDerVaart","621237")
   # print(dire.list_data())
   # print(dire.get_data('vanbasten'))
