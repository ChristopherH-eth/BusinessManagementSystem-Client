import json

##
# @file employee.py
# @author 0xChristopher
# @brief
##

class Employee:
    def createEmployee(firstName, lastName, birthDate, position, age, idNumber):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "birthDate": birthDate,
            "position": position,
            "age": age,
            "idNumber": idNumber
        }

        json.dumps(employee)