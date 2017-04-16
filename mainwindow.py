# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, 20, 40, 20)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.cartWidget = QtWidgets.QListWidget(self.centralWidget)
        self.cartWidget.setObjectName("cartWidget")
        self.gridLayout.addWidget(self.cartWidget, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        self.addButton = QtWidgets.QPushButton(self.centralWidget)
        self.addButton.setMinimumSize(QtCore.QSize(0, 30))
        self.addButton.setStyleSheet("font: 36pt \"Noto Sans\";")
        self.addButton.setFlat(True)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.availableWidget = QtWidgets.QListWidget(self.centralWidget)
        self.availableWidget.setObjectName("availableWidget")
        item = QtWidgets.QListWidgetItem()
        self.availableWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableWidget.addItem(item)
        self.gridLayout.addWidget(self.availableWidget, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.checkoutButton = QtWidgets.QPushButton(self.centralWidget)
        self.checkoutButton.setObjectName("checkoutButton")
        self.gridLayout.addWidget(self.checkoutButton, 5, 3, 1, 1, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Inventory Management System</span></p></body></html>"))
        self.addButton.setText(_translate("MainWindow", ">"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Available Items</span></p></body></html>"))
        __sortingEnabled = self.availableWidget.isSortingEnabled()
        self.availableWidget.setSortingEnabled(False)
        item = self.availableWidget.item(0)
        item.setText(_translate("MainWindow", "Arduino"))
        item = self.availableWidget.item(1)
        item.setText(_translate("MainWindow", "Diode"))
        item = self.availableWidget.item(2)
        item.setText(_translate("MainWindow", "Capacitor"))
        item = self.availableWidget.item(3)
        item.setText(_translate("MainWindow", "MOSFET"))
        item = self.availableWidget.item(4)
        item.setText(_translate("MainWindow", "Soldering Iron"))
        self.availableWidget.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Cart</span></p></body></html>"))
        self.checkoutButton.setText(_translate("MainWindow", "Checkout Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

