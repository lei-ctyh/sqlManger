import sys

import qdarkstyle
from PyQt5 import QtWidgets, QtCore
from qdarkstyle import LightPalette

from Manger import Manger
from utils.ContainerUtil import ContainerUtil

#  适配高分辨率屏幕
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

app = QtWidgets.QApplication(sys.argv)
ContainerUtil.set_app_self(app)
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))

manger_win = Manger()
manger_win.show()

sys.exit(app.exec_())
