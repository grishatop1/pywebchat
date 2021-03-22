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
        self.s.settimeout(5)
        try:
            self.s.connect(self.addr)
        except socket.error:
            return "Server not found. Try again."
        self.s.settimeout(None)
        self.trans = Transfer(self.s)
        self.trans.send(self.username.encode())
        response = self.trans.recvData()
        if response == b"in-use":
            return "Username already in use."
        if response == b"success":
            self.connected = True
            self.s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 5000, 3000))
            threading.Thread(target=self.mainThread, daemon=True).start()
            return True

    def disconnect(self):
        self.trans.send(b"drop")
        self.s.close()

    def sendMessage(self, content):
        data = {
            "type": "msg",
            "content": content
        }
        self.trans.sendDataPickle(data)

    def mainThread(self):
        while self.connected:
            raw = self.trans.recvData()
            if not raw:                 
                break
            if raw == b"drop":
                self.api.disconnection("Server closed connection.")
                return

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

        self.api.disconnection("Connection lost.")
        