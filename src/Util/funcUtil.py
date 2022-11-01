# Imports
from enum import Enum
from time import sleep

from Log.log import Log
from Network.listen import msgQueue
from Network.tcp import newTcp

'''
@file funcUtil.py
@author 0xChristopher
@brief This file handles the indentification of which function to call and subsequently send a request
        to the server to call the corresponding function with the data in the request.
'''

class FuncUtil(Enum):
    login = 100
    logout = 101
    addEmployee = 102
    removeEmployee = 103
    updateEmployee = 104
    searchEmployees = 105

    ##
    # Functions
    ##
    
    ## @brief The IsValid() function checks if a function id is valid
    #  @param fId The function id number
    def IsValid(fId):
        convertedFId = 0
        
        try:
            convertedFId = int(fId)
        except:
            pass

        values = set(item.value for item in FuncUtil)

        return convertedFId in values

    ## @brief The DirectInput() function takes user input and executes the corresponding function
    #  @param fId The unique id of the function to be executed
    #  @param newTcp The current connection to the server
    def DirectInput(fId):
        # Check if an 'exit' or 'shutdown' command was given
        if (fId != "exit" and fId != "shutdown"):
            return
        else:
            newTcp.Send(fId)
        
    ## @brief The WaitForReply() function waits for a server response after sending a request
    def WaitForReply():
        count = 0
        success = False

        while (msgQueue.empty() and count != 60):
            count += 1
            sleep(1)
            
        if (msgQueue.empty() == False):
            success = True
        else:
            success = False
        
        return success