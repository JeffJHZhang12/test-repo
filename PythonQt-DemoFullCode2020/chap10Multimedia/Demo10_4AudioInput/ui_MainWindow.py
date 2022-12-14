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
        MainWindow.resize(476, 440)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_saveMode = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_saveMode.setObjectName("groupBox_saveMode")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_saveMode)
        self.horizontalLayout_3.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioSaveMode_Inner = QtWidgets.QRadioButton(self.groupBox_saveMode)
        self.radioSaveMode_Inner.setChecked(True)
        self.radioSaveMode_Inner.setObjectName("radioSaveMode_Inner")
        self.horizontalLayout_3.addWidget(self.radioSaveMode_Inner)
        self.radioSaveMode_QFile = QtWidgets.QRadioButton(self.groupBox_saveMode)
        self.radioSaveMode_QFile.setObjectName("radioSaveMode_QFile")
        self.horizontalLayout_3.addWidget(self.radioSaveMode_QFile)
        self.verticalLayout_3.addWidget(self.groupBox_saveMode)
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBoxDevice = QtWidgets.QGroupBox(self.splitter)
        self.groupBoxDevice.setObjectName("groupBoxDevice")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxDevice)
        self.verticalLayout_2.setContentsMargins(11, 5, 11, 5)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBoxDevice)
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboDevices = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboDevices.setObjectName("comboDevices")
        self.horizontalLayout.addWidget(self.comboDevices)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.groupBoxDevice)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.actualCodecLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualCodecLabel.setObjectName("actualCodecLabel")
        self.gridLayout.addWidget(self.actualCodecLabel, 0, 0, 1, 1)
        self.comboCodec = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboCodec.setObjectName("comboCodec")
        self.gridLayout.addWidget(self.comboCodec, 0, 1, 1, 1)
        self.actualFreqLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualFreqLabel.setObjectName("actualFreqLabel")
        self.gridLayout.addWidget(self.actualFreqLabel, 1, 0, 1, 1)
        self.comboSampleRate = QtWidgets.QComboBox(self.groupBoxDevice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboSampleRate.sizePolicy().hasHeightForWidth())
        self.comboSampleRate.setSizePolicy(sizePolicy)
        self.comboSampleRate.setObjectName("comboSampleRate")
        self.gridLayout.addWidget(self.comboSampleRate, 1, 1, 1, 1)
        self.actualChannelLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualChannelLabel.setObjectName("actualChannelLabel")
        self.gridLayout.addWidget(self.actualChannelLabel, 2, 0, 1, 1)
        self.comboChannels = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboChannels.setObjectName("comboChannels")
        self.gridLayout.addWidget(self.comboChannels, 2, 1, 1, 1)
        self.actualSampleTypeLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualSampleTypeLabel.setObjectName("actualSampleTypeLabel")
        self.gridLayout.addWidget(self.actualSampleTypeLabel, 3, 0, 1, 1)
        self.comboSampleTypes = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboSampleTypes.setObjectName("comboSampleTypes")
        self.gridLayout.addWidget(self.comboSampleTypes, 3, 1, 1, 1)
        self.actualSampleSizeLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualSampleSizeLabel.setObjectName("actualSampleSizeLabel")
        self.gridLayout.addWidget(self.actualSampleSizeLabel, 4, 0, 1, 1)
        self.comboSampleSizes = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboSampleSizes.setObjectName("comboSampleSizes")
        self.gridLayout.addWidget(self.comboSampleSizes, 4, 1, 1, 1)
        self.actualEndianLabel = QtWidgets.QLabel(self.groupBoxDevice)
        self.actualEndianLabel.setObjectName("actualEndianLabel")
        self.gridLayout.addWidget(self.actualEndianLabel, 5, 0, 1, 1)
        self.comboByteOrder = QtWidgets.QComboBox(self.groupBoxDevice)
        self.comboByteOrder.setObjectName("comboByteOrder")
        self.gridLayout.addWidget(self.comboByteOrder, 5, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.groupBoxDevice)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.groupBoxDevice)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_4 = QtWidgets.QFrame(self.groupBoxDevice)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabVol = QtWidgets.QLabel(self.groupBoxDevice)
        self.LabVol.setObjectName("LabVol")
        self.horizontalLayout_2.addWidget(self.LabVol)
        self.sliderVolumn = QtWidgets.QSlider(self.groupBoxDevice)
        self.sliderVolumn.setMaximum(100)
        self.sliderVolumn.setProperty("value", 90)
        self.sliderVolumn.setOrientation(QtCore.Qt.Horizontal)
        self.sliderVolumn.setObjectName("sliderVolumn")
        self.horizontalLayout_2.addWidget(self.sliderVolumn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_disp = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_disp.setObjectName("groupBox_disp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_disp)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progBar_Max = QtWidgets.QProgressBar(self.groupBox_disp)
        self.progBar_Max.setMaximum(256)
        self.progBar_Max.setProperty("value", 120)
        self.progBar_Max.setTextVisible(False)
        self.progBar_Max.setOrientation(QtCore.Qt.Vertical)
        self.progBar_Max.setObjectName("progBar_Max")
        self.gridLayout_2.addWidget(self.progBar_Max, 0, 0, 1, 1)
        self.progBar_Min = QtWidgets.QProgressBar(self.groupBox_disp)
        self.progBar_Min.setMaximum(256)
        self.progBar_Min.setProperty("value", 120)
        self.progBar_Min.setTextVisible(False)
        self.progBar_Min.setOrientation(QtCore.Qt.Vertical)
        self.progBar_Min.setObjectName("progBar_Min")
        self.gridLayout_2.addWidget(self.progBar_Min, 0, 1, 1, 1)
        self.progBar_Diff = QtWidgets.QProgressBar(self.groupBox_disp)
        self.progBar_Diff.setMaximum(256)
        self.progBar_Diff.setProperty("value", 120)
        self.progBar_Diff.setTextVisible(False)
        self.progBar_Diff.setOrientation(QtCore.Qt.Vertical)
        self.progBar_Diff.setObjectName("progBar_Diff")
        self.gridLayout_2.addWidget(self.progBar_Diff, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_disp)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_disp)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_disp)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_3 = QtWidgets.QFrame(self.groupBox_disp)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.LabBufferSize = QtWidgets.QLabel(self.groupBox_disp)
        self.LabBufferSize.setMinimumSize(QtCore.QSize(200, 0))
        self.LabBufferSize.setObjectName("LabBufferSize")
        self.verticalLayout.addWidget(self.LabBufferSize)
        self.LabBytesReady = QtWidgets.QLabel(self.groupBox_disp)
        self.LabBytesReady.setObjectName("LabBytesReady")
        self.verticalLayout.addWidget(self.LabBytesReady)
        self.LabBlockSize = QtWidgets.QLabel(self.groupBox_disp)
        self.LabBlockSize.setMinimumSize(QtCore.QSize(190, 0))
        self.LabBlockSize.setObjectName("LabBlockSize")
        self.verticalLayout.addWidget(self.LabBlockSize)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setIconSize(QtCore.QSize(16, 16))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actDeviceTest = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/22.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actDeviceTest.setIcon(icon)
        self.actDeviceTest.setObjectName("actDeviceTest")
        self.actStart = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/626.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actStart.setIcon(icon1)
        self.actStart.setObjectName("actStart")
        self.actStop = QtWidgets.QAction(MainWindow)
        self.actStop.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/624.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actStop.setIcon(icon2)
        self.actStop.setObjectName("actStop")
        self.actQuit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actQuit.setIcon(icon3)
        self.actQuit.setObjectName("actQuit")
        self.mainToolBar.addAction(self.actDeviceTest)
        self.mainToolBar.addAction(self.actStart)
        self.mainToolBar.addAction(self.actStop)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actQuit)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo10_4, QAudioInput??????????????????"))
        self.groupBox_saveMode.setTitle(_translate("MainWindow", "?????????????????????"))
        self.radioSaveMode_Inner.setToolTip(_translate("MainWindow", "strat()????????????????????????????????????IODevice????????????"))
        self.radioSaveMode_Inner.setText(_translate("MainWindow", "????????????IODevice"))
        self.radioSaveMode_QFile.setToolTip(_translate("MainWindow", "start(file)???????????????file?????????QFile??????"))
        self.radioSaveMode_QFile.setText(_translate("MainWindow", "??????QFile??????(test.raw)"))
        self.groupBoxDevice.setTitle(_translate("MainWindow", "???????????????????????????"))
        self.label.setText(_translate("MainWindow", "??????????????????"))
        self.actualCodecLabel.setText(_translate("MainWindow", "codec"))
        self.actualFreqLabel.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.actualChannelLabel.setText(_translate("MainWindow", "Channels"))
        self.actualSampleTypeLabel.setText(_translate("MainWindow", "SampleType"))
        self.actualSampleSizeLabel.setText(_translate("MainWindow", "Sample size (bits)"))
        self.actualEndianLabel.setText(_translate("MainWindow", "Endianness"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>???????????????????????????????????????????????????</p><p>8000Hz, 1 ?????????audio/pcm</p><p>8bits,UnSignedInt,LittleEndian</p></body></html>"))
        self.LabVol.setText(_translate("MainWindow", "????????????"))
        self.groupBox_disp.setTitle(_translate("MainWindow", "???????????????????????????"))
        self.label_3.setText(_translate("MainWindow", "?????????"))
        self.label_4.setText(_translate("MainWindow", "?????????"))
        self.label_5.setText(_translate("MainWindow", "??????"))
        self.LabBufferSize.setText(_translate("MainWindow", "QAudioInput.bufferSize()="))
        self.LabBytesReady.setText(_translate("MainWindow", "QAudioInput.bytesReady()="))
        self.LabBlockSize.setText(_translate("MainWindow", "IODevice??????????????????="))
        self.actDeviceTest.setText(_translate("MainWindow", "??????????????????"))
        self.actDeviceTest.setToolTip(_translate("MainWindow", "??????????????????"))
        self.actStart.setText(_translate("MainWindow", "??????"))
        self.actStart.setToolTip(_translate("MainWindow", "??????"))
        self.actStop.setText(_translate("MainWindow", "??????"))
        self.actStop.setToolTip(_translate("MainWindow", "??????"))
        self.actQuit.setText(_translate("MainWindow", "??????"))
        self.actQuit.setToolTip(_translate("MainWindow", "??????"))

import res_rc
