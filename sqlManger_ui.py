# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqlManger_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 621, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.host = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.host.setObjectName("host")
        self.horizontalLayout.addWidget(self.host)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.port = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pwd = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.pwd.setObjectName("pwd")
        self.horizontalLayout.addWidget(self.pwd)
        self.connbut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.connbut.setObjectName("connbut")
        self.horizontalLayout.addWidget(self.connbut)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 100, 621, 281))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 390, 621, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.databasetype = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.databasetype.setObjectName("databasetype")
        self.databasetype.addItem("")
        self.databasetype.addItem("")
        self.horizontalLayout_3.addWidget(self.databasetype)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.themeComboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.themeComboBox.setObjectName("themeComboBox")
        self.themeComboBox.addItem("")
        self.themeComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.themeComboBox)
        self.progressBar = QtWidgets.QProgressBar(self.horizontalLayoutWidget_3)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.roolbackbut = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.roolbackbut.setObjectName("roolbackbut")
        self.horizontalLayout_3.addWidget(self.roolbackbut)
        self.commitbut = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.commitbut.setObjectName("commitbut")
        self.horizontalLayout_3.addWidget(self.commitbut)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 91, 41))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(295, 60, 52, 21))
        self.label_7.setObjectName("label_7")
        self.database = QtWidgets.QComboBox(self.centralwidget)
        self.database.setGeometry(QtCore.QRect(41, 60, 237, 22))
        self.database.setObjectName("database")
        self.tablename = QtWidgets.QComboBox(self.centralwidget)
        self.tablename.setGeometry(QtCore.QRect(328, 60, 221, 22))
        self.tablename.setObjectName("tablename")
        self.querybut = QtWidgets.QPushButton(self.centralwidget)
        self.querybut.setGeometry(QtCore.QRect(554, 59, 78, 23))
        self.querybut.setObjectName("querybut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "主机"))
        self.host.setText(_translate("MainWindow", "localhost"))
        self.label_6.setText(_translate("MainWindow", "端口号"))
        self.port.setText(_translate("MainWindow", "3306"))
        self.label_3.setText(_translate("MainWindow", "用户名"))
        self.username.setText(_translate("MainWindow", "root"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.pwd.setText(_translate("MainWindow", "1234"))
        self.connbut.setText(_translate("MainWindow", "连接"))
        self.label.setText(_translate("MainWindow", "数据库类型"))
        self.databasetype.setItemText(0, _translate("MainWindow", "QMYSQL"))
        self.databasetype.setItemText(1, _translate("MainWindow", "QSQLLITE"))
        self.label_8.setText(_translate("MainWindow", "主题"))
        self.themeComboBox.setItemText(0, _translate("MainWindow", "Light"))
        self.themeComboBox.setItemText(1, _translate("MainWindow", "Dark"))
        self.roolbackbut.setText(_translate("MainWindow", "回滚"))
        self.commitbut.setText(_translate("MainWindow", "提交"))
        self.label_5.setText(_translate("MainWindow", "库名"))
        self.label_7.setText(_translate("MainWindow", "表名"))
        self.querybut.setText(_translate("MainWindow", "查询"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
