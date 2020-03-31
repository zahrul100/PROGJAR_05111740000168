import socket
import os
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP,TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid="" #token id awalnya kosong
    def proses(self,cmdline):
        j=cmdline.split(" ") #memisahakn antar spasi
        try:
            command=j[0].strip() #melihat command pertama
            if (command=='auth'): #jika auth
                username=j[1].strip() #menyimpan username
                password=j[2].strip() #menyimpan password
                return self.login(username,password) #jalankan fungsi login
            elif (command=='send'): #jika send
                usernameto = j[1].strip() #menyimpan alamat username tujuan
                message=""
                for w in j[2:]:
                   message="{} {}" . format(message,w) #menyambung pesan
                return self.sendmessage(usernameto,message) #memanggil fungsi mengirim pesan
            elif (command=='inbox'): #jika inbox
                return self.inbox()
            elif (command=='listuser'): #jika list user
                return self.listuser()
            elif (command=="logout"):
                if(self.tokenid ==""):
                    return "ERROR,Anda belum login"
                self.tokenid=""
                return "logout berhasil"
            else:
                return "*Maaf, command tidak benar"
        except IndexError:
                return "-Maaf, command tidak benar"
    def sendstring(self,string): #fungsi mengirim string ke server
        try:
            self.sock.sendall(string.encode()) #mengirim string
            receivemsg = "" #untuk nanti menerima respon server
            while True:
                data = self.sock.recv(64) #menerima data dari server
#                print("diterima dari server",data) #mengprint data yang diterima dari server per besar bit
                if (data):
                    receivemsg = "{}{}" . format(receivemsg,data.decode())  #data harus didecode agar dapat di operasikan dalam bentuk string
                    if receivemsg[-4:]=='\r\n\r\n':
#                        print("end of string")
                        return json.loads(receivemsg) #mereturn pesan dalam format json
        except:
            self.sock.close()
            return { 'status' : 'ERROR', 'message' : 'Gagal'}
    def login(self,username,password): #fungsi login
        string="auth {} {} \r\n" . format(username,password) #menyimpan string "auth username password"
        result = self.sendstring(string) #menjalankan fungsi sendstring dan menerima dalam bentuk json
        if result['status']=='OK': #melihat json jika status yang diterima ok
            self.tokenid=result['tokenid'] #menyimpan tokenid
            return "username {} logged in, token {} " .format(username,self.tokenid) #mereturn hasilnya
        else:
            return "Error, {}" . format(result['message'])
    def sendmessage(self,usernameto="xxx",message="xxx"): #fungsi send message
        if (self.tokenid==""): #jika tidak ada token id
            return "Error, not authorized"
        string="send {} {} {} \r\n" . format(self.tokenid,usernameto,message) #menjadikan string menjadi 1
      #  print(string)
        result = self.sendstring(string) #mengirim string ke server dan menerima responnya
        if result['status']=='OK':
            return "message sent to {}" . format(usernameto)
        else:
            return "Error, {}" . format(result['message'])
    def inbox(self):
        if (self.tokenid==""):
            return "Error, not authorized"
        string="inbox {} \r\n" . format(self.tokenid)
        result = self.sendstring(string)
        if result['status']=='OK':
            return "{}" . format(json.dumps(result['messages']))
        else:
            return "Error, {}" . format(result['message'])

    def listuser(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "listuser {} \r\n".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "{}".format(json.dumps(result['listuser']))
        else:
            return "Error, {}".format(result['message'])

if __name__=="__main__":
    cc = ChatClient()
    while True:
        cmdline = input("Command {}:" . format(cc.tokenid)) #memasukkan command dan menyambung dengan token id jika sudah login
      #  print(cmdline)
        print(cc.proses(cmdline)) #mencetak hasil proses

