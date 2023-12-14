import pymysql
from PyQt5.QtWidgets import QMessageBox


class Utils(object):
    connection = None
    cursor = None
    """
    显示提示信息
    self : 主窗口
    msg : 信息
    """

    @staticmethod
    def show_msg(self, msg):
        QMessageBox.information(self, "提示信息", f"{msg}        ", QMessageBox.Ok, QMessageBox.Ok)

    """
    获取数据库连接
    self : 主窗口
    """

    @staticmethod
    def get_connection(self):
        if Utils.connection is not None:
            return Utils.connection
        Utils.connection = pymysql.connect(
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
        return Utils.connection

    @staticmethod
    def get_cursor():
        if Utils.cursor is not None:
            return Utils.cursor
        else:
            if Utils.connection is None:
                Utils.connection = Utils.get_connection()
                Utils.cursor = Utils.connection.cursor()
                return Utils.cursor
            else:
                Utils.cursor = Utils.connection.cursor()
                return Utils.cursor

    """
    获取sql语句
    tab_header : 表头
    row_data : 行数据
    opt : 操作类型 add/edit/del
    """

    @staticmethod
    def get_sql_and_list(tab_header, table_name, row_data, opt):
        sql_list = []
        sql = ''
        if not tab_header:
            return ''
        else:
            if opt == 'edit':
                sql = f"update {table_name} set "
                for i in range(len(tab_header)):
                    column_name = tab_header[i][0]
                    sql += f'`{column_name}` = %s, '
                    data_type = tab_header[i][3]
                    sql_list.append(Utils.deal_data(row_data[i], data_type))

                if sql.endswith(', '):
                    sql = sql[:-2]

                where_sql = ' WHERE '
                for index, tuple_val in enumerate(tab_header):
                    column_key = tuple_val[2]
                    column_name = tuple_val[0]
                    if column_key == 'PRI':
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(row_data[index])

                if where_sql.endswith('WHERE '):
                    for index, tuple_val in enumerate(tab_header):
                        column_key = tuple_val[2]
                        column_name = tuple_val[0]
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(row_data[index])

                if where_sql.endswith('AND '):
                    where_sql = where_sql[:-4]
                sql += where_sql

            return sql, sql_list

    @staticmethod
    def deal_data(data, data_type):
        if data is None:
            return ''
        elif data_type == 'int':
            return int(data)
        elif data_type == 'float':
            return float(data)
        elif data_type == 'datetime':
            return data.strftime('%Y-%m-%d %H:%M:%S')
        elif data_type == 'timestamp':
            return data.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return data

    @staticmethod
    def get_manger_self():
        return Utils.manger

    @staticmethod
    def set_manger_self(self):
        Utils.manger = self
