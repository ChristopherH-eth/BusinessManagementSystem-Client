# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from GUI.dashboard import dashboard

##
# @file login.py
# @author 0xChristopher
# @brief
##

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        MainWindow.SetUI(self)

    # The SetUI() function sets the UI of the main window
    def SetUI(self):
        # Set window title
        self.setWindowTitle("Business Management System - Login")

        # Set central widget
        centralWidget = qtw.QWidget(self)
        self.setCentralWidget(centralWidget)

        # Set layouts
        outerLayout = qtw.QVBoxLayout()
        headerLayout = qtw.QVBoxLayout()
        inputFieldLayout = qtw.QFormLayout()
        buttonLayout = qtw.QGridLayout()

        outerLayout.addLayout(headerLayout)
        outerLayout.addLayout(inputFieldLayout)
        outerLayout.addLayout(buttonLayout)
        centralWidget.setLayout(outerLayout)
        self.setGeometry(950, 600, 800, 500)

        # Menu bar
        exitAction = qtw.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")

        menubar = self.menuBar()
        mFile = menubar.addMenu("&File")
        mFile.addAction(exitAction)

        # Welcome label
        welcomeLabel = qtw.QLabel("Welcome!\nPlease Login")
        welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        welcomeLabel.setAlignment(qtc.Qt.AlignCenter)
        headerLayout.addWidget(welcomeLabel)

        # Input fields
        inputFieldLayout.addRow("Username: ", qtw.QLineEdit())
        inputFieldLayout.addRow("Password: ", qtw.QLineEdit())

        # Buttons
        loginButton = qtw.QPushButton("Login", clicked = lambda: Login())
        buttonLayout.addWidget((loginButton), 0, 0)
        clockInButton = qtw.QPushButton("Clock In")
        buttonLayout.addWidget((clockInButton), 0, 1)
        clockOutButton = qtw.QPushButton("Clock Out")
        buttonLayout.addWidget((clockOutButton), 0, 2)

        # The Login() function attempts to log a user in
        def Login():
            self.hide()
            self.mw = dashboard
            self.mw.show()

        # Show application
        self.show()

app = qtw.QApplication([])
mw = MainWindow()