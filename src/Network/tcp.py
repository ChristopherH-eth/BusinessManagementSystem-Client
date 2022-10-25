# Imports
import socket

from Network.listen import Listener, msgQueue
from Log.log import Log

'''
@file tcp.py
@author 0xChristopher
@brief This file handles the socket creation and subsequent server connection to the server application.
'''

# Server connection info
host = "127.0.0.1"
listenerName = "listener"
listenerId = 1

class Tcp:
    ##
    # Functions
    ##

    ## @brief Tcp constructor
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostbyname(host)
        self.port = 54000

        try:
            self.s.connect((self.host, self.port))
        except:
            Log.GetLogger().error("Server connection error, could not connect to server")
            return

        self.listener = Listener(listenerName, listenerId, self.s)
        self.listener.start()


    ## @brief The GetHost() function returns the host ip address
    def GetHost(self):
        return self.host

    ## @brief The Send() function sends a message to the connected server
    #  @param fId The id number of the function to be called server side
    def Send(self, fId):
        input = str(fId)
        self.s.sendall(bytes(input, encoding = 'utf8'))

    ## @brief The Receive() function displays messages for the client held in the msgQueue
    def Receive(self):
        if (msgQueue.empty() == False):
            while (msgQueue.qsize() > 0):
                Log.GetLogger().info(msgQueue.get())

    ## @brief The Connect() function attempts to connect to the server
    def Connect(self):
        try:
            self.s.connect((self.host, self.port))
        except:
            pass

    ## @brief The Disconnect() function closes the connection with the server and terminates threads
    def Disconnect(self):
        self.listener.EndThread()
        self.s.close()

newTcp = Tcp()