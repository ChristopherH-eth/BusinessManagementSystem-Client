# Imports
import threading
import queue

##
# @file listen.py
# @author 0xChristopher
# @brief
##

# Queue to temporarily store messages from the server
msgQueue = queue.Queue(maxsize = 100)

class Listener(threading.Thread):
    # Functions
    # @brief Thread constructor
    def __init__(self, threadName, threadId, socket):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId
        self.s = socket
        self.listening = True
        self.q = msgQueue

    # @brief The run() function determines what the thread will do while running
    def run(self):
        # Thread loop for listening
        while (self.listening):
            try:
                msg = self.s.recv(4096).decode("utf-8")

                if (msg[0] != ''):
                    self.q.put(msg)
            except:
                pass

    # @brief The endThread() function terminates the thread
    def endThread(self):
        self.listening = False