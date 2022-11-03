# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 567)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(11, 5, 11, 5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnFile = QtWidgets.QToolButton(self.groupBox_2)
        self.btnFile.setMinimumSize(QtCore.QSize(0, 22))
        self.btnFile.setObjectName("btnFile")
        self.horizontalLayout_3.addWidget(self.btnFile)
        self.editFilename = QtWidgets.QLineEdit(self.groupBox_2)
        self.editFilename.setObjectName("editFilename")
        self.horizontalLayout_3.addWidget(self.editFilename)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_LittleEndian = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_LittleEndian.setChecked(True)
        self.radio_LittleEndian.setObjectName("radio_LittleEndian")
        self.horizontalLayout.addWidget(self.radio_LittleEndian)
        self.radio_BigEndian = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_BigEndian.setObjectName("radio_BigEndian")
        self.horizontalLayout.addWidget(self.radio_BigEndian)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio_Single = QtWidgets.QRadioButton(self.groupBox_4)
        self.radio_Single.setChecked(True)
        self.radio_Single.setObjectName("radio_Single")
        self.horizontalLayout_2.addWidget(self.radio_Single)
        self.radio_Double = QtWidgets.QRadioButton(self.groupBox_4)
        self.radio_Double.setObjectName("radio_Double")
        self.horizontalLayout_2.addWidget(self.radio_Double)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_Double = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Double.setReadOnly(True)
        self.edit_Double.setObjectName("edit_Double")
        self.gridLayout.addWidget(self.edit_Double, 9, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.editQStr_In = QtWidgets.QLineEdit(self.groupBox)
        self.editQStr_In.setObjectName("editQStr_In")
        self.gridLayout.addWidget(self.editQStr_In, 10, 1, 1, 1)
        self.btnQStr_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnQStr_Write.setObjectName("btnQStr_Write")
        self.gridLayout.addWidget(self.btnQStr_Write, 10, 2, 1, 1)
        self.btnQStr_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnQStr_Read.setObjectName("btnQStr_Read")
        self.gridLayout.addWidget(self.btnQStr_Read, 10, 3, 1, 1)
        self.editQStr_Out = QtWidgets.QLineEdit(self.groupBox)
        self.editQStr_Out.setReadOnly(True)
        self.editQStr_Out.setObjectName("editQStr_Out")
        self.gridLayout.addWidget(self.editQStr_Out, 10, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.chkBox_In = QtWidgets.QCheckBox(self.groupBox)
        self.chkBox_In.setObjectName("chkBox_In")
        self.gridLayout.addWidget(self.chkBox_In, 7, 1, 1, 1)
        self.btnBool_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnBool_Write.setObjectName("btnBool_Write")
        self.gridLayout.addWidget(self.btnBool_Write, 7, 2, 1, 1)
        self.btnBool_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnBool_Read.setObjectName("btnBool_Read")
        self.gridLayout.addWidget(self.btnBool_Read, 7, 3, 1, 1)
        self.spin_UInt8 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_UInt8.setMinimum(-90000000)
        self.spin_UInt8.setMaximum(90000000)
        self.spin_UInt8.setProperty("value", 220)
        self.spin_UInt8.setObjectName("spin_UInt8")
        self.gridLayout.addWidget(self.spin_UInt8, 1, 1, 1, 1)
        self.spin_Int8 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_Int8.setMinimum(-1280000)
        self.spin_Int8.setMaximum(1270000)
        self.spin_Int8.setProperty("value", 56)
        self.spin_Int8.setObjectName("spin_Int8")
        self.gridLayout.addWidget(self.spin_Int8, 0, 1, 1, 1)
        self.btnInt8_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnInt8_Write.setObjectName("btnInt8_Write")
        self.gridLayout.addWidget(self.btnInt8_Write, 0, 2, 1, 1)
        self.edit_Int8 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Int8.setReadOnly(True)
        self.edit_Int8.setObjectName("edit_Int8")
        self.gridLayout.addWidget(self.edit_Int8, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnStr_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnStr_Read.setObjectName("btnStr_Read")
        self.gridLayout.addWidget(self.btnStr_Read, 11, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.spin_Float = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_Float.setDecimals(4)
        self.spin_Float.setMinimum(-60000000.0)
        self.spin_Float.setMaximum(600000000.0)
        self.spin_Float.setProperty("value", 15.26)
        self.spin_Float.setObjectName("spin_Float")
        self.gridLayout.addWidget(self.spin_Float, 8, 1, 1, 1)
        self.btnFloat_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnFloat_Write.setObjectName("btnFloat_Write")
        self.gridLayout.addWidget(self.btnFloat_Write, 8, 2, 1, 1)
        self.btnFloat_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnFloat_Read.setObjectName("btnFloat_Read")
        self.gridLayout.addWidget(self.btnFloat_Read, 8, 3, 1, 1)
        self.edit_Float = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Float.setReadOnly(True)
        self.edit_Float.setObjectName("edit_Float")
        self.gridLayout.addWidget(self.edit_Float, 8, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.spin_Double = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_Double.setDecimals(4)
        self.spin_Double.setMinimum(-600000000.0)
        self.spin_Double.setMaximum(600000000.0)
        self.spin_Double.setProperty("value", -56.253)
        self.spin_Double.setObjectName("spin_Double")
        self.gridLayout.addWidget(self.spin_Double, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_UInt8 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_UInt8.setReadOnly(True)
        self.edit_UInt8.setObjectName("edit_UInt8")
        self.gridLayout.addWidget(self.edit_UInt8, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.spin_Int16 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_Int16.setMinimum(-60000000)
        self.spin_Int16.setMaximum(60000000)
        self.spin_Int16.setProperty("value", -1522)
        self.spin_Int16.setObjectName("spin_Int16")
        self.gridLayout.addWidget(self.spin_Int16, 2, 1, 1, 1)
        self.btnFont_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnFont_Read.setObjectName("btnFont_Read")
        self.gridLayout.addWidget(self.btnFont_Read, 12, 3, 1, 1)
        self.editFont_Out = QtWidgets.QLineEdit(self.groupBox)
        self.editFont_Out.setReadOnly(False)
        self.editFont_Out.setObjectName("editFont_Out")
        self.gridLayout.addWidget(self.editFont_Out, 12, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 13, 0, 1, 1)
        self.btnColor_In = QtWidgets.QPushButton(self.groupBox)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.btnColor_In.setPalette(palette)
        self.btnColor_In.setObjectName("btnColor_In")
        self.gridLayout.addWidget(self.btnColor_In, 13, 1, 1, 1)
        self.btnColor_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnColor_Write.setObjectName("btnColor_Write")
        self.gridLayout.addWidget(self.btnColor_Write, 13, 2, 1, 1)
        self.btnColor_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnColor_Read.setObjectName("btnColor_Read")
        self.gridLayout.addWidget(self.btnColor_Read, 13, 3, 1, 1)
        self.editColor_Out = QtWidgets.QLineEdit(self.groupBox)
        self.editColor_Out.setReadOnly(False)
        self.editColor_Out.setObjectName("editColor_Out")
        self.gridLayout.addWidget(self.editColor_Out, 13, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.spin_Int32 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_Int32.setMinimum(-2147483647)
        self.spin_Int32.setMaximum(2147483647)
        self.spin_Int32.setProperty("value", -4294)
        self.spin_Int32.setObjectName("spin_Int32")
        self.gridLayout.addWidget(self.spin_Int32, 4, 1, 1, 1)
        self.btnInt32_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnInt32_Write.setObjectName("btnInt32_Write")
        self.gridLayout.addWidget(self.btnInt32_Write, 4, 2, 1, 1)
        self.btnInt32_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnInt32_Read.setObjectName("btnInt32_Read")
        self.gridLayout.addWidget(self.btnInt32_Read, 4, 3, 1, 1)
        self.edit_Int32 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Int32.setReadOnly(True)
        self.edit_Int32.setObjectName("edit_Int32")
        self.gridLayout.addWidget(self.edit_Int32, 4, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.spin_Int64 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_Int64.setMinimum(-2147483647)
        self.spin_Int64.setMaximum(2147483647)
        self.spin_Int64.setProperty("value", 25465)
        self.spin_Int64.setObjectName("spin_Int64")
        self.gridLayout.addWidget(self.spin_Int64, 5, 1, 1, 1)
        self.btnInt64_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnInt64_Write.setObjectName("btnInt64_Write")
        self.gridLayout.addWidget(self.btnInt64_Write, 5, 2, 1, 1)
        self.btnInt8_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnInt8_Read.setObjectName("btnInt8_Read")
        self.gridLayout.addWidget(self.btnInt8_Read, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.btnFont_In = QtWidgets.QPushButton(self.groupBox)
        self.btnFont_In.setObjectName("btnFont_In")
        self.gridLayout.addWidget(self.btnFont_In, 12, 1, 1, 1)
        self.btnFont_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnFont_Write.setObjectName("btnFont_Write")
        self.gridLayout.addWidget(self.btnFont_Write, 12, 2, 1, 1)
        self.btnDouble_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnDouble_Write.setObjectName("btnDouble_Write")
        self.gridLayout.addWidget(self.btnDouble_Write, 9, 2, 1, 1)
        self.btnDouble_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnDouble_Read.setObjectName("btnDouble_Read")
        self.gridLayout.addWidget(self.btnDouble_Read, 9, 3, 1, 1)
        self.editStr_Out = QtWidgets.QLineEdit(self.groupBox)
        self.editStr_Out.setObjectName("editStr_Out")
        self.gridLayout.addWidget(self.editStr_Out, 11, 4, 1, 1)
        self.editStr_In = QtWidgets.QLineEdit(self.groupBox)
        self.editStr_In.setObjectName("editStr_In")
        self.gridLayout.addWidget(self.editStr_In, 11, 1, 1, 1)
        self.btnInt64_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnInt64_Read.setObjectName("btnInt64_Read")
        self.gridLayout.addWidget(self.btnInt64_Read, 5, 3, 1, 1)
        self.edit_Int64 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Int64.setReadOnly(True)
        self.edit_Int64.setObjectName("edit_Int64")
        self.gridLayout.addWidget(self.edit_Int64, 5, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.spin_Int = QtWidgets.QSpinBox(self.groupBox)
        self.spin_Int.setMinimum(-2147483647)
        self.spin_Int.setMaximum(2147483647)
        self.spin_Int.setProperty("value", 5658)
        self.spin_Int.setObjectName("spin_Int")
        self.gridLayout.addWidget(self.spin_Int, 6, 1, 1, 1)
        self.btnInt_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnInt_Write.setObjectName("btnInt_Write")
        self.gridLayout.addWidget(self.btnInt_Write, 6, 2, 1, 1)
        self.btnInt_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnInt_Read.setObjectName("btnInt_Read")
        self.gridLayout.addWidget(self.btnInt_Read, 6, 3, 1, 1)
        self.edit_Int = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Int.setReadOnly(True)
        self.edit_Int.setObjectName("edit_Int")
        self.gridLayout.addWidget(self.edit_Int, 6, 4, 1, 1)
        self.btnUInt8_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnUInt8_Write.setObjectName("btnUInt8_Write")
        self.gridLayout.addWidget(self.btnUInt8_Write, 1, 2, 1, 1)
        self.btnUInt8_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnUInt8_Read.setObjectName("btnUInt8_Read")
        self.gridLayout.addWidget(self.btnUInt8_Read, 1, 3, 1, 1)
        self.btnInt16_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnInt16_Write.setObjectName("btnInt16_Write")
        self.gridLayout.addWidget(self.btnInt16_Write, 2, 2, 1, 1)
        self.btnInt16_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnInt16_Read.setObjectName("btnInt16_Read")
        self.gridLayout.addWidget(self.btnInt16_Read, 2, 3, 1, 1)
        self.edit_Int16 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_Int16.setReadOnly(True)
        self.edit_Int16.setObjectName("edit_Int16")
        self.gridLayout.addWidget(self.edit_Int16, 2, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.spin_UInt16 = QtWidgets.QSpinBox(self.groupBox)
        self.spin_UInt16.setMinimum(-900000000)
        self.spin_UInt16.setMaximum(900000000)
        self.spin_UInt16.setProperty("value", 65222)
        self.spin_UInt16.setObjectName("spin_UInt16")
        self.gridLayout.addWidget(self.spin_UInt16, 3, 1, 1, 1)
        self.btnUInt16_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnUInt16_Write.setObjectName("btnUInt16_Write")
        self.gridLayout.addWidget(self.btnUInt16_Write, 3, 2, 1, 1)
        self.btnUIn16_Read = QtWidgets.QPushButton(self.groupBox)
        self.btnUIn16_Read.setObjectName("btnUIn16_Read")
        self.gridLayout.addWidget(self.btnUIn16_Read, 3, 3, 1, 1)
        self.edit_UInt16 = QtWidgets.QLineEdit(self.groupBox)
        self.edit_UInt16.setReadOnly(True)
        self.edit_UInt16.setObjectName("edit_UInt16")
        self.gridLayout.addWidget(self.edit_UInt16, 3, 4, 1, 1)
        self.chkBox_Out = QtWidgets.QCheckBox(self.groupBox)
        self.chkBox_Out.setObjectName("chkBox_Out")
        self.gridLayout.addWidget(self.chkBox_Out, 7, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 11, 0, 1, 1)
        self.btnStr_Write = QtWidgets.QPushButton(self.groupBox)
        self.btnStr_Write.setObjectName("btnStr_Write")
        self.gridLayout.addWidget(self.btnStr_Write, 11, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralWidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actClearOutput = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/214.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actClearOutput.setIcon(icon)
        self.actClearOutput.setObjectName("actClearOutput")
        self.actClose = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actClose.setIcon(icon1)
        self.actClose.setObjectName("actClose")
        self.actSaveALL = QtWidgets.QAction(MainWindow)
        self.actSaveALL.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/saveall1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actSaveALL.setIcon(icon2)
        self.actSaveALL.setObjectName("actSaveALL")
        self.actReadALL = QtWidgets.QAction(MainWindow)
        self.actReadALL.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/upfold1.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actReadALL.setIcon(icon3)
        self.actReadALL.setObjectName("actReadALL")
        self.toolBar.addAction(self.actClearOutput)
        self.toolBar.addAction(self.actSaveALL)
        self.toolBar.addAction(self.actReadALL)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actClose)

        self.retranslateUi(MainWindow)
        self.actClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo9_2， 二进制文件流化读写"))
        self.btnFile.setText(_translate("MainWindow", "测试用文件"))
        self.groupBox_3.setTitle(_translate("MainWindow", "字节序"))
        self.radio_LittleEndian.setText(_translate("MainWindow", "LittleEndian"))
        self.radio_BigEndian.setText(_translate("MainWindow", "BigEndian"))
        self.groupBox_4.setTitle(_translate("MainWindow", "浮点数精度"))
        self.radio_Single.setText(_translate("MainWindow", "SinglePrecision"))
        self.radio_Double.setText(_translate("MainWindow", "DoublePrecision"))
        self.groupBox.setTitle(_translate("MainWindow", "流编码方式读写测试"))
        self.label_13.setText(_translate("MainWindow", "QString"))
        self.editQStr_In.setText(_translate("MainWindow", "Hello"))
        self.btnQStr_Write.setText(_translate("MainWindow", "写入"))
        self.btnQStr_Read.setText(_translate("MainWindow", "读出"))
        self.label_10.setText(_translate("MainWindow", "Bool"))
        self.chkBox_In.setText(_translate("MainWindow", "布尔值"))
        self.btnBool_Write.setText(_translate("MainWindow", "写入"))
        self.btnBool_Read.setText(_translate("MainWindow", "读出"))
        self.btnInt8_Write.setText(_translate("MainWindow", "写入"))
        self.label.setText(_translate("MainWindow", "Int8(-128~127)"))
        self.btnStr_Read.setText(_translate("MainWindow", "读出"))
        self.label_11.setText(_translate("MainWindow", "Float"))
        self.btnFloat_Write.setText(_translate("MainWindow", "写入"))
        self.btnFloat_Read.setText(_translate("MainWindow", "读出"))
        self.label_12.setText(_translate("MainWindow", "Double"))
        self.label_2.setText(_translate("MainWindow", "UInt8(0~255)"))
        self.label_4.setText(_translate("MainWindow", "Int16(-32768~32767)"))
        self.btnFont_Read.setText(_translate("MainWindow", "读出"))
        self.editFont_Out.setText(_translate("MainWindow", "字体"))
        self.label_16.setText(_translate("MainWindow", "QVariant"))
        self.btnColor_In.setText(_translate("MainWindow", "选择颜色"))
        self.btnColor_Write.setText(_translate("MainWindow", "写入"))
        self.btnColor_Read.setText(_translate("MainWindow", "读出"))
        self.editColor_Out.setText(_translate("MainWindow", "颜色"))
        self.label_6.setText(_translate("MainWindow", "Int32"))
        self.btnInt32_Write.setText(_translate("MainWindow", "写入"))
        self.btnInt32_Read.setText(_translate("MainWindow", "读出"))
        self.label_7.setText(_translate("MainWindow", "Int64"))
        self.btnInt64_Write.setText(_translate("MainWindow", "写入"))
        self.btnInt8_Read.setText(_translate("MainWindow", "读出"))
        self.label_15.setText(_translate("MainWindow", "QVariant"))
        self.btnFont_In.setText(_translate("MainWindow", "选择字体"))
        self.btnFont_Write.setText(_translate("MainWindow", "写入"))
        self.btnDouble_Write.setText(_translate("MainWindow", "写入"))
        self.btnDouble_Read.setText(_translate("MainWindow", "读出"))
        self.editStr_In.setText(_translate("MainWindow", "Hello"))
        self.btnInt64_Read.setText(_translate("MainWindow", "读出"))
        self.label_8.setText(_translate("MainWindow", "Int(=Int32)"))
        self.btnInt_Write.setText(_translate("MainWindow", "写入"))
        self.btnInt_Read.setText(_translate("MainWindow", "读出"))
        self.btnUInt8_Write.setText(_translate("MainWindow", "写入"))
        self.btnUInt8_Read.setText(_translate("MainWindow", "读出"))
        self.btnInt16_Write.setText(_translate("MainWindow", "写入"))
        self.btnInt16_Read.setText(_translate("MainWindow", "读出"))
        self.label_5.setText(_translate("MainWindow", "UInt16(0~65535)"))
        self.btnUInt16_Write.setText(_translate("MainWindow", "写入"))
        self.btnUIn16_Read.setText(_translate("MainWindow", "读出"))
        self.chkBox_Out.setText(_translate("MainWindow", "布尔值"))
        self.label_3.setText(_translate("MainWindow", "String"))
        self.btnStr_Write.setText(_translate("MainWindow", "写入"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actClearOutput.setText(_translate("MainWindow", "读出编辑框全清空"))
        self.actClearOutput.setToolTip(_translate("MainWindow", "读出编辑框全清空"))
        self.actClose.setText(_translate("MainWindow", "退出"))
        self.actSaveALL.setText(_translate("MainWindow", "连续写入文件"))
        self.actSaveALL.setToolTip(_translate("MainWindow", "连续写入文件"))
        self.actReadALL.setText(_translate("MainWindow", "连续从文件读取"))
        self.actReadALL.setToolTip(_translate("MainWindow", "连续从文件读取"))


import res_rc
