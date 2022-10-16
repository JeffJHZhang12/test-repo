import sys
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_colordemo import Ui_Form


class QmyUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.spinred.valueChanged.connect(self.spinvalueChanged)
        self.ui.spingreen.valueChanged.connect(self.spinvalueChanged)
        self.ui.spinblue.valueChanged.connect(self.spinvalueChanged)

        self.ui.slidered.valueChanged.connect(self.slidevalueChanged)
        self.ui.slidegreen.valueChanged.connect(self.slidevalueChanged)
        self.ui.slideblue.valueChanged.connect(self.slidevalueChanged)

        self.ui.lblcolor.setText("")
        self.ui.spinred.setValue(255)
        self.ui.spingreen.setValue(255)
        self.ui.spinblue.setValue(255)
        # self.ui.btnOK.clicked.connect(self.doSomething)

    # def doSomething(self):
    #     ret = QMessageBox.question(
    #         self,
    #         "title",
    #         "are you sure you want to quit.",
    #         QMessageBox.Yes | QMessageBox.No,
    #         QMessageBox.Yes,
    #     )
    #     if ret == QMessageBox.Yes:
    #         self.close()
    def spinvalueChanged(self, x):
        if self.sender() == self.ui.spinred:
            self.ui.slidered.setValue(x)
        elif self.sender() == self.ui.spingreen:
            self.ui.slidegreen.setValue(x)
        else:
            self.ui.slideblue.setValue(x)

        red = self.ui.spinred.value()
        green = self.ui.spingreen.value()
        blue = self.ui.spinblue.value()
        pt = self.ui.label.palette()
        pt.setColor(QPalette.Background, QColor(red, green, blue, 255))
        self.ui.lblcolor.setAutoFillBackground(True)
        self.ui.lblcolor.setPalette(pt)

    def slidevalueChanged(self, x):
        if self.sender() == self.ui.slidered:
            self.ui.spinred.setValue(x)
        elif self.sender() == self.ui.slidegreen:
            self.ui.spingreen.setValue(x)
        else:
            self.ui.spinblue.setValue(x)

        red = self.ui.spinred.value()
        green = self.ui.spingreen.value()
        blue = self.ui.spinblue.value()
        pt = self.ui.label.palette()
        pt.setColor(QPalette.Background, QColor(red, green, blue, 255))
        self.ui.lblcolor.setAutoFillBackground(True)
        self.ui.lblcolor.setPalette(pt)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./ico/preview.ico"))
    win = QmyUI()
    win.show()
    sys.exit(app.exec_())
