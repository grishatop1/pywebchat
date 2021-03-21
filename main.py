import webview
import threading
import random
from client import Client

class Api:
    def __init__(self):
        self.window = None
        self.client = None

    def addMessage(self, content, mine, date, sender):
        js = fr"""
        
        addMessage('{content}', '{mine}', '{date}', '{sender}');
        
        """
        self.window.evaluate_js(js)

    def sendMessage(self, content):
        self.client.sendMessage(content)

if __name__ == "__main__":
    username = input("Enter your username: ")
    if not username:
        username = f"tester{random.randint(0,9999999)}"
    addr = input("Enter IP address: ")
    if not addr:
        addr = "192.168.0.33:25565"

    ip, port = addr.split(":")
    port = int(port)

    api = Api()
    client = Client((ip,port), api, username)
    print("Connecting...")
    client.connect()
    print("Connected!")

    window = webview.create_window('Chat', "assets/index.html", width=1270, height=720, js_api=api, min_size=(300, 400))
    api.window = window
    api.client = client
    webview.start(debug=True)