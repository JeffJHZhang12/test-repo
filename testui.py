import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import Ui_firstuio


class MyMainWin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        Ui_firstuio.Ui_MainWindow().setupUi(self)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        left = int((screen.width() - size.width()) / 2)
        top = int((screen.height() - size.height()) / 2)
        self.move(left, top)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWin()
    mywin.show()
    sys.exit(app.exec_())

# MainWindow
# define centralwidget
# mainwindow-->centralwidget --> widget --> horizontalLayout -->label text
# mainwindow-->centralwidget --> ok,cancel
# mainwindow-->menu,status
