import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
 
class App(QMainWindow):
 
    def __init__(self):
        super(App, self).__init__()
        self.title = 'LoadCentral.konek.it'
        self.left = 400
        self.top = 400
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('Phone Number', self)
        label.move(20,10)
        label.resize(280, 30)
        label.setFont(QFont('Arial', 13))

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 40)
        self.textbox.resize(280,30)
        self.textbox.setFont(QFont('Arial', 13))

        self.dropbox = QComboBox(self)
        self.dropbox.move(20,80)
        self.dropbox.resize(280,30)
        data = {'Globe','Smart','Sun'}
        for i in data:
        	self.dropbox.addItem(i)
        self.dropbox.setFont(QFont('Arial', 13))

        button = QPushButton('Confirm && Load', self)
        button.move(141,130) 
        button.resize(160, 30)
        button.setFont(QFont('Arial', 13))
        button.clicked.connect(self.on_click)

        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())