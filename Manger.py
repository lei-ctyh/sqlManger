import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QLineEdit, QMenu
from qdarkstyle import LightPalette, DarkPalette
from qt_material import apply_stylesheet, list_themes

from model.UpdateItemModel import UpdateItemModel
from ui.addrowdialog_ui import Ui_Dialog
from ui.sqlManger_ui import Ui_MainWindow
from utils.BusinessUtil import BusinessUtil
from utils.ContainerUtil import ContainerUtil
from utils.DbUtil import DbUtil


class Manger(QMainWindow):
    def __init__(self, parent=None):
        super(Manger, self).__init__(parent)
        ContainerUtil.set_manger_self(self)
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
        # 连接按钮
        self.ui.connbut.clicked.connect(self.conn_database)
        # 查询按钮
        self.ui.querybut.clicked.connect(self.execute_query)
        # 回滚按钮
        self.ui.roolbackbut.clicked.connect(self.rollback_database)
        # 提交按钮
        self.ui.commitbut.clicked.connect(self.commit_database)
        # 切换数据库选择
        self.ui.database.currentIndexChanged.connect(self.change_database)
        # 更改主题
        self.ui.themeComboBox.currentIndexChanged.connect(self.change_theme)
        # 动态加载qt-material主题美化包
        for theme in list_themes():
            self.ui.themeComboBox.addItem(theme.replace(".xml", ""))

        # 右键表格, 展示菜单
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.display_table_menu)

        # 加载进度条设置为0
        self.ui.progressBar.setValue(0)

    def conn_database(self):
        try:
            connection = DbUtil.get_connection(self)
            cursor = connection.cursor()

            sql = "SHOW DATABASES WHERE `Database` NOT IN ('information_schema', 'performance_schema','mysql', 'sys')"
            # 加载库结构
            if cursor.execute(sql):
                result = cursor.fetchall()
                self.ui.database.clear()
                for i in result:
                    self.ui.database.addItem(i[0])

            # 开启事务
            cursor.execute("BEGIN")
            BusinessUtil.show_msg(self, "数据库链接成功!")
        except Exception as e:
            BusinessUtil.show_msg(self, f"数据库链接异常!{e}")

    def execute_query(self):
        try:
            connection = DbUtil.get_connection(self)
            cursor = connection.cursor()
            connection.rollback()
            if connection is None:
                BusinessUtil.show_msg(self, "请先连接数据库!")
            else:
                query_sql = f"select * from `{self.ui.tablename.currentText()}`"
                query_header_sql = f"select COLUMN_NAME, COLUMN_COMMENT,  COLUMN_KEY,DATA_TYPE from information_schema.columns where table_schema = '{self.ui.database.currentText()}' and table_name = '{self.ui.tablename.currentText()}' ORDER BY  ORDINAL_POSITION"
                if self.ui.tablename.currentText() == "":
                    BusinessUtil.show_msg(self, "请选择要查询的表格!")
                else:
                    model = UpdateItemModel()
                    # 加载表头
                    cursor.execute(query_header_sql)
                    self.tab_header = []
                    header = []
                    for col in cursor.fetchall():
                        self.tab_header.append(col)
                        header.append(f"  {col[0]}  ")
                    model.setHorizontalHeaderLabels(header)

                    # 加载数据
                    cursor.execute(query_sql)
                    result = cursor.fetchall()
                    for index, value in enumerate(result):
                        row = []
                        for colTuple in value:
                            if colTuple is None:
                                colTuple = ""
                            col = QStandardItem(str(colTuple))
                            row.append(col)
                        model.appendRow(row)
                        self.ui.progressBar.setProperty("value", ((index + 1) / len(result)) * 100)

                    self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                    self.ui.tableView.setSortingEnabled(False)
                    self.ui.tableView.setAlternatingRowColors(True)
                    self.ui.tableView.verticalHeader().setVisible(False)
                    self.ui.tableView.setModel(model)

        except Exception as e:
            BusinessUtil.show_msg(self, f"查询失败:{e}")

    def rollback_database(self):
        DbUtil.get_connection(self).rollback()
        BusinessUtil.show_msg(self, "事务回滚成功!")
        self.execute_query()

    def commit_database(self):
        DbUtil.get_connection(self).commit()
        BusinessUtil.show_msg(self, "事务提交成功!")

    def change_database(self):
        try:
            # 切换数据库
            cur_database = self.ui.database.currentText()
            # 数据库为空代表正在进行数据库连接, 无效切换数据库
            if cur_database == "":
                return
            connection = DbUtil.get_connection(self)
            connection.select_db(cur_database)
            cursor = connection.cursor()

            # 加载表
            self.ui.tablename.clear()
            if cursor.execute(f"show tables"):
                result = cursor.fetchall()
                for i in result:
                    self.ui.tablename.addItem(i[0])
            # 清空tableView数据
            self.ui.tableView.setModel(None)
            self.ui.progressBar.setProperty("value", 0)
        except Exception as e:
            BusinessUtil.show_msg(self, f"切换数据库失败:{e}")

    def display_table_menu(self, pos):
        # 判断数据加载进度是否是100%
        if self.ui.progressBar.value() == 0:
            return
        if self.ui.progressBar.value() != 100:
            BusinessUtil.show_msg(self, "数据加载中, 请稍后再试!")
            return

        # 获取当前行号
        row_index = None
        for i in self.ui.tableView.selectionModel().selection().indexes():
            row_index = i.row()

        # 创建菜单
        menu = QMenu()
        add_item = menu.addAction('新增行')
        del_item = menu.addAction('删除行')

        # 将坐标转化为相对于屏幕的
        screen_pos = self.ui.tableView.mapToGlobal(pos)
        action = menu.exec(screen_pos)

        if action == add_item:
            self.insert_data()
        elif action == del_item:
            if row_index is not None:
                self.delete_data(row_index)

        else:
            return

    def insert_data(self):
        try:
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            form_items = []
            for colInfo in self.tab_header:
                form_items.append(colInfo[0])
            ui.setupUi(Dialog, form_items)
            is_ok = Dialog.exec()
            if is_ok == 0:
                return
            row = []
            row_data = []
            for colInfo in self.tab_header:
                col_name = colInfo[0]
                col_data = getattr(ui, f"lineEdit_{col_name}").text()
                row_data.append(col_data)
                row.append(QStandardItem(str(col_data)))
            sql_and_list = DbUtil.get_sql_and_list(self.tab_header, self.ui.tablename.currentText(), row_data, [],
                                                   "add")
            cursor = DbUtil.get_cursor()
            print("插入数据")
            print(sql_and_list)
            cursor.execute(sql_and_list[0], sql_and_list[1])
            self.ui.tableView.model().appendRow(row)
            BusinessUtil.show_msg(self, "保存成功!")
        except Exception as e:
            BusinessUtil.show_msg(self, f"保存失败:{e}")

    def delete_data(self, row_index):
        # 删除数据
        try:
            old_data = []
            for i in range(len(self.tab_header)):
                old_data.append(self.ui.tableView.model().item(self.ui.tableView.currentIndex().row(), i).text())
            sql_and_list = DbUtil.get_sql_and_list(self.tab_header, self.ui.tablename.currentText(), [], old_data,
                                                   "del")
            cursor = DbUtil.get_cursor()
            print("删除数据")
            print(sql_and_list)
            cursor.execute(sql_and_list[0], sql_and_list[1])
            self.ui.tableView.model().removeRow(row_index)
        except Exception as e:
            BusinessUtil.show_msg(self, f"删除失败:{e}")

    def change_theme(self):
        if self.ui.themeComboBox.currentText() == "Dark":
            ContainerUtil.get_app_self().setStyleSheet(
                qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=DarkPalette()))
        elif self.ui.themeComboBox.currentText() == "Light":
            ContainerUtil.get_app_self().setStyleSheet(
                qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
        else:
            apply_stylesheet(ContainerUtil.get_app_self(), theme=self.ui.themeComboBox.currentText() + ".xml")
