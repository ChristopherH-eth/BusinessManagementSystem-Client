# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

from Network.tcp import newTcp
from Util.funcUtil import funcUtil
from Log.log import log
from HR.employee import employee

'''
@file login.py
@author 0xChristopher
@brief This file defines how the UI will be set up for the login window.
'''

class Login():
    ## @brief The SetUI() function sets the UI of the main window
    def SetUI(self, MainWindow):
        # Set Window Title
        MainWindow.setWindowTitle("Business Management System - Login")

        # Set Central Widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Set Layouts
        self.outerLayout = qtw.QVBoxLayout()
        self.headerLayout = qtw.QVBoxLayout()
        self.inputFieldLayout = qtw.QFormLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.inputFieldLayout)
        self.outerLayout.addLayout(self.buttonLayout)
        self.centralWidget.setLayout(self.outerLayout)

        # Window Dimensions
        MainWindow.setGeometry(950, 600, 800, 500)

        # Welcome Label
        self.welcomeLabel = qtw.QLabel("Welcome!\nPlease Login")
        self.welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        self.welcomeLabel.setAlignment(qtc.Qt.AlignCenter)
        self.headerLayout.addWidget(self.welcomeLabel)

        # Input Fields
        self.username = qtw.QLineEdit()
        self.password = qtw.QLineEdit()

        self.password.setEchoMode(qtw.QLineEdit.Password)           # Mask password field

        self.inputFieldLayout.addRow("Username: ", self.username)
        self.inputFieldLayout.addRow("Password: ", self.password)

        # Buttons
        self.loginButton = qtw.QPushButton("Login", clicked = lambda: Login())
        self.buttonLayout.addWidget((self.loginButton), 0, 0)
        self.clockInButton = qtw.QPushButton("Clock In")
        self.buttonLayout.addWidget((self.clockInButton), 0, 1)
        self.clockOutButton = qtw.QPushButton("Clock Out")
        self.buttonLayout.addWidget((self.clockOutButton), 0, 2)

        ##
        # Functions
        ##

        ## @brief The Login() function attempts to log in the current user
        def Login():
            log.logger.info("Executing Login() function")

            username = self.username.text()
            password = self.password.text()

            newTcp.Connect() # Make sure we're still connected to the server
            employee.Login(username, password)
            success = funcUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                log.logger.error("Host connection timeout")

        # Clock in
        # Clock out