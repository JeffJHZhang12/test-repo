# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 449)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frameSetup = QtWidgets.QFrame(self.splitter)
        self.frameSetup.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frameSetup.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameSetup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSetup.setObjectName("frameSetup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameSetup)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frameSetup)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setContentsMargins(11, 5, 11, 5)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setIndent(10)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboTheme = QtWidgets.QComboBox(self.groupBox_4)
        self.comboTheme.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboTheme.setObjectName("comboTheme")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.comboTheme.addItem("")
        self.gridLayout_4.addWidget(self.comboTheme, 0, 1, 1, 1)
        self.chkBox_ShowPoints = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkBox_ShowPoints.setChecked(True)
        self.chkBox_ShowPoints.setObjectName("chkBox_ShowPoints")
        self.gridLayout_4.addWidget(self.chkBox_ShowPoints, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frameSetup)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 5, 11, 5)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setIndent(10)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinAngle_Min = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinAngle_Min.setMinimum(-3600)
        self.spinAngle_Min.setMaximum(3600)
        self.spinAngle_Min.setSingleStep(10)
        self.spinAngle_Min.setObjectName("spinAngle_Min")
        self.gridLayout.addWidget(self.spinAngle_Min, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setIndent(10)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.spinAngle_Max = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinAngle_Max.setMinimum(-3600)
        self.spinAngle_Max.setMaximum(3600)
        self.spinAngle_Max.setSingleStep(10)
        self.spinAngle_Max.setProperty("value", 360)
        self.spinAngle_Max.setObjectName("spinAngle_Max")
        self.gridLayout.addWidget(self.spinAngle_Max, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.spinAngle_Ticks = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinAngle_Ticks.setMinimum(4)
        self.spinAngle_Ticks.setMaximum(5000)
        self.spinAngle_Ticks.setProperty("value", 9)
        self.spinAngle_Ticks.setObjectName("spinAngle_Ticks")
        self.gridLayout.addWidget(self.spinAngle_Ticks, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frameSetup)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(11, 5, 11, 5)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(10)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinRadial_Max = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinRadial_Max.setMinimum(1)
        self.spinRadial_Max.setMaximum(500)
        self.spinRadial_Max.setProperty("value", 12)
        self.spinRadial_Max.setObjectName("spinRadial_Max")
        self.gridLayout_2.addWidget(self.spinRadial_Max, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setIndent(10)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.spinRadial_Ticks = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinRadial_Ticks.setMinimum(2)
        self.spinRadial_Ticks.setMaximum(100)
        self.spinRadial_Ticks.setProperty("value", 6)
        self.spinRadial_Ticks.setObjectName("spinRadial_Ticks")
        self.gridLayout_2.addWidget(self.spinRadial_Ticks, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.frameSetup)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(11, 5, 11, 5)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setIndent(10)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.spinRotate = QtWidgets.QSpinBox(self.groupBox)
        self.spinRotate.setMinimum(-180)
        self.spinRotate.setMaximum(180)
        self.spinRotate.setProperty("value", 90)
        self.spinRotate.setObjectName("spinRotate")
        self.gridLayout_3.addWidget(self.spinRotate, 1, 1, 1, 1)
        self.btnRotate = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/exec.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRotate.setIcon(icon)
        self.btnRotate.setObjectName("btnRotate")
        self.gridLayout_3.addWidget(self.btnRotate, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setIndent(10)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.spinCount = QtWidgets.QSpinBox(self.groupBox)
        self.spinCount.setMinimum(2)
        self.spinCount.setMaximum(100)
        self.spinCount.setProperty("value", 3)
        self.spinCount.setObjectName("spinCount")
        self.gridLayout_3.addWidget(self.spinCount, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 106, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frameChart = QtWidgets.QFrame(self.splitter)
        self.frameChart.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameChart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameChart.setObjectName("frameChart")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameChart)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chartView = QChartView(self.frameChart)
        self.chartView.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.chartView.setObjectName("chartView")
        self.verticalLayout_2.addWidget(self.chartView)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 637, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actZoomReset = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/414.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomReset.setIcon(icon1)
        self.actZoomReset.setObjectName("actZoomReset")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon2)
        self.actQuit.setObjectName("actQuit")
        self.actZoomIn = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/418.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomIn.setIcon(icon3)
        self.actZoomIn.setObjectName("actZoomIn")
        self.actZoomOut = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/416.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actZoomOut.setIcon(icon4)
        self.actZoomOut.setObjectName("actZoomOut")
        self.actRedraw = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/828.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actRedraw.setIcon(icon5)
        self.actRedraw.setObjectName("actRedraw")
        self.mainToolBar.addAction(self.actRedraw)
        self.mainToolBar.addAction(self.actZoomIn)
        self.mainToolBar.addAction(self.actZoomOut)
        self.mainToolBar.addAction(self.actZoomReset)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????"))
        self.groupBox_4.setTitle(_translate("MainWindow", "??????"))
        self.label_7.setText(_translate("MainWindow", "??????"))
        self.comboTheme.setToolTip(_translate("MainWindow", "??????????????????"))
        self.comboTheme.setItemText(0, _translate("MainWindow", "Light"))
        self.comboTheme.setItemText(1, _translate("MainWindow", "BlueCerulean"))
        self.comboTheme.setItemText(2, _translate("MainWindow", "Dark"))
        self.comboTheme.setItemText(3, _translate("MainWindow", "BrownSand"))
        self.comboTheme.setItemText(4, _translate("MainWindow", "BlueNcs"))
        self.comboTheme.setItemText(5, _translate("MainWindow", "HighContrast"))
        self.comboTheme.setItemText(6, _translate("MainWindow", "BlueIcy"))
        self.comboTheme.setItemText(7, _translate("MainWindow", "Qt"))
        self.chkBox_ShowPoints.setText(_translate("MainWindow", "???????????????"))
        self.groupBox_2.setTitle(_translate("MainWindow", "???????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????"))
        self.spinAngle_Min.setSuffix(_translate("MainWindow", "??"))
        self.label_4.setText(_translate("MainWindow", "?????????"))
        self.spinAngle_Max.setSuffix(_translate("MainWindow", "??"))
        self.label.setText(_translate("MainWindow", "???????????????"))
        self.groupBox_3.setTitle(_translate("MainWindow", "???????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.label_5.setText(_translate("MainWindow", "???????????????"))
        self.groupBox.setTitle(_translate("MainWindow", "????????????"))
        self.label_6.setText(_translate("MainWindow", "????????????"))
        self.spinRotate.setToolTip(_translate("MainWindow", "?????????????????????"))
        self.spinRotate.setSuffix(_translate("MainWindow", "??"))
        self.btnRotate.setText(_translate("MainWindow", "??????"))
        self.label_8.setText(_translate("MainWindow", "????????????"))
        self.actZoomReset.setText(_translate("MainWindow", "????????????"))
        self.actZoomReset.setToolTip(_translate("MainWindow", "????????????"))
        self.actQuit.setText(_translate("MainWindow", "??????"))
        self.actQuit.setToolTip(_translate("MainWindow", "??????"))
        self.actZoomIn.setText(_translate("MainWindow", "??????"))
        self.actZoomIn.setToolTip(_translate("MainWindow", "??????"))
        self.actZoomOut.setText(_translate("MainWindow", "??????"))
        self.actZoomOut.setToolTip(_translate("MainWindow", "??????"))
        self.actRedraw.setText(_translate("MainWindow", "??????????????????"))
        self.actRedraw.setToolTip(_translate("MainWindow", "??????????????????"))

from PyQt5.QtChart import QChartView
import res_rc
