import sys

from PyQt5 import QtWidgets

from Manger import Manger
from sqlManger_ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

manger_win = Manger()
manger_win.show()
sys.exit(app.exec_())
