VERSION = "0.0.2 Alpha"
DATE = "05.04.2026"

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QMessageBox, QFileDialog
from compare.tools import compare, get_table
from optimize.tools import getTableByRequest, is_number

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QToolBox, QTableView,
    QVBoxLayout, QWidget, QLabel, QHeaderView,QStyle
)

from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtGui import QColor, QIcon

import pandas as pd
from pathlib import Path
from datetime import datetime
import os


def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работает для dev и PyInstaller"""
    if hasattr(sys, '_MEIPASS'):
        # Путь во время выполнения EXE
        return os.path.join(sys._MEIPASS, relative_path)
    # Путь во время разработки
    return os.path.join(os.path.abspath("."), relative_path)

class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                if pd.isna(self._data.iloc[index.row(), index.column()]):
                    return ""
                columns = self._data.columns.array
                if is_number(self._data.iloc[index.row(), index.column()]) and columns[index.column()] != "Корпус":
                    return f"{float(self._data.iloc[index.row(), index.column()]):g}"
                    #return float(self._data.iloc[index.row(), index.column()])
                else:
                    return str(self._data.iloc[index.row(), index.column()])

        return None

    def sort(self, column, order):
            """Метод вызывается автоматически при клике на заголовок"""
            self.layoutAboutToBeChanged.emit() # Уведомляем о начале изменений

            # Сортируем сам DataFrame
            ascending = (order == Qt.AscendingOrder)
            col_name = self._data.columns[column]
            self._data.sort_values(by=col_name, ascending=ascending, inplace=True)

            self.layoutChanged.emit() # Уведомляем о завершении

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            elif orientation == Qt.Vertical:
                return str(self._data.index[section])

        return None

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("BOMTools " + VERSION)
        self.ui.centralwidget.setLayout(self.ui.gridLayout)
        self.ui.groupBox.setLayout(self.ui.gridLayout_4)
        self.ui.compare.setLayout(self.ui.gridLayout_5)
        self.ui.optimization.setLayout(self.ui.gridLayout_2)

        self.ui.compareButton.clicked.connect(self.compareButton_clicked)
        self.ui.optimizeButton.clicked.connect(self.optimizeButton_clicked)

        self.ui.open_first.clicked.connect(self.open_first_clicked)
        self.ui.open_second.clicked.connect(self.open_second_clicked)

        self.ui.action.triggered.connect(self.show_about_dialog)

    def optimizeButton_clicked(self):

        first_file_name = self.ui.first_file.text()
        first_file_count_column = self.ui.first_count.text()
        first_file_pn_column = self.ui.first_pn.text()
        first_file_skip_row = int(self.ui.first_skip.text())

        table = get_table(first_file_name, f"{first_file_count_column}, C, {first_file_pn_column}, F, L", first_file_skip_row, ["count", "ref", "pn", "tm", "dpn"])

        if self.ui.exceptDNP.isChecked():
            table = table[table['tm'] != 'DNP']
            table = table[table['tm'] != 'NM']

        #table = table.fillna('X')

        request = self.ui.requestLine.text()

        optimizeTable = getTableByRequest(table, request)

        tableView = self.ui.tableView

        tableView.setModel(PandasModel(optimizeTable))
        #tableView.resizeColumnsToContents()
        tableView.setAlternatingRowColors(True)
        tableView.verticalHeader().hide()
        tableView.setSortingEnabled(True)

        tableView.setShowGrid(False)
        tableView.setStyleSheet("""
            QTableView {

                padding-top: 3px;
                padding-bottom: 5px;

                background-color: white;

                selection-background-color: #3498db;
                selection-color: white;
                border: 1px solid rgba(0,0,0,0);
            }
            QTableView::item {
                border: 1px solid #cccccc;
                padding: 5px;
            }
            QHeaderView::section {
                padding: 4px;
                font-weight: bold;
                border: 1px solid #cccccc;
            }
        """)
        header = tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionsMovable(True)
        #tableView.resizeColumnsToContents()


        pass

    def compareButton_clicked(self):

        first_file_name = self.ui.first_file.text()
        first_file_count_column = self.ui.first_count.text()
        first_file_pn_column = self.ui.first_pn.text()
        first_file_skip_row = int(self.ui.first_skip.text())

        first_table = get_table(first_file_name, f"{first_file_count_column}, {first_file_pn_column}", first_file_skip_row, ["count", "pn"])

        second_file_name = self.ui.second_file.text()
        second_file_count_column = self.ui.second_count.text()
        second_file_pn_column = self.ui.second_pn.text()
        second_file_skip_row = int(self.ui.second_skip.text())

        second_table = get_table(second_file_name, f"{second_file_count_column}, {second_file_pn_column}", second_file_skip_row, ["count", "pn"])

        kLevenshtein = float(self.ui.koef.text())

        dfs = compare(first_table, second_table, kLevenshtein)

        #print(dfs)

        titles = ["Без изменений", "Изменилось количество", "Изменилось написание", "Изменилось количество и написание", "Убраны", "Добавлены"]

        for i in reversed(range(self.ui.toolBox.count())):
            widget = self.ui.toolBox.widget(i)
            self.ui.toolBox.removeItem(i)
            widget.deleteLater()

        for i, (df, title) in enumerate(zip(dfs, titles)):

            if len(df.columns) == 2:
                df.columns = ["Кол., шт (1)", "Номенклатура (1)"]
            else:
                df.columns = ["Кол., шт (1)", "Номенклатура (1)", "Кол., шт (2)", "Номенклатура (2)"]

            view = QTableView()
            view.setModel(PandasModel(df))
            view.resizeColumnsToContents()

            view.setColumnWidth(0, 200)
            view.setColumnWidth(1, 200)
            view.setColumnWidth(2, 200)
            view.setColumnWidth(3, 200)
            view.setAlternatingRowColors(True)
            view.verticalHeader().hide()

            view.setShowGrid(False)


            view.setStyleSheet("""
                QTableView {

                    padding-top: 3px;
                    padding-bottom: 5px;

                    background-color: white;

                    selection-background-color: #3498db;
                    selection-color: white;
                    border: 1px solid rgba(0,0,0,0);
                }
                QTableView::item {
                    border: 1px solid #cccccc;
                    padding: 5px;
                }
                QHeaderView::section {
                    padding: 4px;
                    font-weight: bold;
                    border: 1px solid #cccccc;
                }
            """)
            #icon = self.style().standardIcon(QStyle.SP_TitleBarNormalButton)

            match i:
                case 0:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/check.png"))
                    else:
                        icon = QIcon(resource_path("icons/warning.png"))
                case 1:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/warning.png"))
                    else:
                        icon = QIcon(resource_path("icons/check.png"))
                case 2:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/warning.png"))
                    else:
                        icon = QIcon(resource_path("icons/check.png"))
                case 3:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/warning.png"))
                    else:
                        icon = QIcon(resource_path("icons/check.png"))
                case 4:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/warning.png"))
                    else:
                        icon = QIcon(resource_path("icons/check.png"))
                case 5:
                    if len(df) > 0:
                        icon = QIcon(resource_path("icons/warning.png"))
                    else:
                        icon = QIcon(resource_path("icons/check.png"))

            self.ui.toolBox.addItem(view, icon, f"{title} ({len(df)})")


#padding-left: 10px;

        self.ui.toolBox.setStyleSheet("""
            QToolBox {

            }

            QToolBox::tab {
                            background-color: #f5f5f5;
                            padding: -2px 10px;
                            font-size: 16px;
                            border: 1px solid #f5f5f5;
                            border-radius: 10px;
                            margin: 0px;
                        }

                        QToolBox::tab:selected {
                            background-color: #EBEBEB;
                            border: 1px solid #CCCCCC;
                        }

                        QToolBox::tab:hover {
                            background-color: #3399FF;
                            border: 1px solid #3399FF;
                            color: white;
                        }

        """)


    def open_first_clicked(self):

        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path)
        self.ui.first_file.setText(f"{file_path}")
        self.ui.label.setText(f"{temp_time}")


    def open_second_clicked(self):

        file_path = self.open_file_dialog()
        temp_time = self.get_time_modification(file_path)
        self.ui.second_file.setText(f"{file_path}")
        self.ui.label_5.setText(f"{temp_time}")


    def get_time_modification(self, file_path_str):
        """
        Возвращает время последней модификации файла
        """
        file_path = Path(file_path_str)
        modification_time = file_path.stat().st_mtime
        modification_date = datetime.fromtimestamp(modification_time)
        return modification_date.strftime("%Y-%m-%d %H:%M:%S")

    def open_file_dialog(self):
        """Открывает диалоговое окно для выбора файла"""
        options = QFileDialog.Options()  # Опции диалогового окна
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл",
            "",  # Начальная директория (пустая строка означает текущую директорию)
            "Все файлы (*)",  # Фильтр типов файлов
            options=options
        )

        return file_path

    def show_about_dialog(self):
        """Показывает диалог 'О программе'"""
        QMessageBox.about(
            self,
            "О программе",
            "Название программы: searchBASE    \n"
            "Версия: " + VERSION + "\n"
            "Автор: Лев Кириллов\n"
            "Дата сборки: " + DATE + "\n"
            "\n"
            "Программа для анализа, проверки, сравнения перечня элементов."
        )






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

