# Imports
import threading
import queue

'''
@file listen.py
@author 0xChristopher
@brief This file is responsible for creating a thread to listen for incoming responses from the server
        application, storing them in a queue if the client application is busy, and then logging them.
'''

msgQueue = queue.Queue(maxsize = 100) # Queue to temporarily store messages from the server

class Listener(threading.Thread):
    ##
    # Functions
    ##

    ## @brief Listener thread constructor
    def __init__(self, threadName, threadId, socket):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId
        self.s = socket
        self.listening = True
        self.q = msgQueue

    ## @brief The run() function determines what the thread will do while running
    def run(self):
        # Thread loop for listening
        while (self.listening):
            try:
                msg = self.s.recv(4096).decode("utf-8")

                if (msg[0] != ''):
                    self.q.put(msg)
            except:
                pass

    ## @brief The EndThread() function terminates the thread
    def EndThread(self):
        self.listening = False