import sys
import json

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from mainwindow import Ui_MainWindow

class myApp(QMainWindow):
    def __init__(self, widget):
        super(myApp, self).__init__()
        widget.setWindowTitle("Inventory Management")
        Ui_MainWindow().setupUi(widget)

        checkoutButton = widget.findChild(QPushButton, "checkoutButton")
        addButton = widget.findChild(QPushButton, "addButton")
        self.availableWidget = widget.findChild(QListWidget, "availableWidget")
        self.cartWidget = widget.findChild(QListWidget, "cartWidget")

        addButton.clicked.connect(lambda: self.addItem())
        checkoutButton.clicked.connect(lambda: self.checkout())

    def addItem(self):
        self.cartWidget.addItem(self.availableWidget.selectedItems()[0].text())

    def checkout(self):
        checkoutString = ""
#        for item in self.cartWidget.items():
        i=0
        print (self.cartWidget.count())
        while(i<self.cartWidget.count()):
            checkoutString = checkoutString + self.cartWidget.item(i).text() + ", "
            i=i+1
        print (checkoutString)

def main():
    app = QApplication(sys.argv)
    widget = QMainWindow()
    prog = myApp(widget)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
