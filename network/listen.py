# Imports
import threading
import queue

##
# @file listen.py
# @author 0xChristopher
# @brief
##

msgQueue = queue.Queue(maxsize = 100)

class Listener(threading.Thread):
    # Thread constructor
    def __init__(self, threadName, threadId, socket):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId
        self.s = socket
        self.listening = True
        self.q = msgQueue

    # The run() function determines what the thread will do while running
    def run(self):
        # Thread loop for listening
        while (self.listening):
            try:
                msg = self.s.recv(4096).decode("utf-8")

                if (msg[0] != b''):
                    self.q.put(msg)
            except:
                pass

    # The endThread() function terminates the thread
    def endThread(self):
        self.listening = False