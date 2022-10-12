# Imports
import enum
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
# Main working loop
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

main()