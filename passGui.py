import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import passGen as pg
import pyperclip

class passGui(QtWidgets.QMainWindow):
    def __init__(self):
        super(passGui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('passGui.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.initButtons()
        self.initWidgets()

    def initButtons(self):
        self.resbtn.clicked.connect(self.reset)
        self.genbtn.clicked.connect(self.genPass)
        self.copybtn.clicked.connect(self.copyPass)

    def initWidgets(self):
        self.passlen.setRange(5,50)
        self.spilen.addItems(['1','2','3'])
        self.caplen.addItems(['1','2','3'])
        self.cplbl.hide()

    def reset(self):
        self.initWidgets()
        self.passview.setText("")

    def copyPass(self):
        pyperclip.copy(self.passview.text())
        self.cplbl.show()
        QTimer.singleShot(1200,self.cplbl.hide)

    def genPass(self):
        password=pg.createPassword(int(self.passlen.value()),int(self.spilen.currentText()),int(self.caplen.currentText()))
        self.passview.setText(password)

app = QtWidgets.QApplication(sys.argv)
window = passGui()
app.exec_()