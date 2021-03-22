from PyQt5 import QtWidgets
from View import window
from Controller.DBController import DB_Controller
# from Controller.temporary.generate_line import generate


host = "localhost"
user = "root"
database = "hotel"

params = "(`Name`, `Surname`, `Gender`, `BirthDate`, " \
         "`PassportSeries`, `PassportNumber`, `PhoneNumber`, " \
         "`RoomNumber`, `WithChildren`, `AmountOfResidents`, " \
         "`ArrivalDate`, `DepartureDate`)"


class App(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controller = DB_Controller(host, user, database)

        # self.deleteLast()
        # self.addNew()
        # self.updateOld()
        self.setupTable()

    def updateOld(self):
        self.controller.exec("update", ("surname", "\'Smith\'", "id_client", 33))

    def deleteLast(self):
        self.controller.exec("delete", ("id_client", 31))

    def addNew(self):
        # new_person = generate()
        self.controller.exec("insert", (params, new_person))

    def setupTable(self):
        data = self.controller.exec("select", ("*", 1, 1))

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]) - 1)

        for i in range(len(data)):
            for j in range(len(data[i]) - 1):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j + 1])))

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.show()

