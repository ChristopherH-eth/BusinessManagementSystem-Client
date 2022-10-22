# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

##
# @file dashboard.py
# @author 0xChristopher
# @brief
##

class Dashboard():
    # The SetUI() function sets the UI of the dashboard window
    def SetUI(self, MainWindow):

        ##
        # Window layouts and attributes
        ##

        # Set window title
        MainWindow.setWindowTitle("Business Management System - Dashboard")

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