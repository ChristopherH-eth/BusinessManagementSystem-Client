# Imports
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from GUI.dashboard import Dashboard
from GUI.login import Login

class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.login = Login()
        self.dashboard = Dashboard()
        self.startLogin()

        # Menu bar
        exitAction = qtw.QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        mFile = menubar.addMenu("&File")
        mFile.addAction(exitAction)

    def startDashboard(self):
        self.dashboard.setupUI(self)
        self.dashboard.dashButton.clicked.connect(self.startDashboard)
        self.show()

    def startLogin(self):
        self.login.setupUI(self)
        self.login.loginButton.clicked.connect(self.startDashboard)
        self.show()

app = qtw.QApplication([])
mw = MainWindow()