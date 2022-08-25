import sys, ui
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
window.show()
a = ui.Ui_MainWindow()
a.setupUi(window)
a.connectSlots()
app.exec()