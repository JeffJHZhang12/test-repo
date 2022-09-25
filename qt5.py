import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QWidget

import Ui_slottest

if __name__ == "__main__":

    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = Ui_slottest.Ui_Form()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())
