# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(688, 283)
        font = QtGui.QFont()
        font.setPointSize(10)
        Widget.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Widget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGetTime = QtWidgets.QPushButton(self.groupBox_2)
        self.btnGetTime.setObjectName("btnGetTime")
        self.gridLayout.addWidget(self.btnGetTime, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setTime(QtCore.QTime(15, 30, 55))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 2)
        self.editTime = QtWidgets.QLineEdit(self.groupBox_2)
        self.editTime.setObjectName("editTime")
        self.gridLayout.addWidget(self.editTime, 1, 3, 1, 1)
        self.btnSetTime = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSetTime.setObjectName("btnSetTime")
        self.gridLayout.addWidget(self.btnSetTime, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QtCore.QDate(2016, 11, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 2, 1, 1)
        self.editDate = QtWidgets.QLineEdit(self.groupBox_2)
        self.editDate.setObjectName("editDate")
        self.gridLayout.addWidget(self.editDate, 3, 3, 1, 1)
        self.btnSetDate = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSetDate.setObjectName("btnSetDate")
        self.gridLayout.addWidget(self.btnSetDate, 4, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 10, 9), QtCore.QTime(8, 21, 28)))
        self.dateTimeEdit.setDate(QtCore.QDate(2018, 10, 9))
        self.dateTimeEdit.setTime(QtCore.QTime(8, 21, 28))
        self.dateTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(3000, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1763, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(1763, 9, 14))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateTimeEdit.setCalendarPopup(False)
        self.dateTimeEdit.setCurrentSectionIndex(0)
        self.dateTimeEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout.addWidget(self.dateTimeEdit, 5, 2, 1, 1)
        self.editDateTime = QtWidgets.QLineEdit(self.groupBox_2)
        self.editDateTime.setMinimumSize(QtCore.QSize(150, 0))
        self.editDateTime.setObjectName("editDateTime")
        self.gridLayout.addWidget(self.editDateTime, 5, 3, 1, 1)
        self.btnSetDateTime = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSetDateTime.setObjectName("btnSetDateTime")
        self.gridLayout.addWidget(self.btnSetDateTime, 6, 3, 1, 1)
        self.LabDateTime = QtWidgets.QLabel(self.groupBox_2)
        self.LabDateTime.setAlignment(QtCore.Qt.AlignCenter)
        self.LabDateTime.setObjectName("LabDateTime")
        self.gridLayout.addWidget(self.LabDateTime, 0, 3, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.editCalendar = QtWidgets.QLineEdit(self.groupBox_3)
        self.editCalendar.setObjectName("editCalendar")
        self.gridLayout_3.addWidget(self.editCalendar, 0, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_3)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_3.addWidget(self.calendarWidget, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Demo3_4 ????????????"))
        self.groupBox_2.setTitle(_translate("Widget", "????????????"))
        self.btnGetTime.setText(_translate("Widget", "????????????????????????"))
        self.label.setText(_translate("Widget", "???  ???"))
        self.timeEdit.setDisplayFormat(_translate("Widget", "HH:mm:ss"))
        self.editTime.setInputMask(_translate("Widget", "99:99:99;_"))
        self.btnSetTime.setText(_translate("Widget", "????????????"))
        self.label_2.setText(_translate("Widget", "???  ???"))
        self.dateEdit.setDisplayFormat(_translate("Widget", "yyyy???M???d???"))
        self.editDate.setInputMask(_translate("Widget", "9999-99-99"))
        self.btnSetDate.setText(_translate("Widget", "????????????"))
        self.label_3.setText(_translate("Widget", "????????????"))
        self.dateTimeEdit.setDisplayFormat(_translate("Widget", "yyyy-MM-dd HH:mm:ss"))
        self.editDateTime.setInputMask(_translate("Widget", "9999-99-99 99:99:99"))
        self.btnSetDateTime.setText(_translate("Widget", "??????????????????"))
        self.LabDateTime.setText(_translate("Widget", "???????????????"))
        self.groupBox_3.setTitle(_translate("Widget", "????????????"))
        self.label_5.setText(_translate("Widget", "??????????????????"))

