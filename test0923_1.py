import sys
from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QToolTip,
    QHBoxLayout,
    QRadioButton,
    QComboBox,
    QPushButton,
    QDialog,
    QMessageBox,
    QLabel,
)
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt


class Icon(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("你好啊")
        # self.setWindowIcon(QIcon("/Users/jeffjhzhang/pyabc/ico/BBEdit.icns"))
        # self.setToolTip("这是一个奇葩")
        layout = QHBoxLayout()
        self.btn1 = QRadioButton("button1")
        self.btn1.toggled.connect(self.btnstate)
        layout.addWidget(self.btn1)

        self.btn2 = QComboBox()
        # self.btn2.style
        self.btn2.addItem("text1", "v1")
        self.btn2.addItem("text2", "v2")
        self.btn2.addItem("text3", "v3")
        self.btn2.addItem("text4", "v4")
        self.btn2.addItem("text5", "v5")
        self.btn2.setCurrentIndex(-1)
        self.btn2.currentIndexChanged.connect(self.selectionchange)

        # self.btn2.setChecked(1)
        # self.btn2.toggled.connect(self.btnstate)
        layout.addWidget(self.btn2)
        self.btn3 = QPushButton()
        self.btn3.setText("窗口")
        self.btn3.clicked.connect(self.showdialog)
        layout.addWidget(self.btn3)
        self.lb = QLabel()
        # self.lb.setAutoFillBackground(True)
        # palette = QPalette(Qt.blue)
        # self.lb.setPalette(palette)
        img = QPixmap("./ico/spotify_logo.png")
        self.lb.setPixmap(img)
        layout.addWidget(self.lb)
        self.setLayout(layout)

    def btnstate(self):
        btn = self.sender()
        if btn == self.btn1:
            print(
                "name: {} --> state: {}".format(self.btn1.text(), self.btn1.isChecked())
            )
        # if btn == self.btn2:
        #     print(
        #         "name: {} --> state: {}".format(self.btn2.text(), self.btn2.isChecked())
        #     )

    def selectionchange(self):
        txt = self.btn2.currentData()
        print(txt)

    def showdialog(self):
        # d = QDialog()
        # d.setWindowTitle("xxx")
        # d.setWindowModality(Qt.WindowModality.ApplicationModal)
        # d.exec_()
        ret = QMessageBox.information(
            self,
            "提示",
            "你真的要删除这些文件吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if ret == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ico/preview.ico"))
    icon = Icon()
    icon.show()
    sys.exit(app.exec_())
