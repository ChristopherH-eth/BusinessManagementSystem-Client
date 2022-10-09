import this
from network.tcp import *

# file: client.py
# author: 0xChristopher

def main():
    newTcp = Tcp()

    print(newTcp.getHost())

    while (True):
        fId = input("Enter function id: ")

        if (fId != "exit"):
            newTcp.send(fId)
        else :
            break

main()