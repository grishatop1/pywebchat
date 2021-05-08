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

if __name__ == "__main__":
	print("LOADING...")
	api = Api()
	eel.init('assets')
	eel.start('index.html', size=(1270,720), port=0)