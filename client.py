# Imports
from Network.tcp import *
from Network.listen import msgQueue
from time import sleep

##
# @file client.py
# @author 0xChristopher
# @brief
##

# Functions
def main():
    newTcp = Tcp()
    running = True

    print("Welcome to Business Management System v1.0.0")
    print("Connecting to host at: " + newTcp.getHost())
    print("Waiting for response...")
    sleep(5) # Wait for server connected message
    newTcp.receive()

    # Main running loop
    while (running):
        if (msgQueue.empty() == True):
            fId = input("Enter function id: ")

            # Check if an 'exit' command was given
            if (fId != "exit"):
                newTcp.connect()
                newTcp.send(fId)
            else:
                newTcp.send(fId)
                newTcp.disconnect()
                running = False

            sleep(1) # Give server time to respond
        else:
            newTcp.receive()

main()