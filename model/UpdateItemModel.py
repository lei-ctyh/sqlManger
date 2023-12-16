from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel

from utils.BusinessUtil import BusinessUtil
from utils.ContainerUtil import ContainerUtil
from utils.DbUtil import DbUtil


class UpdateItemModel(QStandardItemModel):
    def setData(self, index, value, role=Qt.EditRole):
        try:
            manger_self = ContainerUtil.get_manger_self()
            old_data = []
            row_data = []
            for i in range(len(manger_self.tab_header)):
                if i == index.column():
                    row_data.append(value)
                else:
                    row_data.append(
                        manger_self.ui.tableView.model().item(manger_self.ui.tableView.currentIndex().row(), i).text())
                old_data.append(manger_self.ui.tableView.model().item(manger_self.ui.tableView.currentIndex().row(), i).text())

            DbUtil.crud_data(manger_self.tab_header, manger_self.ui.tablename.currentText(), row_data, old_data, "edit")
        except Exception as e:
            manger_self = ContainerUtil.get_manger_self()
            BusinessUtil.show_msg(manger_self, f"修改失败:{e}")
            return super().setData(index, index.data(), role)

        return super().setData(index, value, role)
