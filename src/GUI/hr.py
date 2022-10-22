# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from Util.funcUtil import FuncUtil
from Network.tcp import newTcp

##
# @file dashboard.py
# @author 0xChristopher
# @brief
##

class HumanResources(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        HumanResources.SetUI(self)

    # The SetUI() function sets the UI of the dashboard window
    def SetUI(self):
        # Set window title
        self.setWindowTitle("Business Management System - Dashboard")

        # Set central widget
        centralWidget = qtw.QWidget(self)
        self.setCentralWidget(centralWidget)

        # Set layouts
        outerLayout = qtw.QVBoxLayout()
        headerLayout = qtw.QVBoxLayout()
        bodyLayout = qtw.QHBoxLayout()
        sideNavLayout = qtw.QGridLayout()
        buttonLayout = qtw.QGridLayout()

        outerLayout.addLayout(headerLayout)
        outerLayout.addLayout(bodyLayout)
        bodyLayout.addLayout(sideNavLayout)
        bodyLayout.addLayout(buttonLayout)
        centralWidget.setLayout(outerLayout)

        outerLayout.setAlignment(qtc.Qt.AlignTop)

        self.setGeometry(400, 200, 1800, 1500)

        # Menu bar
        exitAction = qtw.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        mFile = menubar.addMenu("&File")
        mFile.addAction(exitAction)

        ##
        # Labels 
        ##

        # Window Label
        windowLabel = qtw.QLabel("Dashboard")
        windowLabel.setFont(qtg.QFont("Helvecta", 18))
        windowLabel.setAlignment(qtc.Qt.AlignCenter)
        headerLayout.addWidget(windowLabel)
        windowSpacer = qtw.QWidget()
        windowSpacer.setFixedHeight(75)
        headerLayout.addWidget(windowSpacer)

        # Side Nav Label
        sideNavLabel = qtw.QLabel("Navigation")
        sideNavLabel.setFont(qtg.QFont("Helvecta", 10))
        sideNavLabel.setAlignment(qtc.Qt.AlignCenter)
        sideNavLabel.setFixedWidth(250)
        sideNavLayout.addWidget(sideNavLabel, 0, 0)

        ##
        # Buttons
        ##

        # Dashboard Button
        dashButton = qtw.QPushButton("Dashboard", clicked = lambda: dashboard())
        dashButton.setFixedWidth(250)
        sideNavLayout.addWidget(dashButton, 1, 0)
        sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        dashSpacer = qtw.QWidget()
        dashSpacer = qtw.QWidget().setFixedWidth(250)
        sideNavLayout.addWidget(dashSpacer, 1, 1)

        # HR Button
        hrButton = qtw.QPushButton("Human Resources", clicked = lambda: hr())
        hrButton.setFixedWidth(250)
        sideNavLayout.addWidget(hrButton, 2, 0)
        sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        hrSpacer = qtw.QWidget()
        hrSpacer.setFixedWidth(250)
        sideNavLayout.addWidget(hrSpacer, 2, 1)

        # Add Employee Button
        addEmployeeButton = qtw.QPushButton("Add", clicked = lambda: AddEmployee())
        buttonLayout.addWidget(addEmployeeButton)

        # Remove Employee Button
        removeEmployeeButton = qtw.QPushButton("Remove", clicked = lambda: RemoveEmployee())
        buttonLayout.addWidget(removeEmployeeButton)

        # Update Employee Button
        updateEmployeeButton = qtw.QPushButton("Update", clicked = lambda: UpdateEmployee())
        buttonLayout.addWidget(updateEmployeeButton)

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

        def dashboard():
            self.hide()
            self.humanResources = dashboard
            self.humanResources.show()

        def hr():
            self.hide()
            self.humanResources = humanResources
            self.humanResources.show()

app = qtw.QApplication([])
humanResources = HumanResources()