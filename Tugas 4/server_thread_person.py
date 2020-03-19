from socket import *
import socket
import threading
import logging
import time
import sys
import base64
from person_machine import PersonMachine

pm = PersonMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        file = (b"")
        tes = []
        while True:
            #hilangkan semua dalam while untuk memakai fitur list dan download
            #uncomen ini
            # data = self.connection.recv(1024)
            while True:
                try:

                    data = self.connection.recv(1024)
                   #self.connection.sendall(data)
                    file = file + data
                    tes.append(data)
                    print(b"isi = " + data)
                except KeyboardInterrupt:
                    pass

                if not data: break

            #print(file)
            data = file
            if data:
                d = data.decode()
                print("Masuk Decode")
                hasil = pm.proses(d)
                hasil=hasil+"\r\n"
                print("retunrnya = " + hasil)
                self.connection.sendall(hasil.encode())

            else:
                break
        self.connection.close()



class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 8889))
        self.my_socket.listen(1)
        #self.my_socket.settimeout(100)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

