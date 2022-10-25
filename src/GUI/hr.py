# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from Util.funcUtil import FuncUtil
from Network.tcp import newTcp
from HR.employee import Employee
from Log.log import Log

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
        self.highBodyLayout = qtw.QVBoxLayout()
        self.lowBodyLayout = qtw.QVBoxLayout()
        self.sideNavLayout = qtw.QGridLayout()
        self.inputFieldsLayout = qtw.QFormLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.bodyLayout)
        self.bodyLayout.addLayout(self.sideNavLayout)
        self.bodyLayout.addLayout(self.innerBodyLayout)
        self.innerBodyLayout.addLayout(self.highBodyLayout)
        self.innerBodyLayout.addLayout(self.lowBodyLayout)
        self.lowBodyLayout.addLayout(self.inputFieldsLayout)
        self.lowBodyLayout.addLayout(self.buttonLayout)
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
        self.headerLayout.addWidget(self.windowLabel)
        self.windowSpacer = qtw.QWidget()
        self.windowSpacer.setFixedHeight(75)
        self.headerLayout.addWidget(self.windowSpacer)

        # Side Nav Label
        self.sideNavLabel = qtw.QLabel("Navigation")
        self.sideNavLabel.setFont(qtg.QFont("Helvecta", 10))
        self.sideNavLabel.setAlignment(qtc.Qt.AlignCenter)
        self.sideNavLabel.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.sideNavLabel, 0, 0)
        self.sideNavSpacer = qtw.QWidget()
        self.sideNavSpacer.setFixedHeight(25)
        self.sideNavLayout.addWidget(self.sideNavSpacer, 1, 0)

        # Employee Form Label
        self.empInfoLabel = qtw.QLabel("Employee Information")
        self.empInfoLabel.setFont(qtg.QFont("Helvecta", 10))
        self.empInfoLabel.setAlignment(qtc.Qt.AlignCenter)
        self.highBodyLayout.addWidget(self.empInfoLabel)
        self.empInfoSpacer = qtw.QWidget()
        self.empInfoSpacer.setFixedHeight(25)
        self.highBodyLayout.addWidget(self.empInfoSpacer)

        ##
        # Input Fields
        ##

        # Employee Information
        self.firstName = qtw.QLineEdit()
        self.lastName = qtw.QLineEdit()
        self.birthDate = qtw.QLineEdit()
        self.age = qtw.QLineEdit()
        self.position = qtw.QLineEdit()
        self.empId = qtw.QLineEdit()

        self.inputFieldsLayout.addRow("First Name: ", self.firstName)
        self.inputFieldsLayout.addRow("Last Name: ", self.lastName)
        self.inputFieldsLayout.addRow("Date of Birth: ", self.birthDate)
        self.inputFieldsLayout.addRow("Age: ", self.age)
        self.inputFieldsLayout.addRow("Position: ", self.position)
        self.inputFieldsLayout.addRow("ID Number: ", self.empId)

        ##
        # Side Nav Buttons
        ##

        # Dashboard Button
        self.dashButton = qtw.QPushButton("Dashboard")
        self.dashButton.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.dashButton, 2, 0)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.dashSpacer = qtw.QWidget()
        self.dashSpacer.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.dashSpacer, 2, 1)

        # HR Button
        self.hrButton = qtw.QPushButton("Human Resources")
        self.hrButton.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.hrButton, 3, 0)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.hrSpacer = qtw.QWidget()
        self.hrSpacer.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.hrSpacer, 3, 1)

        ##
        # Employee Function Buttons
        ##

        # Form/Button Spacer
        self.empButtonSpacer = qtw.QWidget()
        self.empButtonSpacer.setFixedHeight(25)
        self.buttonLayout.addWidget(self.empButtonSpacer)

        # Add Employee Button
        self.addEmployeeButton = qtw.QPushButton("Add", clicked = lambda: AddEmployee())
        self.addEmployeeButton.setFixedWidth(250)
        self.buttonLayout.addWidget(self.addEmployeeButton)

        # Remove Employee Button
        self.removeEmployeeButton = qtw.QPushButton("Remove", clicked = lambda: RemoveEmployee())
        self.removeEmployeeButton.setFixedWidth(250)
        self.buttonLayout.addWidget(self.removeEmployeeButton)

        # Update Employee Button
        self.updateEmployeeButton = qtw.QPushButton("Update", clicked = lambda: UpdateEmployee())
        self.updateEmployeeButton.setFixedWidth(250)
        self.buttonLayout.addWidget(self.updateEmployeeButton)

        ##
        # Functions
        ##

        ## @brief The AddEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def AddEmployee():
            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            age = self.age.text()
            position = self.position.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            Employee.AddEmployee(firstName, lastName, birthDate, age, position, empId)
            success = FuncUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                Log.GetLogger().error("Host connection timeout")
        
        ## @brief The RemoveEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def RemoveEmployee():
            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            age = self.age.text()
            position = self.position.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            Employee.RemoveEmployee(firstName, lastName, birthDate, age, position, empId)
            success = FuncUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                Log.GetLogger().error("Host connection timeout")

        ## @brief The UpdateEmployee() function calls the FuncUtil.directInput() function with the corresponding
        #       function id. 'success' returns true based on server response
        def UpdateEmployee():
            firstName = self.firstName.text()
            lastName = self.lastName.text()
            birthDate = self.birthDate.text()
            age = self.age.text()
            position = self.position.text()
            empId = self.empId.text()

            newTcp.Connect() # Make sure we're still connected to the server
            Employee.UpdateEmployee(firstName, lastName, birthDate, age, position, empId)
            success = FuncUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                Log.GetLogger().error("Host connection timeout")