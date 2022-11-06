from HR.employee import employee
from Util.funcUtil import funcUtil
from Network.tcp import newTcp

'''
@file test_02_employee.py
@author 0xChristopher
@brief This file tests the Employee module.
'''

## @brief Test the EmployeeInfo() function
def test_EmployeeInfo():
    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    emp = employee.EmployeeInfo(firstName, lastName, birthDate, position, salary, empId)

    assert emp == "{\"firstName\": \"John\", \"lastName\": \"Doe\", \"birthDate\": \"1/1/1990\", \"position\": \"Representative\", \"salary\": 14000.53, \"empId\": 1}"

## @brief Test the LoginInfo() function
def test_LoginInfo():
    username = ""
    password = ""

    login = employee.LoginInfo(username, password)

    assert login == "{\"username\": \"\", \"password\": \"\"}"

## @brief Test the Login() function
def test_Login(capsys):
    username = ""
    password = ""

    employee.Login(username, password)
    # captured = capsys.readouterr()

    # assert captured.out == "Sending: {\"username\": \"\", \"password\": \"\"}"

    funcUtil.WaitForReply()

    assert newTcp.Receive() == "Login successful"

## @brief Test the Logout() function
def test_Logout():
    employee.Logout()
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "Logout successful"

## @brief Test the AddEmployee() function
def test_AddEmployee():
    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    employee.AddEmployee(firstName, lastName, birthDate, position, salary, empId)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "addEmployee function successfully called"

## @brief Test the AddEmployee() function with a duplicate empId - should fail
def test_AddEmployeeDuplicateEmpId():
    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    employee.AddEmployee(firstName, lastName, birthDate, position, salary, empId)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "Failed to add employee"

## @brief Test the RemoveEmployee() function
def test_RemoveEmployee():
    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    employee.RemoveEmployee(firstName, lastName, birthDate, position, salary, empId)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "removeEmployee function successfully called"

## @brief Test the UpdateEmployee() function
def test_UpdateEmployee():
    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    employee.UpdateEmployee(firstName, lastName, birthDate, position, salary, empId)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == "updateEmployee function successfully called"

## @brief Test the SearchEmployees() function
def test_SearchEmployees():
    firstName = "John"
    result = {"firstName": "John"}

    employee.SearchEmployees(firstName)
    funcUtil.WaitForReply()

    assert newTcp.Receive() == result