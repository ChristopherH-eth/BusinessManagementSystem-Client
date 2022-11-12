# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

'''
@file dashboard.py
@author 0xChristopher
@brief This file defines how the UI will be set up for the dashboard window.
'''

class Dashboard():
    ## @brief The SetUI() function sets the UI of the dashboard window
    def SetUI(self, MainWindow):

        ##
        # Window Layouts and Attributes
        ##

        # Set Window Title
        MainWindow.setWindowTitle("Business Management System - Dashboard")

        # Set Central Widget
        self.centralWidget = qtw.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        # Set Layouts
        self.outerLayout = qtw.QVBoxLayout()
        self.headerLayout = qtw.QVBoxLayout()
        self.bodyLayout = qtw.QHBoxLayout()
        self.innerBodyLayout = qtw.QVBoxLayout()
        self.welcomeUpdate = qtw.QVBoxLayout()
        self.sideNavLayout = qtw.QGridLayout()
        self.buttonLayout = qtw.QGridLayout()

        self.outerLayout.addLayout(self.headerLayout)
        self.outerLayout.addLayout(self.bodyLayout)
        self.bodyLayout.addLayout(self.sideNavLayout)
        self.bodyLayout.addLayout(self.innerBodyLayout)
        self.innerBodyLayout.addLayout(self.welcomeUpdate)
        self.innerBodyLayout.addLayout(self.buttonLayout)
        self.centralWidget.setLayout(self.outerLayout)

        self.outerLayout.setAlignment(qtc.Qt.AlignTop)
        self.bodyLayout.setAlignment(qtc.Qt.AlignTop)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.innerBodyLayout.setAlignment(qtc.Qt.AlignTop)

        # Window Dimensions
        MainWindow.setGeometry(400, 200, 1800, 1500)

        ##
        # Labels 
        ##

        # Window Label
        self.windowLabel = qtw.QLabel("Dashboard")
        self.windowLabel.setFont(qtg.QFont("Helvecta", 18))
        self.windowLabel.setAlignment(qtc.Qt.AlignCenter)
        self.windowSpacer = qtw.QWidget()
        self.windowSpacer.setFixedHeight(75)

        # Side Nav Label
        self.sideNavLabel = qtw.QLabel("Navigation")
        self.sideNavLabel.setFont(qtg.QFont("Helvecta", 10))
        self.sideNavLabel.setAlignment(qtc.Qt.AlignCenter)
        self.sideNavLabel.setFixedWidth(250)
        self.sideNavSpacer = qtw.QWidget()
        self.sideNavSpacer.setFixedHeight(25)

        # Welcome Label
        self.welcomeLabel = qtw.QLabel("Welcome!")
        self.welcomeLabel.setFont(qtg.QFont("Helvecta", 16))
        self.welcomeLabel.setFixedWidth(1250)
        self.welcomeSpacer = qtw.QWidget()
        self.welcomeSpacer.setFixedHeight(25)

        # Update Label
        self.updateLabel = qtw.QLabel("This is where updates will show up!")
        self.updateLabel.setFont(qtg.QFont("Helvecta", 10))
        self.updateLabel.setFixedWidth(1250)

        ##
        # Buttons
        ##

        # Dashboard Button
        self.dashButton = qtw.QPushButton("Dashboard")
        self.dashButton.setFixedWidth(250)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.dashSpacer = qtw.QWidget()
        self.dashSpacer.setFixedWidth(250)

        # HR Button
        self.hrButton = qtw.QPushButton("Human Resources")
        self.hrButton.setFixedWidth(250)
        self.sideNavLayout.setAlignment(qtc.Qt.AlignTop)
        self.hrSpacer = qtw.QWidget()
        self.hrSpacer.setFixedWidth(250)

        ##
        # Build Window
        ##

        # Window Header
        self.headerLayout.addWidget(self.windowLabel)
        self.headerLayout.addWidget(self.windowSpacer)

        # Side Nav
        self.sideNavLayout.addWidget(self.sideNavLabel, 0, 0)
        self.sideNavLayout.addWidget(self.sideNavSpacer, 1, 0)
        self.sideNavLayout.addWidget(self.dashButton, 2, 0)
        self.sideNavLayout.addWidget(self.dashSpacer, 2, 1)
        self.sideNavLayout.addWidget(self.hrButton, 3, 0)
        self.sideNavLayout.addWidget(self.hrSpacer, 3, 1)

        # Body
        self.welcomeUpdate.addWidget(self.welcomeLabel)
        self.welcomeUpdate.addWidget(self.welcomeSpacer)
        self.welcomeUpdate.addWidget(self.updateLabel)