from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from mysqlx import Error


def create_db():
    try:
        db = QSqlDatabase.addDatabase('QSQLITE', 'sqlmanger')
        db.setDatabaseName('sqlmanger.db')
        if db.open():
            print('数据库连接成功')
            return db
        else:
            print('数据库连接失败: ', db.lastError().text())
    except Exception as e:
        print(e)


def create_table(db):
    try:
        query = QSqlQuery(db)
        query.exec("""
        CREATE TABLE IF NOT EXISTS `demo01`
(
    `id`      INTEGER PRIMARY KEY ,
    `name`    VARCHAR(255),
    `age`     INTEGER,
    `sex`     VARCHAR(255),
    `address` VARCHAR(255)
)
        """)
        if query.lastError().isValid():
            print('创建表失败: ', query.lastError().text())
    except Exception as e:
        print(e)


def insert_data(db):
    try:
        query = QSqlQuery(db)
        for i in range(10):
            # 随机名字
            name = '测试' + str(i)
            query.exec(f"INSERT INTO demo01 (name, age, sex, address) VALUES ('{name}', 20, '男', '北京')")
        if query.lastError().isValid():
            print('插入数据失败: ', query.lastError().text())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    _db = create_db()
    create_table(_db)
    insert_data(_db)
