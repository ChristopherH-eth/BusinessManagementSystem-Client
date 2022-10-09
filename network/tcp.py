import socket

# file: tcp.py
# author: 0xChristopher

class Tcp:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname("127.0.0.1")
        self.port = 54000

    def getHost(self):
        return self.host

    def send(self, fId):
        input = str(fId)

        self.s.connect((self.host, self.port))
        self.s.send(bytes(input, encoding='utf8'))
        print(self.s.recv(4096))
        self.s.close()