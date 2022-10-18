# Imports
from enum import Enum
from time import sleep
from HR.employee import *
from Log.log import *

##
# @file funcUtil.py
# @author 0xChristopher
# @brief
##

# Example employee
firstName = "John"
lastName = "Doe"
birthDate = "1/1/2020"
position = "Manager"
age = "32"
idNumber = "123456"

class FuncUtil(Enum):
    addEmployee = 100
    removeEmployee = 101
    updateEmployee = 102

    # Functions
    # @brief The isValid() function checks if a function id is valid
    # @param cls The enum class containing function ids
    # @param fId The function id number
    def isValid(cls, fId):
        convertedFId = 0
        
        try:
            convertedFId = int(fId)
        except:
            pass

        values = set(item.value for item in FuncUtil)
        return convertedFId in values

    # @brief The directInput() function takes user input and executes the corresponding function
    # @param running Remains true while the program is running
    # @param fId The unique id of the function to be executed
    # @param newTcp The current connection to the server
    def directInput(running, fId, newTcp):
        # Check if an 'exit' or 'shutdown' command was given
            if (fId != "exit" and fId != "shutdown"):
                newTcp.connect()
                # Check submitted function id against valid function ids
                if (FuncUtil.isValid(FuncUtil, fId)):
                    # Add employee
                    if (fId == "100"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        Log.getLogger().info("Sending: " + employeeJson)

                        msg = fId + " " + employeeJson
                        newTcp.send(msg)
                    # Remove employee
                    elif (fId == "101"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        Log.getLogger().info("Sending: " + employeeJson)

                        msg = fId + " " + employeeJson
                        newTcp.send(msg)
                    # Update employee
                    elif (fId == "102"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        Log.getLogger().info("Sending: " + employeeJson)

                        msg = fId + " " + employeeJson
                        newTcp.send(msg)
                    else:
                        newTcp.send(fId)
                    
                    sleep(1) # Give server time to respond
                else:
                    print("Invalid input")
            else:
                newTcp.send(fId)
                newTcp.disconnect()
                running = False

            return running