# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from Util.funcUtil import funcUtil
from Network.tcp import newTcp
from HR.employee import employee
from Log.log import log

'''
@file hr.py
@author 0xChristopher
@brief This file defines how the UI will be set up for the human resources window.
'''

class HumanResources():
    ## @brief The SetUI() function sets the UI of the human resources window
    #  @param MainWindow The MainWindow object
    def SetUI(self, MainWindow):

        ##
        # Window Layouts and Attributes
        ##

        # Set window title
        MainWindow.setWindowTitle("Business Management System - Human Resources")

        # Set central widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Set layouts
        self.outerLayout = qtw.QVBoxLayout()
        self.headerLayout = qtw.QVBoxLayout()
        self.bodyLayout = qtw.QHBoxLayout()
        self.innerBodyLayout = qtw.QVBoxLayout()
        self.employeeSearch = qtw.QVBoxLayout()
        self.empSearchBar = qtw.QFormLayout()
        self.empSearchBtns = qtw.QGridLayout()
        self.employeeForm = qtw.QVBoxLayout()
        self.sideNavLayout = qtw.QGridLayout()
        self.inputFieldsLayout = qtw.QFormLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.bodyLayout)
        self.bodyLayout.addLayout(self.sideNavLayout)
        self.bodyLayout.addLayout(self.innerBodyLayout)
        self.innerBodyLayout.addLayout(self.employeeSearch)
        self.innerBodyLayout.addLayout(self.empSearchBar)
        self.innerBodyLayout.addLayout(self.empSearchBtns)
        self.innerBodyLayout.addLayout(self.employeeForm)
        self.innerBodyLayout.addLayout(self.inputFieldsLayout)
        self.innerBodyLayout.addLayout(self.buttonLayout)
        self.centralWidget.setLayout(self.outerLayout)

        self.outerLayout.setAlignment(qtc.Qt.AlignTop)

        # Window dimensions
        MainWindow.setGeometry(400, 200, 1800, 1500)

        ##
        # Labels 
        ##

        # Window Label
        self.windowLabel = qtw.QLabel("Human Resources")
        self.windowLabel.setFont(qtg.QFont("Helvecta", 18))
        self.windowLabel.setAlignment(qtc.Qt.AlignCenter)
        self.windowSpacer = qtw.QWidget()
        self.windowSpacer.setFixedHeight(75)

        # Side Nav Label
        self.sideNavLabel = qtw.QLabel("Navigation")
        self.sideNavLabel.setFont(qtg.QFont("Helvecta", 10))
        self.sideNavLabel.setAlignment(qtc.Qt.AlignCenter)
        self.sideNavLabel.setFixedWidth(250)
        self.sideNavSpacer = qtw.QWidget()
        self.sideNavSpacer.setFixedHeight(25)

        # Employee Search Label
        self.empSearchLabel = qtw.QLabel("Search Employees")
        self.empSearchLabel.setFont(qtg.QFont("Helvecta", 10))
        self.empSearchLabel.setAlignment(qtc.Qt.AlignCenter)
        self.empSearchSpacer = qtw.QWidget()
        self.empSearchSpacer.setFixedHeight(25)

        # Employee Form Label
        self.empInfoLabel = qtw.QLabel("Employee Information")
        self.empInfoLabel.setFont(qtg.QFont("Helvecta", 10))
        self.empInfoLabel.setAlignment(qtc.Qt.AlignCenter)
        self.empInfoSpacer = qtw.QWidget()
        self.empInfoSpacer.setFixedHeight(25)

        ##
        # Input Fields
        ##

        # Search Bar
        self.searchName = qtw.QLineEdit()

        # Employee Information
        self.firstName = qtw.QLineEdit()
        self.lastName = qtw.QLineEdit()
        self.birthDate = qtw.QLineEdit()
        self.salary = qtw.QLineEdit()
        self.position = qtw.QLineEdit()
        self.empId = qtw.QLineEdit()

        ##
        # Side Nav Buttons
        ##

        # Dashboard Button
        self.dashButton = qtw.QPushButton("Dashboard")
        self.dashButton.setFixedWidth(250)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.dashSpacer = qtw.QWidget()
        self.dashSpacer.setFixedWidth(250)

        # HR Button
        self.hrButton = qtw.QPushButton("Human Resources")
        self.hrButton.setFixedWidth(250)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.hrSpacer = qtw.QWidget()
        self.hrSpacer.setFixedWidth(250)

        ##
        # Employee Function Buttons
        ##

        # Form/Button Spacer
        self.empButtonSpacer = qtw.QWidget()
        self.empButtonSpacer.setFixedHeight(25)

        # Search/Button Spacers
        self.empSearchSpacer = qtw.QWidget()
        self.empSearchSpacer.setFixedHeight(25)
        self.empSearchSpacer1 = qtw.QWidget()
        self.empSearchSpacer1.setFixedHeight(25)
        self.empSearchSpacer2 = qtw.QWidget()
        self.empSearchSpacer2.setFixedHeight(50)

        # Add Employee Button
        self.addEmployeeButton = qtw.QPushButton("Add", clicked = lambda: AddEmployee())
        self.addEmployeeButton.setFixedWidth(250)

        # Remove Employee Button
        self.removeEmployeeButton = qtw.QPushButton("Remove", clicked = lambda: RemoveEmployee())
        self.removeEmployeeButton.setFixedWidth(250)

        # Update Employee Button
        self.updateEmployeeButton = qtw.QPushButton("Update", clicked = lambda: UpdateEmployee())
        self.updateEmployeeButton.setFixedWidth(250)

        # Search Employees Button
        self.searchEmployeesButton = qtw.QPushButton("Search", clicked = lambda: SearchEmployees())
        self.searchEmployeesButton.setFixedWidth(250)

        ##
        # Build Window
        ##

        # Window Header
        self.headerLayout.addWidget(self.windowLabel)
        self.headerLayout.addWidget(self.windowSpacer)

        # Side Nav
        self.sideNavLayout.addWidget(self.sideNavLabel, 0, 0)
        self.sideNavLayout.addWidget(self.sideNavSpacer, 1, 0)
        self.sideNavLayout.addWidget(self.dashButton, 2, 0)
        self.sideNavLayout.addWidget(self.dashSpacer, 2, 1)
        self.sideNavLayout.addWidget(self.hrButton, 3, 0)
        self.sideNavLayout.addWidget(self.hrSpacer, 3, 1)

        # Employee Search
        self.employeeSearch.addWidget(self.empSearchLabel)
        self.employeeSearch.addWidget(self.empSearchSpacer)
        self.empSearchBar.addRow("Name: ", self.searchName)
        self.empSearchBtns.addWidget(self.empSearchSpacer1)
        self.empSearchBtns.addWidget(self.searchEmployeesButton)
        self.empSearchBtns.addWidget(self.empSearchSpacer2)

        # Employee Form
        self.employeeForm.addWidget(self.empInfoLabel)
        self.employeeForm.addWidget(self.empInfoSpacer)
        self.inputFieldsLayout.addRow("First Name: ", self.firstName)
        self.inputFieldsLayout.addRow("Last Name: ", self.lastName)
        self.inputFieldsLayout.addRow("Date of Birth: ", self.birthDate)
        self.inputFieldsLayout.addRow("Position: ", self.position)
        self.inputFieldsLayout.addRow("Salary: ", self.salary)
        self.inputFieldsLayout.addRow("ID Number: ", self.empId)

        # Employee Function Buttons
        self.buttonLayout.addWidget(self.empButtonSpacer)
        self.buttonLayout.addWidget(self.addEmployeeButton)
        self.buttonLayout.addWidget(self.removeEmployeeButton)
        self.buttonLayout.addWidget(self.updateEmployeeButton)

        

        ##
        # Functions
        ##

        ## @brief The AddEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def AddEmployee():
            log.logger.info("Executing AddEmployee() function")

            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            position = self.position.text()
            salary = self.salary.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            employee.AddEmployee(firstName, lastName, birthDate, position, salary, empId)
            success = funcUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                log.logger.error("Host connection timeout")
        
        ## @brief The RemoveEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def RemoveEmployee():
            log.logger.info("Executing RemoveEmployee() function")

            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            position = self.position.text()
            salary = self.salary.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            employee.RemoveEmployee(firstName, lastName, birthDate, position, salary, empId)
            success = funcUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                log.logger.error("Host connection timeout")

        ## @brief The UpdateEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def UpdateEmployee():
            log.logger.info("Executing UpdateEmployee() function")

            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            position = self.position.text()
            salary = self.salary.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            employee.UpdateEmployee(firstName, lastName, birthDate, position, salary, empId)
            success = funcUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                log.logger.error("Host connection timeout")

        ## @brief The SearchEmployee() function queries the server which searches the database for
        #       employees.
        def SearchEmployees():
            log.logger.info("Executing SearchEmployees() function")

            firstName = self.searchName.text()

            newTcp.Connect() # Make sure we're still connected to the server
            employee.SearchEmployees(firstName)
            success = funcUtil.WaitForReply()

            # Check if we've successfully received a reply from the server
            if (success):
                msg = newTcp.Receive()

                try:
                    log.logger.info("Found " + msg["firstName"])
                except:
                    log.logger.error("Could not parse invalid JSON string: " + msg)
            else:
                log.logger.error("Host connection timeout")