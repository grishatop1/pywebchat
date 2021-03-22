import socket
import threading
import pickle
import datetime
import time
import atexit
from transfer import Transfer

class Server:
    def __init__(self, addr):
        self.clients = {}
        self.addr = addr
        self.running = False

    def run(self):
        self.s = socket.socket()
        self.s.bind(self.addr)
        self.s.listen()
        self.running = True
        print(f"Server started on {self.addr}")
        self.mainThread()
    
    def handleClient(self, conn, addr):
        trans = Transfer(conn)
        username = trans.recvData().decode()
        if username in self.clients:
            trans.send(b"in-use")
            return
        self.clients[username] = trans
        print(f"{username} has connected!")
        trans.send(b"success")

        while True:
            raw = trans.recvData()

            if not raw: break
            if raw == b"drop": break

            data = pickle.loads(raw)

            if data["type"] == "msg":
                msg = data["content"]
                date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                data = {"type": "msg", "sender": username, "date": date, 
                    "content": msg}
                self.sendAll(pickle.dumps(data))

        print(f"{username} has disconnected.")
        del self.clients[username]

    def sendAll(self, data, username=""):
        if username:
            for user, trans in self.clients.items():
                if username == user:
                    continue
                trans.send(data)
        else:
            for _, trans in self.clients.items():
                trans.send(data)

    def mainThread(self):
        while self.running:
            conn, addr = self.s.accept()
            threading.Thread(target=self.handleClient, daemon=True, 
                args=(conn, addr)).start()
            print(f"Handling connection on {addr[0]}:{addr[1]}")

def consoleMessage():
    while True:
        msg = input()
        if msg:
            data = pickle.dumps({"type": "msg","sender": "SERVER", "date": "", "content": msg})
            server.sendAll(data)

if __name__ == "__main__":
    server = Server((socket.gethostbyname(socket.gethostname()), 25565))
    #threading.Thread(target=consoleMessage, daemon=True).start() #buggy
    server.run()