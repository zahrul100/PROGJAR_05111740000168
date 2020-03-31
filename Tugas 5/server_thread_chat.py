from socket import *
import socket
import threading
import time
import sys
import json
import logging
from chat import Chat

chatserver = Chat()

class ProcessTheClient(threading.Thread):
	def __init__(self, connection, address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		rcv=""
		while True:
			data = self.connection.recv(32) #menerima string dalam bentuk byte
			if data:
				d = data.decode() #menjadikan string
				rcv=rcv+d #menyambungkan string
				if rcv[-2:]=='\r\n': #jika baris terakhir mengandung \r\n
					#end of command, proses string
					logging.warning("data dari client: {}" . format(rcv)) #membuat log warning
					hasil = json.dumps(chatserver.proses(rcv)) #mendump dict menjadi json hasil proses dengan input yang diterima
					hasil=hasil+"\r\n\r\n"
					logging.warning("balas ke  client: {}" . format(hasil)) #log format balasan
					self.connection.sendall(hasil.encode()) #mengirim pesan tadi
					rcv="" #mengkosongkan rcv
			else:
				break
		self.connection.close()

class Server(threading.Thread):
	def __init__(self):
		self.the_clients = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('0.0.0.0',8889))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			logging.warning("connection from {}" . format(self.client_address))
			
			clt = ProcessTheClient(self.connection, self.client_address)
			clt.start()
			self.the_clients.append(clt)
	

def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()

