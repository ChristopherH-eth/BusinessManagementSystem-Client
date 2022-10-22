# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

##
# @file login.py
# @author 0xChristopher
# @brief
##

class Login(object):
    # The SetUI() function sets the UI of the main window
    def setupUI(self, MainWindow):
        # Set window title
        MainWindow.setWindowTitle("Business Management System - Login")

        # Set central widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Set layouts
        outerLayout = qtw.QVBoxLayout()
        headerLayout = qtw.QVBoxLayout()
        inputFieldLayout = qtw.QFormLayout()
        buttonLayout = qtw.QGridLayout()

        outerLayout.addLayout(headerLayout)
        outerLayout.addLayout(inputFieldLayout)
        outerLayout.addLayout(buttonLayout)
        self.centralWidget.setLayout(outerLayout)
        MainWindow.setGeometry(950, 600, 800, 500)

        # Welcome label
        welcomeLabel = qtw.QLabel("Welcome!\nPlease Login")
        welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        welcomeLabel.setAlignment(qtc.Qt.AlignCenter)
        headerLayout.addWidget(welcomeLabel)

        # Input fields
        inputFieldLayout.addRow("Username: ", qtw.QLineEdit())
        inputFieldLayout.addRow("Password: ", qtw.QLineEdit())

        # Buttons
        self.loginButton = qtw.QPushButton("Login")
        buttonLayout.addWidget((self.loginButton), 0, 0)
        clockInButton = qtw.QPushButton("Clock In")
        buttonLayout.addWidget((clockInButton), 0, 1)
        clockOutButton = qtw.QPushButton("Clock Out")
        buttonLayout.addWidget((clockOutButton), 0, 2)

        # The Login() function attempts to log a user in
        # def Login():
        #     self.hide()
        #     self.mw = dashboard
        #     self.mw.show()

        # Show application
        MainWindow.show()