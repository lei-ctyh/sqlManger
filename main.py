import sys

from PyQt5 import QtWidgets, QtCore

from Manger import Manger

#  适配高分辨率屏幕
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

app = QtWidgets.QApplication(sys.argv)
manger_win = Manger()
manger_win.show()
sys.exit(app.exec_())
