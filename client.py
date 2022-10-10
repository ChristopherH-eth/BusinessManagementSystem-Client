# Imports
from network.tcp import *

##
# @file client.py
# @author 0xChristopher
# @brief
##

# Functions
def main():
    newTcp = Tcp()

    print(newTcp.getHost())

    # Main running loop
    while (True):
        fId = input("Enter function id: ")

        # Check if an 'exit' command was given
        if (fId != "exit"):
            newTcp.connect()
            newTcp.send(fId)
        else:
            newTcp.send(fId)
            newTcp.disconnect()
            break

main()