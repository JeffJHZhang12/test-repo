# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 314)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.frameButtons = QtWidgets.QFrame(self.centralWidget)
        self.frameButtons.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frameButtons.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameButtons)
        self.horizontalLayout.setContentsMargins(11, 2, 11, 2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpen = QtWidgets.QPushButton(self.frameButtons)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/001.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpen.setIcon(icon)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnPlay = QtWidgets.QPushButton(self.frameButtons)
        self.btnPlay.setEnabled(False)
        self.btnPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/620.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setObjectName("btnPlay")
        self.horizontalLayout.addWidget(self.btnPlay)
        self.btnPause = QtWidgets.QPushButton(self.frameButtons)
        self.btnPause.setEnabled(False)
        self.btnPause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/622.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.frameButtons)
        self.btnStop.setEnabled(False)
        self.btnStop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/624.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon3)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        spacerItem = QtWidgets.QSpacerItem(24, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSound = QtWidgets.QPushButton(self.frameButtons)
        self.btnSound.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/volumn.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSound.setIcon(icon4)
        self.btnSound.setFlat(True)
        self.btnSound.setObjectName("btnSound")
        self.horizontalLayout.addWidget(self.btnSound)
        self.sliderVolumn = QtWidgets.QSlider(self.frameButtons)
        self.sliderVolumn.setMaximum(100)
        self.sliderVolumn.setProperty("value", 100)
        self.sliderVolumn.setOrientation(QtCore.Qt.Horizontal)
        self.sliderVolumn.setObjectName("sliderVolumn")
        self.horizontalLayout.addWidget(self.sliderVolumn)
        self.btnText = QtWidgets.QPushButton(self.frameButtons)
        self.btnText.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/165.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnText.setIcon(icon5)
        self.btnText.setCheckable(True)
        self.btnText.setChecked(True)
        self.btnText.setObjectName("btnText")
        self.horizontalLayout.addWidget(self.btnText)
        self.btnZoomIn = QtWidgets.QPushButton(self.frameButtons)
        self.btnZoomIn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/418.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomIn.setIcon(icon6)
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.horizontalLayout.addWidget(self.btnZoomIn)
        self.btnZoomOut = QtWidgets.QPushButton(self.frameButtons)
        self.btnZoomOut.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/images/416.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnZoomOut.setIcon(icon7)
        self.btnZoomOut.setObjectName("btnZoomOut")
        self.horizontalLayout.addWidget(self.btnZoomOut)
        self.btnClose = QtWidgets.QPushButton(self.frameButtons)
        self.btnClose.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon8)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addWidget(self.frameButtons)
        self.frameProgress = QtWidgets.QFrame(self.centralWidget)
        self.frameProgress.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frameProgress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameProgress.setObjectName("frameProgress")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameProgress)
        self.horizontalLayout_2.setContentsMargins(11, 2, 11, 2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabCurMedia = QtWidgets.QLabel(self.frameProgress)
        self.LabCurMedia.setMinimumSize(QtCore.QSize(100, 0))
        self.LabCurMedia.setObjectName("LabCurMedia")
        self.horizontalLayout_2.addWidget(self.LabCurMedia)
        self.sliderPosition = QtWidgets.QSlider(self.frameProgress)
        self.sliderPosition.setTracking(False)
        self.sliderPosition.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPosition.setObjectName("sliderPosition")
        self.horizontalLayout_2.addWidget(self.sliderPosition)
        self.LabRatio = QtWidgets.QLabel(self.frameProgress)
        self.LabRatio.setMinimumSize(QtCore.QSize(80, 0))
        self.LabRatio.setObjectName("LabRatio")
        self.horizontalLayout_2.addWidget(self.LabRatio)
        self.verticalLayout.addWidget(self.frameProgress)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.btnClose.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo10_6, QGraphicsVideoItem ????????????"))
        self.btnOpen.setToolTip(_translate("MainWindow", "??????????????????"))
        self.btnPlay.setToolTip(_translate("MainWindow", "??????"))
        self.btnPause.setToolTip(_translate("MainWindow", "??????"))
        self.btnStop.setToolTip(_translate("MainWindow", "??????"))
        self.btnText.setToolTip(_translate("MainWindow", "????????????"))
        self.btnZoomIn.setToolTip(_translate("MainWindow", "??????"))
        self.btnZoomOut.setToolTip(_translate("MainWindow", "??????"))
        self.btnClose.setToolTip(_translate("MainWindow", "??????"))
        self.LabCurMedia.setText(_translate("MainWindow", "?????????"))
        self.LabRatio.setText(_translate("MainWindow", "??????"))

import res_rc
