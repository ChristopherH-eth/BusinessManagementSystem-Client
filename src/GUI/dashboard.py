# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

##
# @file dashboard.py
# @author 0xChristopher
# @brief
##

class Dashboard(object):
    # The SetUI() function sets the UI of the dashboard window
    def setupUI(self, MainWindow):
        # Set window title
        MainWindow.setWindowTitle("Business Management System - Dashboard")

        # Set central widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

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
        self.centralWidget.setLayout(outerLayout)

        outerLayout.setAlignment(qtc.Qt.AlignTop)

        MainWindow.setGeometry(400, 200, 1800, 1500)

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
        self.dashButton = qtw.QPushButton("Dashboard")
        self.dashButton.setFixedWidth(250)
        sideNavLayout.addWidget(self.dashButton, 1, 0)
        sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        dashSpacer = qtw.QWidget()
        dashSpacer = qtw.QWidget().setFixedWidth(250)
        sideNavLayout.addWidget(dashSpacer, 1, 1)

        # HR Button
        self.hrButton = qtw.QPushButton("Human Resources")
        self.hrButton.setFixedWidth(250)
        sideNavLayout.addWidget(self.hrButton, 2, 0)
        sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        hrSpacer = qtw.QWidget()
        hrSpacer.setFixedWidth(250)
        sideNavLayout.addWidget(hrSpacer, 2, 1)

        ##
        # Button Functions
        ##

        # @brief The AddEmployee() function calls the FuncUtil.directInput() function with the corresponding
        # function id. 'success' returns true based on server response
        # def dashboard():
        #     self.hide()
        #     self.dashboard = dashboard
        #     self.dashboard.show()
        
        # def hr():
        #     self.hide()
        #     self.dashboard = humanResources
        #     self.dashboard.show()

        MainWindow.show()