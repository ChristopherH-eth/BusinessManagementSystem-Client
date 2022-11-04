# Imports
import asyncio
from time import sleep

from Network.tcp import newTcp
from Network.listen import msgQueue
from Util.funcUtil import funcUtil
from Log.log import log
from GUI.mainWindow import app

'''
@file app.py
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
    log.logger.info("Welcome to Business Management System v1.0.0")
    log.logger.info("Connecting to server")
    log.logger.info("Waiting for response...")

    # Wait for server connected message 
    timetoConnect = await WaitForServer()

    # Make sure we have a working connection to the server
    if (msgQueue.empty() == True):
        log.logger.error("Server connection error, no response from server")
        return
    else:
        log.logger.info("Time to connect: " + str(timetoConnect) + " seconds")

    # Print queued messages upon server connection
    newTcp.Receive()

    # Launch app window
    app.exec_()

    # Disconnect from server
    funcUtil.DirectInput("exit")
    newTcp.Disconnect()

if (__name__ == "__main__"):
    asyncio.run(main())