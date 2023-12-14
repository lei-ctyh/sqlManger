from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel

from Utils import Utils


class UpdateItemModel(QStandardItemModel):
    def setData(self, index, value, role=Qt.EditRole):
        try:
            manger_self = Utils.get_manger_self()
            old_data = []
            row_data = []
            for i in range(len(manger_self.tab_header)):
                if i == index.column():
                    old_data.append(index.data())
                else:
                    old_data.append(
                        manger_self.ui.tableView.model().item(manger_self.ui.tableView.currentIndex().row(), i).text())
                row_data.append(
                    manger_self.ui.tableView.model().item(manger_self.ui.tableView.currentIndex().row(), i).text())

            sql_s_list = Utils.get_sql_and_list(manger_self.tab_header, manger_self.ui.tablename.currentText(),
                                                row_data, "edit")
            print(old_data)
            print(row_data)
            cursor = Utils.get_cursor()
            print(sql_s_list)
            cursor.execute(sql_s_list[0], sql_s_list[1])
        except Exception as e:
            Utils.show_msg(manger_self, f"修改失败:{e}")
            manger_self.execute_query()

        return super().setData(index, value, role)
