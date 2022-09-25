import sys
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Listwidget(QListWidget):
    def clicked(self, item):
        QMessageBox.information(self, "Listwidget", "你选择了:" + item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listwidget = Listwidget()
    listwidget.resize(300, 120)
    listwidget.addItem("Item 1")
    listwidget.addItem("Item 2")
    listwidget.addItem("Item 3")
    listwidget.addItem("Item 4")
    listwidget.setWindowTitle("QListwidget")
    listwidget.itemClicked.connect(listwidget.clicked)
    listwidget.show()
    sys.exit(app.exec_())
