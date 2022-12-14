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
        MainWindow.resize(896, 530)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolBox = QtWidgets.QToolBox(self.splitter)
        self.toolBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolBox.setObjectName("toolBox")
        self.pageFile = QtWidgets.QWidget()
        self.pageFile.setGeometry(QtCore.QRect(0, 0, 296, 390))
        self.pageFile.setObjectName("pageFile")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pageFile)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_10 = QtWidgets.QGroupBox(self.pageFile)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.btnFile_exists = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_exists.setObjectName("btnFile_exists")
        self.verticalLayout_11.addWidget(self.btnFile_exists)
        self.btnFile_copy = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_copy.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_copy.setObjectName("btnFile_copy")
        self.verticalLayout_11.addWidget(self.btnFile_copy)
        self.btnFile_remove = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_remove.setObjectName("btnFile_remove")
        self.verticalLayout_11.addWidget(self.btnFile_remove)
        self.btnFile_rename = QtWidgets.QPushButton(self.groupBox_10)
        self.btnFile_rename.setMinimumSize(QtCore.QSize(0, 30))
        self.btnFile_rename.setObjectName("btnFile_rename")
        self.verticalLayout_11.addWidget(self.btnFile_rename)
        self.btnFile_copy.raise_()
        self.btnFile_remove.raise_()
        self.btnFile_rename.raise_()
        self.btnFile_exists.raise_()
        self.verticalLayout_8.addWidget(self.groupBox_10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/804.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageFile, icon, "")
        self.pageFileInfo = QtWidgets.QWidget()
        self.pageFileInfo.setGeometry(QtCore.QRect(0, 0, 327, 373))
        self.pageFileInfo.setObjectName("pageFileInfo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageFileInfo)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.pageFileInfo)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setContentsMargins(5, 3, 5, 3)
        self.gridLayout_4.setHorizontalSpacing(5)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnInfo_baseName = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_baseName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_baseName.setObjectName("btnInfo_baseName")
        self.gridLayout_4.addWidget(self.btnInfo_baseName, 3, 0, 1, 1)
        self.btnInfo_absPath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_absPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_absPath.setObjectName("btnInfo_absPath")
        self.gridLayout_4.addWidget(self.btnInfo_absPath, 0, 1, 1, 1)
        self.btnInfo_absFilePath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_absFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_absFilePath.setObjectName("btnInfo_absFilePath")
        self.gridLayout_4.addWidget(self.btnInfo_absFilePath, 0, 0, 1, 1)
        self.btnInfo_baseName2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_baseName2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_baseName2.setObjectName("btnInfo_baseName2")
        self.gridLayout_4.addWidget(self.btnInfo_baseName2, 3, 1, 1, 1)
        self.btnInfo_isDir = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isDir.setObjectName("btnInfo_isDir")
        self.gridLayout_4.addWidget(self.btnInfo_isDir, 6, 0, 1, 1)
        self.btnInfo_isFile = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isFile.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isFile.setObjectName("btnInfo_isFile")
        self.gridLayout_4.addWidget(self.btnInfo_isFile, 6, 1, 1, 1)
        self.btnInfo_isExec = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_isExec.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_isExec.setObjectName("btnInfo_isExec")
        self.gridLayout_4.addWidget(self.btnInfo_isExec, 7, 0, 1, 1)
        self.btnInfo_lastModified = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_lastModified.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_lastModified.setObjectName("btnInfo_lastModified")
        self.gridLayout_4.addWidget(self.btnInfo_lastModified, 8, 0, 1, 1)
        self.btnInfo_lastRead = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_lastRead.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_lastRead.setObjectName("btnInfo_lastRead")
        self.gridLayout_4.addWidget(self.btnInfo_lastRead, 8, 1, 1, 1)
        self.btnInfo_fileName = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_fileName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_fileName.setObjectName("btnInfo_fileName")
        self.gridLayout_4.addWidget(self.btnInfo_fileName, 1, 0, 1, 1)
        self.btnInfo_exists2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_exists2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_exists2.setObjectName("btnInfo_exists2")
        self.gridLayout_4.addWidget(self.btnInfo_exists2, 10, 1, 1, 1)
        self.btnInfo_suffix = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_suffix.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_suffix.setObjectName("btnInfo_suffix")
        self.gridLayout_4.addWidget(self.btnInfo_suffix, 4, 0, 1, 1)
        self.btnInfo_exists = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_exists.setObjectName("btnInfo_exists")
        self.gridLayout_4.addWidget(self.btnInfo_exists, 10, 0, 1, 1)
        self.btnInfo_suffix2 = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_suffix2.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_suffix2.setObjectName("btnInfo_suffix2")
        self.gridLayout_4.addWidget(self.btnInfo_suffix2, 4, 1, 1, 1)
        self.btnInfo_filePath = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_filePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_filePath.setObjectName("btnInfo_filePath")
        self.gridLayout_4.addWidget(self.btnInfo_filePath, 1, 1, 1, 1)
        self.btnInfo_path = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_path.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_path.setObjectName("btnInfo_path")
        self.gridLayout_4.addWidget(self.btnInfo_path, 2, 1, 1, 1)
        self.btnInfo_size = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_size.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_size.setObjectName("btnInfo_size")
        self.gridLayout_4.addWidget(self.btnInfo_size, 2, 0, 1, 1)
        self.btnInfo_birthTime = QtWidgets.QPushButton(self.groupBox_6)
        self.btnInfo_birthTime.setMinimumSize(QtCore.QSize(0, 30))
        self.btnInfo_birthTime.setObjectName("btnInfo_birthTime")
        self.gridLayout_4.addWidget(self.btnInfo_birthTime, 7, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/135.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageFileInfo, icon1, "")
        self.pageDir = QtWidgets.QWidget()
        self.pageDir.setGeometry(QtCore.QRect(0, -104, 324, 477))
        self.pageDir.setObjectName("pageDir")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageDir)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.pageDir)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnDir_homePath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_homePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_homePath.setObjectName("btnDir_homePath")
        self.gridLayout_3.addWidget(self.btnDir_homePath, 1, 0, 1, 1)
        self.btnDir_tempPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_tempPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_tempPath.setObjectName("btnDir_tempPath")
        self.gridLayout_3.addWidget(self.btnDir_tempPath, 0, 0, 1, 1)
        self.btnDir_rootPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_rootPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rootPath.setObjectName("btnDir_rootPath")
        self.gridLayout_3.addWidget(self.btnDir_rootPath, 0, 1, 1, 1)
        self.btnDir_drives = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_drives.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_drives.setObjectName("btnDir_drives")
        self.gridLayout_3.addWidget(self.btnDir_drives, 1, 1, 1, 1)
        self.btnDir_curPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_curPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_curPath.setObjectName("btnDir_curPath")
        self.gridLayout_3.addWidget(self.btnDir_curPath, 2, 0, 1, 1)
        self.btnDir_setCurPath = QtWidgets.QPushButton(self.groupBox)
        self.btnDir_setCurPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_setCurPath.setObjectName("btnDir_setCurPath")
        self.gridLayout_3.addWidget(self.btnDir_setCurPath, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.pageDir)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnDir_mkdir = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_mkdir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_mkdir.setObjectName("btnDir_mkdir")
        self.gridLayout_2.addWidget(self.btnDir_mkdir, 0, 0, 1, 1)
        self.btnDir_remove = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_remove.setObjectName("btnDir_remove")
        self.gridLayout_2.addWidget(self.btnDir_remove, 2, 0, 1, 1)
        self.btnDir_rename = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_rename.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rename.setObjectName("btnDir_rename")
        self.gridLayout_2.addWidget(self.btnDir_rename, 2, 1, 1, 1)
        self.btnDir_setPath = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_setPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_setPath.setObjectName("btnDir_setPath")
        self.gridLayout_2.addWidget(self.btnDir_setPath, 3, 0, 1, 1)
        self.btnDir_rmdir = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_rmdir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_rmdir.setObjectName("btnDir_rmdir")
        self.gridLayout_2.addWidget(self.btnDir_rmdir, 0, 1, 1, 1)
        self.btnDir_removeALL = QtWidgets.QPushButton(self.groupBox_4)
        self.btnDir_removeALL.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_removeALL.setObjectName("btnDir_removeALL")
        self.gridLayout_2.addWidget(self.btnDir_removeALL, 3, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.pageDir)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnDir_absPath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_absPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_absPath.setObjectName("btnDir_absPath")
        self.gridLayout.addWidget(self.btnDir_absPath, 0, 1, 1, 1)
        self.btnDir_canonPath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_canonPath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_canonPath.setObjectName("btnDir_canonPath")
        self.gridLayout.addWidget(self.btnDir_canonPath, 1, 0, 1, 1)
        self.btnDir_filePath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_filePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_filePath.setObjectName("btnDir_filePath")
        self.gridLayout.addWidget(self.btnDir_filePath, 1, 1, 1, 1)
        self.btnDir_dirName = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_dirName.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_dirName.setObjectName("btnDir_dirName")
        self.gridLayout.addWidget(self.btnDir_dirName, 2, 1, 1, 1)
        self.btnDir_exists = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_exists.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_exists.setObjectName("btnDir_exists")
        self.gridLayout.addWidget(self.btnDir_exists, 2, 0, 1, 1)
        self.btnDir_absFilePath = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_absFilePath.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_absFilePath.setObjectName("btnDir_absFilePath")
        self.gridLayout.addWidget(self.btnDir_absFilePath, 0, 0, 1, 1)
        self.btnDir_listFile = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_listFile.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_listFile.setObjectName("btnDir_listFile")
        self.gridLayout.addWidget(self.btnDir_listFile, 3, 1, 1, 1)
        self.btnDir_listDir = QtWidgets.QPushButton(self.groupBox_3)
        self.btnDir_listDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnDir_listDir.setObjectName("btnDir_listDir")
        self.gridLayout.addWidget(self.btnDir_listDir, 3, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/007.GIF"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageDir, icon2, "")
        self.pageWatcher = QtWidgets.QWidget()
        self.pageWatcher.setGeometry(QtCore.QRect(0, 0, 296, 390))
        self.pageWatcher.setObjectName("pageWatcher")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.pageWatcher)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_11 = QtWidgets.QGroupBox(self.pageWatcher)
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btnWatch_addDir = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_addDir.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_addDir.setObjectName("btnWatch_addDir")
        self.verticalLayout_6.addWidget(self.btnWatch_addDir)
        self.btnWatch_addFiles = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_addFiles.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_addFiles.setObjectName("btnWatch_addFiles")
        self.verticalLayout_6.addWidget(self.btnWatch_addFiles)
        self.btnWatch_remove = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_remove.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_remove.setObjectName("btnWatch_remove")
        self.verticalLayout_6.addWidget(self.btnWatch_remove)
        self.btnWatch_dirs = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_dirs.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_dirs.setObjectName("btnWatch_dirs")
        self.verticalLayout_6.addWidget(self.btnWatch_dirs)
        self.btnWatch_files = QtWidgets.QPushButton(self.groupBox_11)
        self.btnWatch_files.setMinimumSize(QtCore.QSize(0, 30))
        self.btnWatch_files.setObjectName("btnWatch_files")
        self.verticalLayout_6.addWidget(self.btnWatch_files)
        self.verticalLayout_9.addWidget(self.groupBox_11)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/714.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.pageWatcher, icon3, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpenFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOpenFile.setMinimumSize(QtCore.QSize(0, 30))
        self.btnOpenFile.setIcon(icon2)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.horizontalLayout.addWidget(self.btnOpenFile)
        self.btnOpenDir = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOpenDir.setMinimumSize(QtCore.QSize(0, 30))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/122.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOpenDir.setIcon(icon4)
        self.btnOpenDir.setObjectName("btnOpenDir")
        self.horizontalLayout.addWidget(self.btnOpenDir)
        self.btnClear = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClear.setMinimumSize(QtCore.QSize(0, 30))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/212.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon5)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setMinimumSize(QtCore.QSize(0, 30))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/132.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon6)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.editFile = QtWidgets.QLineEdit(self.groupBox_2)
        self.editFile.setClearButtonEnabled(True)
        self.editFile.setObjectName("editFile")
        self.gridLayout_6.addWidget(self.editFile, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.editDir = QtWidgets.QLineEdit(self.groupBox_2)
        self.editDir.setClearButtonEnabled(True)
        self.editDir.setObjectName("editDir")
        self.gridLayout_6.addWidget(self.editDir, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_6.addWidget(self.textEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_6)
        self.verticalLayout_10.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(3)
        self.btnClose.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Demo9_4????????????????????????"))
        self.groupBox_10.setTitle(_translate("MainWindow", "????????????"))
        self.btnFile_exists.setToolTip(_translate("MainWindow", "Returns true if the file specified by fileName exists; otherwise returns false."))
        self.btnFile_exists.setText(_translate("MainWindow", "exists()"))
        self.btnFile_copy.setToolTip(_translate("MainWindow", "Copies the file fileName to newName."))
        self.btnFile_copy.setText(_translate("MainWindow", "copy()"))
        self.btnFile_remove.setToolTip(_translate("MainWindow", "Removes the file specified by the fileName given."))
        self.btnFile_remove.setText(_translate("MainWindow", "remove()"))
        self.btnFile_rename.setToolTip(_translate("MainWindow", "Renames the file oldName to newName. "))
        self.btnFile_rename.setText(_translate("MainWindow", "rename()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFile), _translate("MainWindow", "QFile???"))
        self.groupBox_6.setTitle(_translate("MainWindow", "????????????"))
        self.btnInfo_baseName.setToolTip(_translate("MainWindow", "The base name consists of all characters in the file up to (but not including) the first \'.\' character"))
        self.btnInfo_baseName.setText(_translate("MainWindow", "baseName()"))
        self.btnInfo_absPath.setToolTip(_translate("MainWindow", "Returns a file\'s path absolute path. This doesn\'t include the file name"))
        self.btnInfo_absPath.setText(_translate("MainWindow", "absolutePath() "))
        self.btnInfo_absFilePath.setToolTip(_translate("MainWindow", "Returns an absolute path including the file name"))
        self.btnInfo_absFilePath.setText(_translate("MainWindow", "absoluteFilePath()"))
        self.btnInfo_baseName2.setToolTip(_translate("MainWindow", "The complete base name consists of all characters in the file up to (but not including) the last \'.\' character"))
        self.btnInfo_baseName2.setText(_translate("MainWindow", "completeBaseName()"))
        self.btnInfo_isDir.setToolTip(_translate("MainWindow", "Returns true if this object points to a directory or to a symbolic link to a directory; otherwise returns false"))
        self.btnInfo_isDir.setText(_translate("MainWindow", "isDir()"))
        self.btnInfo_isFile.setToolTip(_translate("MainWindow", "Returns true if this object points to a file or to a symbolic link to a file"))
        self.btnInfo_isFile.setText(_translate("MainWindow", "isFile()"))
        self.btnInfo_isExec.setToolTip(_translate("MainWindow", "Returns true if the file is executable; otherwise returns false."))
        self.btnInfo_isExec.setText(_translate("MainWindow", "isExecutable()"))
        self.btnInfo_lastModified.setToolTip(_translate("MainWindow", "Returns the date and time when the file was last modified."))
        self.btnInfo_lastModified.setText(_translate("MainWindow", "lastModified()"))
        self.btnInfo_lastRead.setToolTip(_translate("MainWindow", "Returns the date and time when the file was last read (accessed)."))
        self.btnInfo_lastRead.setText(_translate("MainWindow", "lastRead()"))
        self.btnInfo_fileName.setToolTip(_translate("MainWindow", "Returns the name of the file, excluding the path."))
        self.btnInfo_fileName.setText(_translate("MainWindow", "fileName()"))
        self.btnInfo_exists2.setToolTip(_translate("MainWindow", "Returns true if the file exists; otherwise returns false"))
        self.btnInfo_exists2.setText(_translate("MainWindow", "exists()"))
        self.btnInfo_suffix.setToolTip(_translate("MainWindow", "The suffix consists of all characters in the file after (but not including) the last \'.\'"))
        self.btnInfo_suffix.setText(_translate("MainWindow", "suffix()"))
        self.btnInfo_exists.setToolTip(_translate("MainWindow", "Returns true if the file exists; otherwise returns false"))
        self.btnInfo_exists.setText(_translate("MainWindow", "????????????exists()"))
        self.btnInfo_suffix2.setToolTip(_translate("MainWindow", "The complete suffix consists of all characters in the file after (but not including) the first \'.\'"))
        self.btnInfo_suffix2.setText(_translate("MainWindow", "completeSuffix()"))
        self.btnInfo_filePath.setToolTip(_translate("MainWindow", "Returns the file name, including the path (which may be absolute or relative)."))
        self.btnInfo_filePath.setText(_translate("MainWindow", "filePath()"))
        self.btnInfo_path.setToolTip(_translate("MainWindow", "Returns the file\'s path. This doesn\'t include the file name."))
        self.btnInfo_path.setText(_translate("MainWindow", "path()"))
        self.btnInfo_size.setToolTip(_translate("MainWindow", "Returns the file size in bytes."))
        self.btnInfo_size.setText(_translate("MainWindow", "size()"))
        self.btnInfo_birthTime.setToolTip(_translate("MainWindow", "Returns the date and time when the file was created / born"))
        self.btnInfo_birthTime.setText(_translate("MainWindow", "birthTime()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageFileInfo), _translate("MainWindow", "QFileInfo???"))
        self.groupBox.setTitle(_translate("MainWindow", "????????????"))
        self.btnDir_homePath.setToolTip(_translate("MainWindow", "Returns the absolute path of the user\'s home directory"))
        self.btnDir_homePath.setText(_translate("MainWindow", "homePath()"))
        self.btnDir_tempPath.setToolTip(_translate("MainWindow", "Returns the absolute path of the system\'s temporary directory"))
        self.btnDir_tempPath.setText(_translate("MainWindow", "tempPath()"))
        self.btnDir_rootPath.setToolTip(_translate("MainWindow", "Returns the absolute path of the root directory"))
        self.btnDir_rootPath.setText(_translate("MainWindow", "rootPath()"))
        self.btnDir_drives.setToolTip(_translate("MainWindow", "Returns a list of the root directories on this system"))
        self.btnDir_drives.setText(_translate("MainWindow", "drives()"))
        self.btnDir_curPath.setToolTip(_translate("MainWindow", "Returns the absolute path of the application\'s current directory"))
        self.btnDir_curPath.setText(_translate("MainWindow", "currentPath()"))
        self.btnDir_setCurPath.setToolTip(_translate("MainWindow", "Sets the application\'s current working directory to path"))
        self.btnDir_setCurPath.setText(_translate("MainWindow", "setCurrent()"))
        self.groupBox_4.setTitle(_translate("MainWindow", "?????????????????????"))
        self.btnDir_mkdir.setToolTip(_translate("MainWindow", "Creates a sub-directory called dirName."))
        self.btnDir_mkdir.setText(_translate("MainWindow", "mkdir()"))
        self.btnDir_remove.setToolTip(_translate("MainWindow", "Removes the file, fileName."))
        self.btnDir_remove.setText(_translate("MainWindow", "remove()"))
        self.btnDir_rename.setToolTip(_translate("MainWindow", "Renames a file or directory from oldName to newName"))
        self.btnDir_rename.setText(_translate("MainWindow", "rename()"))
        self.btnDir_setPath.setToolTip(_translate("MainWindow", "Sets the path of the directory to path"))
        self.btnDir_setPath.setText(_translate("MainWindow", "setPath()"))
        self.btnDir_rmdir.setToolTip(_translate("MainWindow", "Removes the directory specified by dirName."))
        self.btnDir_rmdir.setText(_translate("MainWindow", "rmdir()"))
        self.btnDir_removeALL.setToolTip(_translate("MainWindow", "Removes the directory, including all its contents."))
        self.btnDir_removeALL.setText(_translate("MainWindow", "removeRecursively()"))
        self.groupBox_3.setTitle(_translate("MainWindow", "?????????????????????"))
        self.btnDir_absPath.setToolTip(_translate("MainWindow", "Returns the absolute path (a path that starts with \"/\" or with a drive specification)"))
        self.btnDir_absPath.setText(_translate("MainWindow", "absolutePath()"))
        self.btnDir_canonPath.setToolTip(_translate("MainWindow", "Returns the canonical path, i.e. a path without symbolic links or redundant \".\" or \"..\" elements."))
        self.btnDir_canonPath.setText(_translate("MainWindow", "canonicalPath()"))
        self.btnDir_filePath.setToolTip(_translate("MainWindow", "Returns the path name of a file in the directory"))
        self.btnDir_filePath.setText(_translate("MainWindow", "filePath()"))
        self.btnDir_dirName.setToolTip(_translate("MainWindow", "Returns the name of the directory"))
        self.btnDir_dirName.setText(_translate("MainWindow", "dirName()"))
        self.btnDir_exists.setToolTip(_translate("MainWindow", "Returns true if the directory exists"))
        self.btnDir_exists.setText(_translate("MainWindow", "exists()??????"))
        self.btnDir_absFilePath.setToolTip(_translate("MainWindow", "Returns the absolute path name of a file in the directory"))
        self.btnDir_absFilePath.setText(_translate("MainWindow", "absoluteFilePath()"))
        self.btnDir_listFile.setToolTip(_translate("MainWindow", "Returns a list of the names of all the files and directories in the directory"))
        self.btnDir_listFile.setText(_translate("MainWindow", "entryList(file)"))
        self.btnDir_listDir.setToolTip(_translate("MainWindow", "Returns a list of the names of all the files and directories in the directory"))
        self.btnDir_listDir.setText(_translate("MainWindow", "entryList(dir)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageDir), _translate("MainWindow", "QDir???"))
        self.btnWatch_addDir.setToolTip(_translate("MainWindow", "Adds path to the file system watcher if path exists. "))
        self.btnWatch_addDir.setText(_translate("MainWindow", "addPath()??????????????????"))
        self.btnWatch_addFiles.setToolTip(_translate("MainWindow", "Adds each path in paths to the file system watcher. "))
        self.btnWatch_addFiles.setText(_translate("MainWindow", "addPaths()??????????????????"))
        self.btnWatch_remove.setToolTip(_translate("MainWindow", "Removes the specified path from the file system watcher."))
        self.btnWatch_remove.setText(_translate("MainWindow", "removePaths()?????????????????????"))
        self.btnWatch_dirs.setToolTip(_translate("MainWindow", "Returns a list of paths to directories that are being watched."))
        self.btnWatch_dirs.setText(_translate("MainWindow", "directories()"))
        self.btnWatch_files.setToolTip(_translate("MainWindow", "Returns a list of paths to files that are being watched."))
        self.btnWatch_files.setText(_translate("MainWindow", "files()"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageWatcher), _translate("MainWindow", "QFileSystemWatcher???"))
        self.btnOpenFile.setText(_translate("MainWindow", "????????????"))
        self.btnOpenDir.setText(_translate("MainWindow", "????????????"))
        self.btnClear.setToolTip(_translate("MainWindow", "???????????????????????????"))
        self.btnClear.setText(_translate("MainWindow", "??????"))
        self.btnClose.setText(_translate("MainWindow", "??????"))
        self.label.setText(_translate("MainWindow", "??? ??? "))
        self.label_2.setText(_translate("MainWindow", "??? ??? "))
        self.label_3.setText(_translate("MainWindow", "??? ??? "))

import res_rc
