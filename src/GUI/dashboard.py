# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from Util.funcUtil import FuncUtil
from Network.tcp import newTcp

##
# @file dashboard.py
# @author 0xChristopher
# @brief
##

class Dashboard(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Business Management System - Dashboard")

        # Set layout
        self.setLayout(qtw.QGridLayout())
        self.setGeometry(600, 400, 1000, 800)

        welcomeLabel = qtw.QLabel("Dashboard")
        welcomeLabel.setFont(qtg.QFont("Helvecta", 18))
        self.layout().addWidget(welcomeLabel)

        # Buttons
        addEmployeeButton = qtw.QPushButton("Add", clicked = lambda: AddEmployee())
        self.layout().addWidget(addEmployeeButton)
        removeEmployeeButton = qtw.QPushButton("Remove", clicked = lambda: RemoveEmployee())
        self.layout().addWidget(removeEmployeeButton)
        updateEmployeeButton = qtw.QPushButton("Update", clicked = lambda: UpdateEmployee())
        self.layout().addWidget(updateEmployeeButton)

        def AddEmployee():
            FuncUtil.directInput(True, "100", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()
        
        def RemoveEmployee():
            FuncUtil.directInput(True, "101", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()

        def UpdateEmployee():
            FuncUtil.directInput(True, "102", newTcp)
            success = FuncUtil.waitForReply()

            if (success):
                newTcp.receive()

app = qtw.QApplication([])
dashboard = Dashboard()