import sys
import os
import json
import uuid
import logging
from queue import  Queue

class Chat:
	def __init__(self):
		self.sessions={}
		self.users = {}
		self.users['messi']={ 'nama': 'Lionel Messi', 'negara': 'Argentina', 'password': 'surabaya', 'incoming' : {}, 'outgoing': {}}
		self.users['henderson']={ 'nama': 'Jordan Henderson', 'negara': 'Inggris', 'password': 'surabaya', 'incoming': {}, 'outgoing': {}}
		self.users['lineker']={ 'nama': 'Gary Lineker', 'negara': 'Inggris', 'password': 'surabaya','incoming': {}, 'outgoing':{}}
	def proses(self,data):
		j=data.split(" ") #meng split inpitan
		try:
			command=j[0].strip() #mencari command pertama
			if (command=='auth'): #jika string pertama auth
				username=j[1].strip() #cocokan username
				password=j[2].strip() #cocokkan password
				logging.warning("AUTH: auth {} {}" . format(username,password)) #membuat log, Note : format dalam python sama seperti %s,%d,dll pada cpp
				return self.autentikasi_user(username,password) #memanggil fungsi autentikasi user dan mereturn
			elif (command=='send'): #jika perintahnya adalah send
				sessionid = j[1].strip() #cek sessionnya
				usernameto = j[2].strip() #cek username tujuan
				message=""
				for w in j[3:]: #menyambung pesan
					message="{} {}" . format(message,w)
				usernamefrom = self.sessions[sessionid]['username'] #menyimpan username pengirim berdasar tokenid
				logging.warning("SEND: session {} send message from {} to {}" . format(sessionid, usernamefrom,usernameto))
				return self.send_message(sessionid,usernamefrom,usernameto,message) #jalankan fungsi mengirim message
			elif (command=='inbox'):
				sessionid = j[1].strip()
				username = self.sessions[sessionid]['username']
				logging.warning("INBOX: {}" . format(sessionid))
				return self.get_inbox(username)
			elif (command=='listuser'):
				sessionid = j[1].strip()

				return self.get_listuser()
			else:
				return {'status': 'ERROR', 'message': '**Protocol Tidak Benar'}
		except KeyError:
			return { 'status': 'ERROR', 'message' : 'Informasi tidak ditemukan'}
		except IndexError:
			return {'status': 'ERROR', 'message': '--Protocol Tidak Benar'}
	def autentikasi_user(self,username,password): #fungsi untuk meng autentikasi user
		if (username not in self.users): #jika username salah
			return { 'status': 'ERROR', 'message': 'User Tidak Ada' }
		if (self.users[username]['password']!= password): #jika password salah
			return { 'status': 'ERROR', 'message': 'Password Salah' }
		tokenid = str(uuid.uuid4()) #jika cocok maka membuat uuid
		self.sessions[tokenid]={ 'username': username, 'userdetail':self.users[username]} #membuat session sesuai tokenid dan meingisi sesuai username dan ada userdetail nya
		return { 'status': 'OK', 'tokenid': tokenid } #mereturn dengan format dict
	def get_user(self,username):
		if (username not in self.users):
			return False
		return self.users[username]
	def send_message(self,sessionid,username_from,username_dest,message):
		if (sessionid not in self.sessions): #jika sessions nya tidak ada
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}
		s_fr = self.get_user(username_from) #mencococokkan username jika ada
		s_to = self.get_user(username_dest) #mencocokan username tujuan jika ada
		
		if (s_fr==False or s_to==False): #jika ada yang tidak ditemukan
			return {'status': 'ERROR', 'message': 'User Tidak Ditemukan'}

		message = { 'msg_from': s_fr['nama'], 'msg_to': s_to['nama'], 'msg': message } #menyimpan secara format message
		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']
		try:	
			outqueue_sender[username_from].put(message) #menulis pesan terkirim didalam inbox
		except KeyError:
			outqueue_sender[username_from]=Queue()
			outqueue_sender[username_from].put(message)
		try:
			inqueue_receiver[username_from].put(message) #menyimpan pesan diterima didalam inbox
		except KeyError:
			inqueue_receiver[username_from]=Queue()
			inqueue_receiver[username_from].put(message)
		return {'status': 'OK', 'message': 'Message Sent'}

	def get_inbox(self, username):
		s_fr = self.get_user(username)  # menyimpan username
		incoming = s_fr['incoming']  # menyimpan pesan diterima berdasarkan username
		msgs = {}
		for users in incoming:
			msgs[users] = []
			while not incoming[users].empty():  # selama tidak kosong
				msgs[users].append(s_fr['incoming'][users].get_nowait())

		return {'status': 'OK', 'messages': msgs}

	def get_listuser(self):
		listuser = {'listuser':{}}

		return {'status': 'OK','listuser': list(self.users.keys()) }

if __name__=="__main__":
	j = Chat()
	i=0
#	print(j.users)
	print(j.get_listuser())
	#user = {'listuser':list(j.users.keys())}
	#print(user)
	#print(j.users)
#	sesi = j.proses("auth messi surabaya")
#	print(sesi)
	#sesi = j.autentikasi_user('messi','surabaya')
	#print sesi
##	tokenid = sesi['tokenid']
#	print(j.proses("send {} henderson hello gimana kabarnya son " . format(tokenid)))
#	print(j.proses("send {} messi hello gimana kabarnya mess " . format(tokenid)))

	#print j.send_message(tokenid,'messi','henderson','hello son')
	#print j.send_message(tokenid,'henderson','messi','hello si')
	#print j.send_message(tokenid,'lineker','messi','hello si dari lineker')


#	print("isi mailbox dari messi")
#	print(j.get_inbox('messi'))
#	print("isi mailbox dari henderson")
#	print(j.get_inbox('henderson'))
















