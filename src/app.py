# Imports
import asyncio
from time import sleep

from Network.tcp import newTcp
from Network.listen import msgQueue
from Util.funcUtil import FuncUtil
from Log.log import Log
from GUI.mainWindow import app

'''
@file client.py
@author 0xChristopher
@brief This is the entry point for the Business Management System client side application.
'''

##
# Functions
##

## @brief The WaitForServer() function is a coroutine to wait for a server reply before continuing
async def WaitForServer():
    count = 0

    while (msgQueue.empty() and count != 60):
        count += 1
        sleep(1)
    
    return count

## Client application entry point
async def main():
    Log.GetLogger().info("Welcome to Business Management System v1.0.0")
    Log.GetLogger().info("Connecting to server")
    Log.GetLogger().info("Waiting for response...")

    # Wait for server connected message 
    timetoConnect = await WaitForServer()

    # Make sure we have a working connection to the server
    if (msgQueue.empty() == True):
        Log.GetLogger().error("Server connection error, no response from server")
        return
    else:
        Log.GetLogger().info("Time to connect: " + str(timetoConnect) + " seconds")

    # Print queued messages upon server connection
    newTcp.Receive()

    # Launch app window
    app.exec_()

    # Disconnect from server
    FuncUtil.DirectInput("exit")
    newTcp.Disconnect()
    input()

if (__name__ == "__main__"):
    asyncio.run(main())