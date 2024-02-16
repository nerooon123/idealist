import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


class DatabaseSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NEROOOON")
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.search_layout = QHBoxLayout()
        self.search_line_edit = QLineEdit()
        self.search_button = QPushButton("Поиск")
        self.search_layout.addWidget(self.search_line_edit)
        self.search_layout.addWidget(self.search_button)

        self.layout.addLayout(self.search_layout)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(13)
        self.result_table.setHorizontalHeaderLabels(["field1", "field2", "field3", "field4", "field5", "field6", "field7", "field8", "field9", "field10", "field11", "field12", "field13"])
        self.layout.addWidget(self.result_table)

        self.search_button.clicked.connect(self.search_database)

    def search_database(self):
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName("nerooon.db")

        if not database.open():
            print("Не удалось открыть БД")
            return

        query = QSqlQuery()
        search_text = self.search_line_edit.text()

        query.prepare("SELECT * FROM kari_club WHERE field1 LIKE :searchText OR field2 LIKE :searchText OR field3 LIKE:searchText OR field4 LIKE:searchText OR field5 LIKE:searchText OR field6 LIKE:searchText OR field7 LIKE:searchText OR field8 LIKE:searchText OR field9 LIKE:searchText OR field10 LIKE:searchText OR field11 LIKE:searchText OR field12 LIKE:searchText OR field13 LIKE:searchText")
        query.bindValue(":searchText", f"%{search_text}%")
        query.exec_()

        self.result_table.setRowCount(0)

        while query.next():
            field1 = QTableWidgetItem(str(query.value(0)))
            field2 = QTableWidgetItem(query.value(1))
            field3 = QTableWidgetItem(query.value(2))
            field4 = QTableWidgetItem(query.value(3))
            field5 = QTableWidgetItem(query.value(4))
            field6 = QTableWidgetItem(query.value(5))
            field7 = QTableWidgetItem(query.value(6))
            field8 = QTableWidgetItem(query.value(7))
            field9 = QTableWidgetItem(query.value(8))
            field10 = QTableWidgetItem(query.value(9))
            field11 = QTableWidgetItem(query.value(10))
            field12 = QTableWidgetItem(query.value(11))
            field13 = QTableWidgetItem(query.value(12))

            row_position = self.result_table.rowCount()
            self.result_table.insertRow(row_position)
            self.result_table.setItem(row_position, 0, field1)
            self.result_table.setItem(row_position, 1, field2)
            self.result_table.setItem(row_position, 2, field3)
            self.result_table.setItem(row_position, 3, field4)
            self.result_table.setItem(row_position, 4, field5)
            self.result_table.setItem(row_position, 5, field6)
            self.result_table.setItem(row_position, 6, field7)
            self.result_table.setItem(row_position, 7, field8)
            self.result_table.setItem(row_position, 8, field9)
            self.result_table.setItem(row_position, 9, field10)
            self.result_table.setItem(row_position, 10, field11)
            self.result_table.setItem(row_position, 11, field12)
            self.result_table.setItem(row_position, 12, field13)

        if self.result_table.rowCount() == 0:
            self.result_label.setText("Ничего не найдено")
        else:
            self.result_label.setText(f"Результат: {self.result_table.rowCount()}")

        database.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DatabaseSearch()
    window.show()

    sys.exit(app.exec_())