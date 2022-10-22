# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

##
# @file login.py
# @author 0xChristopher
# @brief
##

class Login():
    # The SetUI() function sets the UI of the main window
    def SetUI(self, MainWindow):
        # Set window title
        MainWindow.setWindowTitle("Business Management System - Login")

        # Set central widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Set layouts
        self.outerLayout = qtw.QVBoxLayout()
        self.headerLayout = qtw.QVBoxLayout()
        self.inputFieldLayout = qtw.QFormLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.inputFieldLayout)
        self.outerLayout.addLayout(self.buttonLayout)
        self.centralWidget.setLayout(self.outerLayout)

        # Window dimensions
        MainWindow.setGeometry(950, 600, 800, 500)

        # Welcome label
        self.welcomeLabel = qtw.QLabel("Welcome!\nPlease Login")
        self.welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        self.welcomeLabel.setAlignment(qtc.Qt.AlignCenter)
        self.headerLayout.addWidget(self.welcomeLabel)

        # Input fields
        self.inputFieldLayout.addRow("Username: ", qtw.QLineEdit())
        self.inputFieldLayout.addRow("Password: ", qtw.QLineEdit())

        # Buttons
        self.loginButton = qtw.QPushButton("Login")
        self.buttonLayout.addWidget((self.loginButton), 0, 0)
        self.clockInButton = qtw.QPushButton("Clock In")
        self.buttonLayout.addWidget((self.clockInButton), 0, 1)
        self.clockOutButton = qtw.QPushButton("Clock Out")
        self.buttonLayout.addWidget((self.clockOutButton), 0, 2)