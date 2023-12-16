for colTuple, colInfo in zip(value, self.tab_header):
    if colTuple is None:
        # This value is NULL
        original_value = None
        display_value = "NULL"
    elif colInfo[3].upper() in ['DATE', 'DATETIME']:
        # Assuming the column is of data type 'DATE' or similar
        original_value = QDateTime.fromString(str(colTuple), 'yyyy-MM-dd HH:mm:ss')
        display_value = original_value.toString(Qt.ISODate)
    elif colInfo[3].upper() in ['INT', 'TINYINT', 'SMALLINT', 'MEDIUMINT', 'BIGINT']:
        original_value = int(colTuple)
        display_value = str(original_value)
    elif colInfo[3].upper() in ['FLOAT', 'DOUBLE', 'DECIMAL']:
        original_value = float(colTuple)
        display_value = str(original_value)
    elif colInfo[3].upper() in ['CHAR', 'VARCHAR', 'TINYTEXT', 'TEXT', 'MEDIUMTEXT', 'LONGTEXT']:
        original_value = str(colTuple)
        display_value = original_value
    else:
        # Handle other data types as needed
        original_value = colTuple
        display_value = str(original_value)

    col = QStandardItem(display_value)
    col.setData(original_value, Qt.UserRole)
    row.append(col)