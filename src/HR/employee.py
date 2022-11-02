# Imports
import json

from Log.log import log
from Network.tcp import newTcp
from Util.funcUtil import funcUtil

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

    ## @brief The EmployeeInfo() function takes in employee details and returns a JSON string
    #  @param firstName Employee's first name
    #  @param lastName Employee's last name
    #  @param birthDate Employee's birth date
    #  @param position Employee's position in the company
    #  @param salary The employee's yearly salary
    #  @param empId Employee's id number
    def EmployeeInfo(self, firstName, lastName, birthDate, position, salary, empId):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "birthDate": birthDate,
            "position": position,
            "salary": salary,
            "empId": empId
        }

        return json.dumps(employee)

    ## @brief The LoginInfo() function takes in employee login credentials and returns a JSON string
    #  @param username The username credential of a given employee
    #  @param password The password credential of a given employee
    def LoginInfo(self, username, password):
        login = {
            "username": username,
            "password": password
        }

        return json.dumps(login)

    ## @brief The Login() function attempts to log in the current user
    def Login(self, username, password):
        fId = "100"

        if (funcUtil.IsValid(fId)):
            loginJson = employee.LoginInfo(username, password)
            log.logger.info("Sending: " + loginJson)

            msg = fId + " " + loginJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

    ## @brief The Logout() function attempts to log out the current user
    def Logout(self):
        fId = "101"

        if (funcUtil.IsValid(fId)):
            logoutJson = "{\"username\": \"\", \"password\": \"\"}"
            log.logger.info("Sending: " + logoutJson)

            msg = fId + " " + logoutJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

    ## @brief The AddEmployee() function attempts to send employee data to the server to be added to the
    #       database
    def AddEmployee(self, firstName, lastName, birthDate, position, salary, empId):
        fId = "102"

        if (funcUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, salary, empId)
            log.logger.info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

    ## @brief The RemoveEmployee() function attempts to send employee data to the server to be removed from the
    #       database
    def RemoveEmployee(self, firstName, lastName, birthDate, position, salary, empId):
        fId = "103"

        if (funcUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, salary, empId)
            log.logger.info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

    ## @brief The UpdateEmployee() function attempts to send employee data to the server to be updated in the
    #       database
    def UpdateEmployee(self, firstName, lastName, birthDate, position, salary, empId):
        fId = "104"

        if (funcUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, lastName, birthDate, position, salary, empId)
            log.logger.info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

    ## @brief The SearchEmployees() function attempts to send employee data to the server to be updated in the
    #       database
    def SearchEmployees(self, firstName):
        fId = "105"

        if (funcUtil.IsValid(fId)):
            employeeJson = Employee.EmployeeInfo(firstName, 0, 0, 0, 0, 0)
            log.logger.info("Sending: " + employeeJson)

            msg = fId + " " + employeeJson
            newTcp.Send(msg)
        else:
            log.logger.error("Invalid function call with function id (fId): " + fId)

# Initialize employee object
employee = Employee()