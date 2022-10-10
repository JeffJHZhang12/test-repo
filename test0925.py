import sys
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    btn = QPushButton()
    btn.setText("hello")
    btn.setWindowTitle("hello xx")
    btn.resize(640, 480)
    btn.show()
    # model = QDirModel()
    # tree = QTreeView()
    # tree.setModel(model)
    # tree.setWindowTitle("hello xx")
    # tree.resize(640, 480)
    # tree.show()
    sys.exit(app.exec_())
