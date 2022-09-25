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
    QFormLayout,
)
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap
from PyQt5.QtCore import Qt


class layout(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton("ok")
        self.btn2 = QPushButton("cancel")
        formlayout = QFormLayout()
        formlayout.addRow("first:", self.btn1)
        formlayout.addRow("second:", self.btn2)
        self.setLayout(formlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ico/golive.ico"))
    icon = layout()
    icon.show()
    sys.exit(app.exec_())
