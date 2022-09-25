import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(300, 200)
window.move(250, 200)
window.setWindowTitle("你好啊")
window.show()
sys.exit(app.exec_())
