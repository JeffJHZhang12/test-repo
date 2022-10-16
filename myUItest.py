import sys
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_test1014 import Ui_Form


class QmyUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.ui.spinred.valueChanged.connect(self.spinvalueChanged)
        # self.ui.btnOK.clicked.connect(self.doSomething)

    def doClose(self):
        ret = QMessageBox.question(
            self,
            "title",
            "are you sure you want to quit.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes,
        )
        if ret == QMessageBox.Yes:
            self.close()

    # def spinvalueChanged(self, x):
    #     if self.sender() == self.ui.spinred:
    #         self.ui.slidered.setValue(x)
    #     red = self.ui.spinred.value()
    #     green = self.ui.spingreen.value()
    #     blue = self.ui.spinblue.value()
    #     pt = self.ui.label.palette()
    #     pt.setColor(QPalette.ColorRole.WindowText, QColor(red, green, blue, 255))
    #     self.ui.lblcolor.setAutoFillBackground(True)
    #     self.ui.lblcolor.setPalette(pt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ico/preview.ico"))
    win = QmyUI()
    win.show()
    sys.exit(app.exec_())
