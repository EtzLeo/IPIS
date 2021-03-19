from PyQt5 import QtWidgets, QtGui, QtSql
import window
import mysql.connector as sql

host = "localhost"
user = "root"
database = "hotel"


def get_everything():
    con = sql.connect(host=host, user=user, database=database)
    with con:
        cur = con.cursor()
        cur.execute("select * from visitors")
        return cur.fetchall()


class App(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupTable()

    def setupTable(self):
        data = get_everything()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

        self.tableWidget.show()

