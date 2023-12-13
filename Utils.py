from PyQt5.QtWidgets import QMessageBox


class Utils(object):
    @staticmethod
    def show_msg(self, msg):
        QMessageBox.information(self, "提示信息", f"{msg}        ", QMessageBox.Ok, QMessageBox.Ok)

