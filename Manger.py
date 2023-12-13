import pymysql
from PyQt5 import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QLineEdit

from Utils import Utils
from sqlManger_ui import Ui_MainWindow


# SqlQueryMoedl和QSqlQuery联合使用;
class Manger(QMainWindow):
    def __init__(self, parent=None):
        super(Manger, self).__init__(parent)
        # 数据库链接信息
        self.connection = None
        self.db = None
        # 数据库表面板参数
        self.tab_header = []
        self.tab_primary_key = ''

        # 设置UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 密码开启隐私模式
        self.ui.pwd.setEchoMode(QLineEdit.Password)
        # 端口限制 0-65535
        port_validator = QIntValidator()
        port_validator.setRange(0, 65535)
        self.ui.port.setValidator(port_validator)

        # 连接槽函数
        self.ui.connbut.clicked.connect(self.conn_database)
        self.ui.querybut.clicked.connect(self.execute_query)
        self.ui.roolbackbut.clicked.connect(self.rollback_database)
        self.ui.commitbut.clicked.connect(self.commit_database)
        self.ui.database.currentIndexChanged.connect(self.change_database)

    def conn_database(self):
        try:
            self.connection = pymysql.connect(
                # 数据库主机名
                host=self.ui.host.text(),
                # 数据库端口号，默认为3306
                port=int(self.ui.port.text()),
                # 数据库用户名
                user=self.ui.username.text(),
                # 数据库密码
                passwd=self.ui.pwd.text(),
                # 字符编码
                charset='utf8'
            )
            # 创建游标对象
            cursor = self.connection.cursor()
            sql = "SHOW DATABASES"
            # 加载库结构
            if cursor.execute(sql):
                result = cursor.fetchall()
                self.ui.database.clear()
                for i in result:
                    self.ui.database.addItem(i[0])
            Utils.show_msg(self, "数据库链接成功!")
        except Exception as e:
            Utils.show_msg(self, f"数据库链接异常!{e}")

    def execute_query(self):
        try:
            if self.connection is None:
                Utils.show_msg(self, "请先连接数据库!")
            else:
                query_sql = f"select * from `{self.ui.tablename.currentText()}`"
                query_header = f"select CASE WHEN COLUMN_COMMENT IS NULL THEN COLUMN_NAME WHEN COLUMN_COMMENT = '' THEN COLUMN_NAME ELSE COLUMN_COMMENT END, column_key from information_schema.columns where table_schema = '{self.ui.database.currentText()}' and table_name = '{self.ui.tablename.currentText()}' ORDER BY  ORDINAL_POSITION"
                if self.ui.tablename.currentText() == "":
                    Utils.show_msg(self, "请选择要查询的表格!")
                else:
                    cursor = self.connection.cursor()
                    model = QStandardItemModel()
                    model.dataChanged.connect(self.modify_data)
                    # 加载表头
                    cursor.execute(query_header)
                    self.tab_header = []
                    header = []
                    for col in cursor.fetchall():
                        self.tab_header.append(col)
                        header.append(col[0])
                    model.setHorizontalHeaderLabels(header)

                    # 加载数据
                    cursor.execute(query_sql)
                    result = cursor.fetchall()
                    for index, value in enumerate(result):
                        row = []
                        for colTuple in value:
                            col = QStandardItem(str(colTuple))
                            row.append(col)
                        model.appendRow(row)
                        self.load_progress_bar(((index + 1) / len(result)) * 100)

                    self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                    self.ui.tableView.setSortingEnabled(True)
                    self.ui.tableView.setModel(model)
        except Exception as e:
            Utils.show_msg(self, f"查询失败:{e}")

    def rollback_database(self):
        # 上一页
        print("上一页")

    def commit_database(self):
        # 获取tableView全部数据
        self.ui.tableView.model().lay
        Utils.show_msg(self, "提交成功")

    def change_database(self):
        # 切换数据库
        curDataBase = self.ui.database.currentText()
        if curDataBase == "":
            return
        self.connection.select_db(curDataBase)
        curses = self.connection.cursor()
        curses.execute(f"use {curDataBase}")
        # 加载表
        self.ui.tablename.clear()
        if curses.execute(f"show tables"):
            result = curses.fetchall()
            for i in result:
                self.ui.tablename.addItem(i[0])

    def load_progress_bar(self, progress):
        self.ui.progressBar.setProperty("value", progress)

    def modify_data(self):
        # 修改数据
        data = self.ui.tableView.currentIndex().data()
        row_data = self.ui.tableView
        col_index = self.ui.tableView.currentIndex().column()
        upd_sql = f"update `{self.ui.tablename.currentText()}` set `{self.tab_header[col_index]}` = '{data}' where id = {self.ui.tableView.currentIndex().row()}"
        print(upd_sql)
        self.connection.cursor().execute(upd_sql)

    def delete_data(self):
        # 删除数据
        row = self.ui.tableView.currentIndex().row()
        print(row)

    def insert_data(self):
        # 插入数据
        row = self.ui.tableView.currentIndex().row()
        column = self.ui.tableView.currentIndex().column()
        if row == -1 or column == -1:
            return
        value = self.ui.lineEdit.text()
        self.ui.tableView.model().setData(self.ui.tableView.model().index(row, column), value)
