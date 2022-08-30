import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Ui_firstuio

if __name__ == "__main__":

    app = QApplication(sys.argv)
    mw = QMainWindow()
    ui = Ui_firstuio.Ui_MainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())
