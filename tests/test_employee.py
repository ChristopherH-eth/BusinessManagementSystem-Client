from HR.employee import Employee

'''
@file test_employee.py
@author 0xChristopher
@brief This file tests the Employee module.
'''

## @brief Test the EmployeeInfo() function
def test_EmployeeInfo():
    employee = Employee()

    firstName = "John"
    lastName = "Doe"
    birthDate = "1/1/1990"
    position = "Representative"
    salary = 14000.53
    empId = 1

    emp = employee.EmployeeInfo(firstName, lastName, birthDate, position, salary, empId)

    assert emp == "{\"firstName\": \"John\", \"lastName\": \"Doe\", \"birthDate\": \"1/1/1990\", \"position\": \"Representative\", \"salary\": 14000.53, \"empId\": 1}"