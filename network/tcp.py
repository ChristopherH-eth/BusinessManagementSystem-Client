# Imports
import socket

##
# @file tcp.py
# @author 0xChristopher
# @brief
##

class Tcp:
    # Tcp constructor
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname("127.0.0.1")
        self.port = 54000
        self.s.connect((self.host, self.port))

    # The getHost() function returns the host ip address
    def getHost(self):
        return self.host

    # The send() function sends a message to the connected server
    def send(self, fId):
        input = str(fId)

        self.s.send(bytes(input, encoding='utf8'))
        print(self.s.recv(4096))

    # The connect() function attempts to connect to the server
    def connect(self):
        try:
            self.s.connect((self.host, self.port))
        except:
            print("Already connected or server not available")

    # The disconnect() function closes the connection with the server
    def disconnect(self):
        self.s.close()