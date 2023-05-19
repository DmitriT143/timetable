import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QAbstractScrollArea, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox, QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Timetable")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_teacher_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="mtuci_timetable",
                                     user="postgres",
                                     password="LRX58!",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Shedule")

        self.monday_gbox = QGroupBox("Monday")
        self.tuesday_gbox = QGroupBox("Tuesday")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.monday_gbox)
        self.shbox1.addWidget(self.tuesday_gbox)

        self._create_monday_table()
        self._create_tuesday_table()

        self.update_shedule_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Teachers")

        self.teacher_gbox = QGroupBox("Staff")

        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()

        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.teacher_gbox)

        # TODO self._create_teacher_table()

        self.shedule_tab.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(5)
        self.monday_table.setHorizontalHeaderLabels(["Starts", "Ends", "Subject", "Modify", "Remove"])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(5)
        self.tuesday_table.setHorizontalHeaderLabels(["Starts", "Ends", "Subject", "Modify", "Remove"])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(2)
        self.teacher_table.setHorizontalHeaderLabels(["Subject", "Teacher"])

        self._update_teacher_table()
        # TODO
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.mvbox)

    def _update_teacher_table(self):
        self.cursor.execute("SELECT teacher, named FROM subject ORDER BY num")
        records = list(self.cursor.fetchall())

        self.setRowCount(len(records))

        for i, e in enumerate(records):
            e = list(e)

            self.teacher_table.setItem(i, 0,
                                       QTableWidgetItem(str(e[0])))
            self.teacher_table.setItem(i, 1,
                                       QTableWidgetItem(str(e[1])))
            self.teacher_table.resizeRowsToContents()

    def _update_monday_table(self):
        self.cursor.execute("SELECT time_start, time_end, subject FROM monday ORDER BY num")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 2)

        for i, r in enumerate(records):
            r = list(r)
            joinButton_mon = QPushButton("Join")
            DeleteButton_mon = QPushButton("Delete")

            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setCellWidget(i, 3, joinButton_mon)
            self.monday_table.setCellWidget(i, 4, DeleteButton_mon)

            joinButton_mon.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 1))
            DeleteButton_mon.clicked.connect(lambda ch, num=i: self._change_day_from_table(num), 11)

        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.cursor.execute("SELECT time_start, time_end, subject FROM tuesday ORDER BY num")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 2)

        for i, r in enumerate(records):
            r = list(r)
            joinButton_tue = QPushButton("Join")
            DeleteButton_tue = QPushButton("Delete")

            self.tuesday_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.tuesday_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.tuesday_table.setCellWidget(i, 3, joinButton_tue)
            self.tuesday_table.setCellWidget(i, 4, DeleteButton_tue)

            joinButton_tue.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, 2))

        self.tuesday_table.resizeRowsToContents()

    def _change_day_from_table(self, rowNum, day):
        row = list()
        if day == '1' or '11':
            if day == '11':
                try:
                    self.cursor.execute(f"Delete from monday where num = {rowNum + 1}")
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Enter all fields")
            if day == 1:
                for i in range(self.monday_table.columnCount()):
                    try:
                        row.append(self.monday_table.item(rowNum, i).text())
                    except:
                        row.append(None)
                    try:
                        self.cursor.execute(f"UPDATE monday set time_start='{row[0]}', time_end='{row[1]}', subject='{row[2]}'"
                                            f"WHERE num={rowNum + 1}")
                        self.conn.commit()
                        return
                    except:
                        QMessageBox.about(self, "Error", "Enter all fields")

        if day == 2 or 12:
            for i in range(self.tuesday_table.columnCount()):
                try:
                    row.append(self.tuesday_table.item(rowNum, i).text())
                except:
                    row.append(None)
            try:
                self.cursor.execute(f"UPDATE tuesday set time_start='{row[0]}', time_end='{row[1]}', subject='{row[2]}'"
                                    f"WHERE num={rowNum + 1}")
                self.conn.commit()
                return
            except:
                QMessageBox.about(self, "Error", "Enter all fields")

    def _update_shedule(self):
        self._update_monday_table()
        self._update_tuesday_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
