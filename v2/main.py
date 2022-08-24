import sys
from ui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.show()
ui = Ui_MainWindow()
ui.setupUi(window)
app.exec()

