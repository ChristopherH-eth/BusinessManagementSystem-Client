# Imports
import socket
from Network.listen import *

##
# @file tcp.py
# @author 0xChristopher
# @brief
##

host = "127.0.0.1"
listenerName = "listener"
listenerId = 1

class Tcp:
    # Tcp constructor
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(host)
        self.port = 54000
        self.s.connect((self.host, self.port))
        self.listener = Listener(listenerName, listenerId, self.s)
        self.listener.start()


    # The getHost() function returns the host ip address
    def getHost(self):
        return self.host

    # The send() function sends a message to the connected server
    def send(self, fId):
        input = str(fId)
        self.s.sendall(bytes(input, encoding='utf8'))

    # The receive() function displays messages for the client held in the msgQueue
    def receive(self):
        if (msgQueue.empty() == False):
            while (msgQueue.qsize() > 0):
                print(msgQueue.get())

    # The connect() function attempts to connect to the server
    def connect(self):
        try:
            self.s.connect((self.host, self.port))
        except:
            pass

    # The disconnect() function closes the connection with the server and terminates threads
    def disconnect(self):
        self.listener.endThread()
        self.s.close()