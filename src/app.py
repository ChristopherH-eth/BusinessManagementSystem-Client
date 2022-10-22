# Imports
from Network.tcp import newTcp
from Network.listen import msgQueue
from time import sleep
from Util.funcUtil import FuncUtil
from Log.log import Log
from GUI.mainWindow import app
import asyncio

##
# @file client.py
# @author 0xChristopher
# @brief This is the entry point for the Business Management System client side application.
##

# Functions
# The waitForServer() function is a coroutine to wait for a server reply before continuing
async def waitForServer():
    count = 0

    while (msgQueue.empty() and count != 60):
        count += 1
        sleep(1)
    
    return count

# Client application entry point
async def main():
    Log.getLogger().info("Welcome to Business Management System v1.0.0")
    Log.getLogger().info("Connecting to server")
    Log.getLogger().info("Waiting for response...")

    # Wait for server connected message 
    timetoConnect = await waitForServer()

    # Make sure we have a working connection to the server
    if (msgQueue.empty() == True):
        Log.getLogger().error("Server connection error, no response from server")
        return
    else:
        Log.getLogger().info("Time to connect: " + str(timetoConnect) + " seconds")

    # Print queued messages upon server connection
    newTcp.receive()

    # Launch app window
    app.exec_()

    # Disconnect from server
    FuncUtil.directInput("exit", newTcp)
    newTcp.disconnect()

if (__name__ == "__main__"):
    asyncio.run(main())