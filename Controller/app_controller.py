from PyQt5 import QtWidgets
from View import window
from Controller.DBController import DB_Controller


host = "localhost"
user = "root"
database = "hotel"


class App(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupTable()

    def setupTable(self):
        controller = DB_Controller(host, user, database)
        data = controller.exec("select")

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for i in range(len(data)):
            for j in range(len(data[i])):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))

        self.tableWidget.show()

