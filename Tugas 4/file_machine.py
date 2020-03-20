from file import Dire
import json
import logging
import base64
'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- upload : untuk mengupload file ke direktori
  request : upload
  parameter : namafile spasi isifile
  response : berhasil -> ok
             gagal -> error

- list : untuk melihat daftar dalam direktori
  request: list
  parameter: tidak ada
  response: daftar isi direktori file yang ada

- download : untuk mendownload file berdasarkan nama file
  request: download
  parameter: namafile yang ingin didownload
  response: memberikan unduhan file kepada client

- jika command tidak dikenali akan merespon dengan ERRCMD

'''

p = Dire()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                file = cstring[2].strip()

                print(nama)
                print(file.encode())
                print("Masuk Upload")
                p.upload_data(nama,file.encode())
                print("Selesai Upload")
                print(nama)
               # print(file)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                print("masuk list")
                hasil = p.list_data()
                print(hasil)
                return json.dumps(hasil)
            elif (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                print("masuk")
                hasil = p.download_data(nama)
                #print(hasil.decode())
               # hasil = hasil.decode
                return hasil[0]
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = PersonMachine()
    input = "pesan.txt"
    hasil = pm.proses("download pesan.txt")
    print("hasilnya")
    print(hasil)
    #hasil = pm.proses("list")
    #print(hasil)
    #hasil = pm.proses("get vanbasten")
    #print(hasil)