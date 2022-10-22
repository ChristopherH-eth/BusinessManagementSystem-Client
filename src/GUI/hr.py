# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from Util.funcUtil import FuncUtil
from Network.tcp import newTcp

##
# @file hr.py
# @author 0xChristopher
# @brief
##

class HumanResources():
    # The SetUI() function sets the UI of the human resources window
    def SetUI(self, MainWindow):

        ##
        # Window layouts and attributes
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
        self.sideNavLayout = qtw.QGridLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.bodyLayout)
        self.bodyLayout.addLayout(self.sideNavLayout)
        self.bodyLayout.addLayout(self.buttonLayout)
        self.centralWidget.setLayout(self.outerLayout)

        self.outerLayout.setAlignment(qtc.Qt.AlignTop)

        # Window dimensions
        MainWindow.setGeometry(400, 200, 1800, 1500)

        ##
        # Labels 
        ##

        # Window Label
        self.windowLabel = qtw.QLabel("Dashboard")
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

        ##
        # Buttons
        ##

        # Dashboard Button
        self.dashButton = qtw.QPushButton("Dashboard")
        self.dashButton.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.dashButton, 1, 0)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.dashSpacer = qtw.QWidget()
        self.dashSpacer.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.dashSpacer, 1, 1)

        # HR Button
        self.hrButton = qtw.QPushButton("Human Resources")
        self.hrButton.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.hrButton, 2, 0)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.hrSpacer = qtw.QWidget()
        self.hrSpacer.setFixedWidth(250)
        self.sideNavLayout.addWidget(self.hrSpacer, 2, 1)

        # Add Employee Button
        self.addEmployeeButton = qtw.QPushButton("Add", clicked = lambda: AddEmployee())
        self.buttonLayout.addWidget(self.addEmployeeButton)

        # Remove Employee Button
        self.removeEmployeeButton = qtw.QPushButton("Remove", clicked = lambda: RemoveEmployee())
        self.buttonLayout.addWidget(self.removeEmployeeButton)

        # Update Employee Button
        self.updateEmployeeButton = qtw.QPushButton("Update", clicked = lambda: UpdateEmployee())
        self.buttonLayout.addWidget(self.updateEmployeeButton)

        ##
        # Button Functions
        ##

        # @brief The AddEmployee() function calls the FuncUtil.directInput() function with the corresponding
        # function id. 'success' returns true based on server response
        def AddEmployee():
            FuncUtil.directInput("100", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()
        
        # @brief The RemoveEmployee() function calls the FuncUtil.directInput() function with the corresponding
        # function id. 'success' returns true based on server response
        def RemoveEmployee():
            FuncUtil.directInput("101", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()

        # @brief The UpdateEmployee() function calls the FuncUtil.directInput() function with the corresponding
        # function id. 'success' returns true based on server response
        def UpdateEmployee():
            FuncUtil.directInput("102", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()