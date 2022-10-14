# Imports
from Network.tcp import *
from Network.listen import msgQueue
from time import sleep
from HR.employee import *
from Util.funcUtil import *

##
# @file client.py
# @author 0xChristopher
# @brief This is the entry point for the Business Management System client side application.
##

# Example employee
firstName = "John"
lastName = "Doe"
birthDate = "1/1/2020"
position = "Manager"
age = "32"
idNumber = "123456"

# Functions
def main():
    print("Welcome to Business Management System v1.0.0")
    print("Connecting to server")
    print("Waiting for response...")

    running = False # Set 'running' to false until we validate our connection to the server
    newTcp = Tcp()
    sleep(5) # Wait for server connected message

    # Make sure we have a working connection to the server
    if (msgQueue.empty() == True):
        print("Server connection error, no response from server")
        return
    else:
        running = True

    newTcp.receive()

    # Main running loop
    while (running):
        if (msgQueue.empty() == True):
            fId = input("Enter function id: ")

            # Check if an 'exit' or 'shutdown' command was given
            if (fId != "exit" and fId != "shutdown"):
                newTcp.connect()
                # Check submitted function id against valid function ids
                if (FuncUtil.isValid(FuncUtil, fId)):
                    # Add employee
                    if (fId == "100"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        print("Sending: " + employeeJson)

                        msg = fId + " " + employeeJson
                        newTcp.send(msg)
                    # Remove employee
                    elif (fId == "101"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        print("Sending: " + employeeJson)

                        msg = fId + " " + employeeJson
                        newTcp.send(msg)
                    # Update employee
                    elif (fId == "102"):
                        employeeJson = Employee.employeeInfo(
                            firstName, lastName, birthDate, position, age, idNumber)
                        print("Sending: " + employeeJson)

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
        else:
            newTcp.receive()

if (__name__ == "__main__"):
    main()