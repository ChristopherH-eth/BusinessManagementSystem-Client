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

        ##
        # Window Layouts and Attributes
        ##

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

        ##
        # Labels
        ##

        # Welcome Label
        self.welcomeLabel = qtw.QLabel("Welcome!\nPlease Login")
        self.welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        self.welcomeLabel.setAlignment(qtc.Qt.AlignCenter)

        ##
        # Input Fields
        ##

        # Login/Clock In and Out
        self.username = qtw.QLineEdit()
        self.password = qtw.QLineEdit()

        self.password.setEchoMode(qtw.QLineEdit.Password)           # Mask password field

        ##
        # Input Validators
        ##

        # Username
        usernameRX = qtc.QRegExp("^[A-Za-z0-9]{1,16}$")
        usernameVal = qtg.QRegExpValidator(usernameRX)
        self.username.setValidator(usernameVal)

        # Password
        passwordRX = qtc.QRegExp("^[A-Za-z0-9!#$&*.()]{1,16}$")
        passwordVal = qtg.QRegExpValidator(passwordRX)
        self.password.setValidator(passwordVal)

        ##
        # Buttons
        ##

        # Login
        self.loginButton = qtw.QPushButton("Login", clicked = lambda: Login())

        # Clock In
        self.clockInButton = qtw.QPushButton("Clock In")

        # Clock Out
        self.clockOutButton = qtw.QPushButton("Clock Out")

        ##
        # Build Window
        ##

        # Window Header
        self.headerLayout.addWidget(self.welcomeLabel)

        # Login Form
        self.inputFieldLayout.addRow("Username: ", self.username)
        self.inputFieldLayout.addRow("Password: ", self.password)

        # Login/Clock In and Out Buttons
        self.buttonLayout.addWidget((self.loginButton), 0, 0)
        self.buttonLayout.addWidget((self.clockInButton), 0, 1)
        self.buttonLayout.addWidget((self.clockOutButton), 0, 2)

        ##
        # Functions
        ##

        ## @brief The Login() function attempts to log in the current user
        def Login():
            log.logger.info("Executing Login() function")

            username = self.username.text()
            password = self.password.text()

            employee.Login(username, password)
            success = funcUtil.WaitForReply()

            if (success):
                newTcp.Receive()
            else:
                # Attempt to reconnect to the server on timeout
                log.logger.error("Host connection timeout")
                newTcp.Reconnect()

        # Clock in
        # Clock out