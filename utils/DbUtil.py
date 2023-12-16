import datetime

import pymysql


class DbUtil(object):
    connection = None
    cursor = None

    """
   获取数据库连接
   self : 主窗口
   """

    @staticmethod
    def get_connection(self):
        if DbUtil.connection is not None:
            return DbUtil.connection
        DbUtil.connection = pymysql.connect(
            # 数据库主机名
            host=self.ui.host.text(),
            # 数据库端口号，默认为3306
            port=int(self.ui.port.text()),
            # 数据库用户名
            user=self.ui.username.text(),
            # 数据库密码
            passwd="123456",
            # 字符编码
            charset='utf8'
        )
        return DbUtil.connection

    @staticmethod
    def get_cursor():
        if DbUtil.cursor is not None:
            return DbUtil.cursor
        else:
            if DbUtil.connection is None:
                DbUtil.connection = DbUtil.get_connection()
                DbUtil.cursor = DbUtil.connection.cursor()
                return DbUtil.cursor
            else:
                DbUtil.cursor = DbUtil.connection.cursor()
                return DbUtil.cursor

    """
    获取sql语句
    tab_header : 表头
    row_data : 行数据
    opt : 操作类型 add/edit/del
    """

    @staticmethod
    def __get_sql_and_list(tab_header, table_name, row_data, old_row_data, opt):
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
                    sql_list.append(DbUtil.__deal_data(row_data[i], data_type))

                if sql.endswith(', '):
                    sql = sql[:-2]

                where_sql = ' WHERE '
                for index, tuple_val in enumerate(tab_header):
                    column_key = tuple_val[2]
                    column_name = tuple_val[0]
                    if column_key == 'PRI':
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(old_row_data[index])

                if where_sql.endswith('WHERE '):
                    for index, tuple_val in enumerate(tab_header):
                        column_key = tuple_val[2]
                        column_name = tuple_val[0]
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(old_row_data[index])

                if where_sql.endswith('AND '):
                    where_sql = where_sql[:-4]
                sql += where_sql

            elif opt == 'add':
                sql = f"insert into {table_name} ("
                for i in range(len(tab_header)):
                    column_name = tab_header[i][0]
                    sql += f'`{column_name}`, '
                if sql.endswith(', '):
                    sql = sql[:-2]
                sql += ') values ('
                for i in range(len(tab_header)):
                    sql += '%s, '
                    data_type = tab_header[i][3]
                    sql_list.append(DbUtil.__deal_data(row_data[i], data_type))
                if sql.endswith(', '):
                    sql = sql[:-2]
                sql += ')'

            elif opt == 'del':
                sql = f"delete from {table_name}  "
                where_sql = ' WHERE '
                for index, tuple_val in enumerate(tab_header):
                    column_key = tuple_val[2]
                    column_name = tuple_val[0]
                    if column_key == 'PRI':
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(old_row_data[index])
                if where_sql.endswith('WHERE '):
                    for index, tuple_val in enumerate(tab_header):
                        column_key = tuple_val[2]
                        column_name = tuple_val[0]
                        where_sql += f'`{column_name}` = %s AND '
                        sql_list.append(old_row_data[index])

                if where_sql.endswith('AND '):
                    where_sql = where_sql[:-4]
                sql += where_sql
            return sql, sql_list

    @staticmethod
    def __deal_data(data, data_type):
        if data == '':
            return None
        if data_type == 'int':
            return int(data)
        elif data_type == 'float':
            return float(data)
        elif data_type == 'datetime':
            try:
                return datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
            # 捕获日期格式化异常""
            except ValueError:
                raise Exception(f'输入日期格式异常，正确示例: 2020-01-01 12:12:12')  # except Exception as e:

        elif data_type == 'timestamp':
            return datetime.datetime.now()
        elif data_type == 'date':
            try:
                if data == '':
                    return None
                return datetime.datetime.strptime(data, '%Y-%m-%d')
            # 捕获日期格式化异常""
            except ValueError:
                raise Exception(f'输入日期格式异常，正确示例: 2020-01-01')
        else:
            return data

    @staticmethod
    def crud_data(tab_header, table_name, row_data, old_row_data, opt):
        sql_and_list = DbUtil.__get_sql_and_list(tab_header, table_name, row_data, old_row_data, opt)
        cursor = DbUtil.get_cursor()
        print(f"{opt}数据")
        print(sql_and_list)
        cursor.execute(sql_and_list[0], sql_and_list[1])
