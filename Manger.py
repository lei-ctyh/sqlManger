import pymysql
from PyQt5.QtCore import QAbstractItemModel, QAbstractTableModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtWidgets import QMainWindow, QHeaderView

from Utils import Utils
from sqlManger_ui import Ui_MainWindow


# SqlQueryMoedl和QSqlQuery联合使用;
class Manger(QMainWindow):
    def __init__(self, parent=None):
        super(Manger, self).__init__(parent)
        # 数据库链接信息
        self.connection = None
        self.db = None

        # UI信息
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 连接槽函数
        self.ui.pushButton.clicked.connect(self.conn_database)
        self.ui.pushButton_2.clicked.connect(self.execute_query)
        self.ui.pushButton_3.clicked.connect(self.previous_page)
        self.ui.pushButton_4.clicked.connect(self.next_page)
        self.ui.comboBox.currentIndexChanged.connect(self.change_database)

    def conn_database(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',  # 数据库主机名
                port=3306,  # 数据库端口号，默认为3306
                user='root',  # 数据库用户名
                passwd='123456',  # 数据库密码
                charset='utf8'  # 字符编码
            )
            # 创建游标对象
            cursor = self.connection.cursor()
            sql = "SHOW DATABASES"
            # 加载库结构
            if cursor.execute(sql):
                result = cursor.fetchall()
                self.ui.comboBox.clear()
                for i in result:
                    self.ui.comboBox.addItem(i[0])
            Utils.show_msg(self, "数据库链接成功!")
        except Exception as e:
            Utils.show_msg(self, f"数据库链接异常!{e}")

    def execute_query(self):
        try:
            if self.connection is None:
                Utils.show_msg(self, "请先连接数据库!")
            else:
                query_sql = f"select * from `{self.ui.comboBox_2.currentText()}`"
                if query_sql == "":
                    Utils.show_msg(self, "请选择要查询的表格!")
                else:
                    cursor = self.connection.cursor()
                    cursor.execute(query_sql)
                    result = cursor.fetchall()
                    model = QStandardItemModel()
                    # 加载表头
                    header = []
                    for col in cursor.description:
                        header.append(col[0])
                        model.setHorizontalHeaderLabels(header)

                        # 加载数据
                        for index, value in enumerate(result):
                            row = []
                            for colTuple in value:
                                col = QStandardItem(str(colTuple))
                                row.append(col)
                            model.appendRow(row)
                            self.load_progress_bar(((index+1) / len(result)) * 100)

                        # model.
                        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                        self.ui.tableView.setSortingEnabled(True)
                        self.ui.tableView.setModel(model)
        except Exception as e:
            Utils.show_msg(self, f"查询失败:{e}")

    def previous_page(self):
        # 上一页
        print("上一页")

    def next_page(self):
        # 下一页
        print("下一页")

    def change_database(self):
        # 切换数据库
        curDataBase = self.ui.comboBox.currentText()
        curses = self.connection.cursor()
        curses.execute(f"use {curDataBase}")
        # 加载表
        self.ui.comboBox_2.clear()
        if curses.execute(f"show tables"):
            result = curses.fetchall()
            for i in result:
                self.ui.comboBox_2.addItem(i[0])

    def load_progress_bar(self, progress):
        self.ui.progressBar.setProperty("value", progress)
