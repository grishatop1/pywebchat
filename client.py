import socket
import threading
import pickle
import datetime
from transfer import Transfer

class Client:
    def __init__(self, addr, api, username):
        self.addr = addr
        self.api = api
        self.username = username
        self.connected = False

    def connect(self):
        self.s = socket.socket()
        self.s.connect(self.addr)
        self.trans = Transfer(self.s)
        self.trans.send(self.username.encode())
        response = self.trans.recvData()
        if response == b"in-use":
            return "Username already in use."
        if response == b"success":
            self.connected = True
            threading.Thread(target=self.mainThread, daemon=True).start()
            return True

    def sendMessage(self, content):
        data = {
            "type": "msg",
            "content": content
        }
        self.trans.sendDataPickle(data)

    def mainThread(self):
        while self.connected:
            raw = self.trans.recvData()
            if not raw: return
            if raw == b"drop": return

            data = pickle.loads(raw)
            if data["type"] == "msg":
                if data["sender"] == self.username:
                    self.api.addMessage(data["content"], 
                        "true", 
                        data["date"],
                        "Me")
                else:
                    self.api.addMessage(data["content"], 
                        "false", 
                        data["date"],
                        data["sender"])
        