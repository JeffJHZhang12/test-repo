# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jeffjhzhang/pyabc/testx.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(206, 135)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btncancel = QtWidgets.QPushButton(self.centralwidget)
        self.btncancel.setGeometry(QtCore.QRect(124, 60, 51, 26))
        self.btncancel.setObjectName("btncancel")
        self.btnok = QtWidgets.QPushButton(self.centralwidget)
        self.btnok.setGeometry(QtCore.QRect(34, 60, 51, 26))
        self.btnok.setObjectName("btnok")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 166, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtname = QtWidgets.QLineEdit(self.widget)
        self.txtname.setObjectName("txtname")
        self.horizontalLayout.addWidget(self.txtname)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 206, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btncancel.setText(_translate("MainWindow", "Cancel"))
        self.btnok.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "??????:"))
