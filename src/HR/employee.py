# Imports
import json

##
# @file employee.py
# @author 0xChristopher
# @brief
##

class Employee:

    # Functions
    # @brief The employeeInfo() function takes in employee details and returns a JSON object
    # @param firstName Employee's first name
    # @param lastName Employee's last name
    # @param birthDate Employee's birth date
    # @param position Employee's position in the company
    # @param age Employee's current age
    # @param idNumber Employee's id number
    def employeeInfo(firstName, lastName, birthDate, position, age, idNumber):
        employee = {
            "firstName": firstName,
            "lastName": lastName,
            "birthDate": birthDate,
            "position": position,
            "age": age,
            "idNumber": idNumber
        }

        return json.dumps(employee)