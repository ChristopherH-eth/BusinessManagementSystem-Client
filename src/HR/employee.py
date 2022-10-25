# Imports
import json

from Log.log import Log
from Network.tcp import newTcp
from Util.funcUtil import FuncUtil

'''
@file employee.py
@author 0xChristopher
@brief This file allows for conversion of employee info into JSON format to be sent to the server,
        which will then update the database.
'''

class Employee:

    ##
    # Functions
    ##

    ## @brief The EmployeeInfo() function takes in employee details and returns a JSON object
    #  @param firstName Employee's first name
    #  @param lastName Employee's last name
    #  @param birthDate Employee's birth date
    #  @param position Employee's position in the company
    #  @param age Employee's current age
    #  @param idNumber Employee's id number
    def EmployeeInfo(firstName, lastName, birthDate, position, age, idNumber):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "birthDate": birthDate,
            "position": position,
            "age": age,
            "idNumber": idNumber
        }

        return json.dumps(employee)

    ## @brief The AddEmployee() function attempts to send employee data to the server to be added to the
    #       database
    def AddEmployee(firstName, lastName, birthDate, position, age, empId):
        fId = "100"

        if (FuncUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, age, empId)
            Log.GetLogger().info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)

    ## @brief The RemoveEmployee() function attempts to send employee data to the server to be removed from the
    #       database
    def RemoveEmployee(firstName, lastName, birthDate, position, age, empId):
        fId = "101"

        if (FuncUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, age, empId)
            Log.GetLogger().info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)

    ## @brief The UpdateEmployee() function attempts to send employee data to the server to be updated in the
    #       database
    def UpdateEmployee(firstName, lastName, birthDate, position, age, empId):
        fId = "102"

        if (FuncUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, age, empId)
            Log.GetLogger().info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)