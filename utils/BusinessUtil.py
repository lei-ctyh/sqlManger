from PyQt5.QtWidgets import QMessageBox


class BusinessUtil(object):
    """
    显示提示信息
    self : 主窗口
    msg : 信息
    """

    @staticmethod
    def show_msg(self, msg):
        QMessageBox.information(self, "提示信息", f"{msg}        ", QMessageBox.Ok, QMessageBox.Ok)


