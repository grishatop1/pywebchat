import eel
import threading
import random
from client import Client

@eel.expose
def createConnection(data):
	return api.createConnection(data)

@eel.expose
def sendMessage(content):
	api.sendMessage(content)

@eel.expose
def dropConnection():
	api.dropConnection()

class Api:
	def __init__(self):
		self.window = None
		self.client = None

	def createConnection(self, data):
		addr, username = data["addr"], data["username"]
		try:
			ip, port = addr.split(":")
			port = int(port)
		except:
			return "IP address is invalid"

		if not username:
			return "Username can not be empty"

		self.client = Client((ip,port), self, username)
		result = self.client.connect()
		if result == True:
			return "success"
		else:
			return result

	def dropConnection(self):
		self.client.disconnect()

	def disconnection(self, message):
		eel.disconnection(message)

	def addMessage(self, content, mine, date, sender):
		eel.addMessage(content, mine, date, sender)

	def sendMessage(self, content):
		self.client.sendMessage(content)

def is_port_in_use(port):
	import socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.settimeout(1)
		return s.connect_ex(('localhost', port)) == 0

def get_random_port():
	while True:
		port = random.randint(10000, 65000)
		if not is_port_in_use(port):
			return port
		print("PORT IN USE!")

if __name__ == "__main__":
	api = Api()
	eel.init('assets')
	eel.start('index.html', size=(1270,720), port=get_random_port())