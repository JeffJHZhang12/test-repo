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


class winform(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("你好啊")
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")

        layout = QHBoxLayout()
        layout.addStretch(0)
        layout.addWidget(btn1)
        # layout.addStretch(2)
        layout.addWidget(btn2)
        # layout.addStretch(0)
        layout.addWidget(btn3)
        # layout.addStretch(1)
        # layout.addWidget(QPushButton("1"),0, Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(
        #     QPushButton("2"), 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        # )
        # layout.addWidget(QPushButton("3"), 0)
        # layout.addWidget(
        #     QPushButton("4"),
        #     0,
        #     Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
        # )
        # layout.addWidget(
        #     QPushButton("5"),
        #     0,
        #     Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft,
        # )
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
    icon = winform()
    icon.show()
    sys.exit(app.exec_())
