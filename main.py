import webview
import threading
import random
from client import Client

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

    def addMessage(self, content, mine, date, sender):
        js = fr"""
        
        addMessage('{content}', '{mine}', '{date}', '{sender}');
        
        """
        self.window.evaluate_js(js)

    def sendMessage(self, content):
        self.client.sendMessage(content)

if __name__ == "__main__":
    api = Api()
    window = webview.create_window('Chat', "assets/index.html", width=1270, height=720, js_api=api, min_size=(300, 400))
    api.window = window
    webview.start()