import socket as sck
import sys

class Socket:
	def __init__(self,IP,PORT):
		self.IP = IP
		self.PORT = PORT


	def __enter__(self):
		self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
		self.socket.setsockopt(sck.SOL_SOCKET, sck.SO_REUSEADDR, 1)
		return self

	def __exit__(self,*args):
		self.socket.close()

	def Server(self):
		print("Starting socket at: " + self.IP + ':' + str(self.PORT))
		self.socket.bind((self.IP,self.PORT))
		self.socket.listen()
		self.conn,self.addr = self.socket.accept()
		print("Successful")

	def Client(self):
		print("Connecting to: " + self.IP + ':' + str(self.PORT))
		while True:
			try:
				self.socket.connect((self.IP,self.PORT))
				break
			except:
				pass
		print("Connected")

###########################################################################
	def CData(self,msg=''):
		self.socket.sendall(str.encode(str(msg)))
		data = self.socket.recv(1024)
		return data
###########################################################################
	def SData(self,conn,msg='Success'):
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(str.encode(str(msg)))
			return data
		return b''
