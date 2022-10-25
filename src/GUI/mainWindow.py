# Imports
import PyQt5.QtWidgets as qtw

from GUI.dashboard import Dashboard
from GUI.login import Login
from GUI.hr import HumanResources
from Util.funcUtil import FuncUtil

'''
@file mainWindow.py
@author 0xChristopher
@brief This file handles the manipulation of the main window by changing what is displayed based
        on user input.
'''

class MainWindow(qtw.QMainWindow):
    ## @brief MainWindow constructor
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Initialize other windows
        self.login = Login()
        self.dashboard = Dashboard()
        self.hr = HumanResources()

        self.StartLogin()

        ##
        # Menu Bar
        ##

        # Logout action
        logoutAction = qtw.QAction("&Logout", self)
        logoutAction.setStatusTip("Logout of Application")

        # Shutdown Server action
        shutdownAction = qtw.QAction("&Shutdown Server", self)
        shutdownAction.setStatusTip("Shutdown the Server")
        shutdownAction.triggered.connect(self.Shutdown)

        # Exit action
        exitAction = qtw.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        # Create Menu Bar
        menubar = self.menuBar()
        mFile = menubar.addMenu("&File")
        mFile.addAction(logoutAction)
        mFile.addAction(shutdownAction)
        mFile.addAction(exitAction)

    ##
    # Functions
    ##

    ## @brief The StartLogin() function sets up and displays the Login window
    def StartLogin(self):
        self.login.SetUI(self)
        self.login.loginButton.clicked.connect(self.StartDashboard)
        self.show()

    ## @brief The StartDashboard() function sets up and displays the Dashboard window
    def StartDashboard(self):
        self.dashboard.SetUI(self)
        self.dashboard.dashButton.clicked.connect(self.StartDashboard)
        self.dashboard.hrButton.clicked.connect(self.StartHR)
        self.show()

    ## @brief The StartHR() function sets up and displays the HR window
    def StartHR(self):
        self.hr.SetUI(self)
        self.hr.dashButton.clicked.connect(self.StartDashboard)
        self.hr.hrButton.clicked.connect(self.StartHR)
        self.show()

    ## @brief The Shutdown() function shuts down the server
    def Shutdown(self):
        FuncUtil.DirectInput("shutdown")

# Initialize Main Window
app = qtw.QApplication([])
mw = MainWindow()