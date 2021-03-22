from PyQt5 import QtWidgets
from View import main_window
from Controller.DBController import DB_Controller
# from Controller.temporary.generate_line import generate


host = "localhost"
user = "root"
database = "hotel"

params = "(`Name`, `Surname`, `Gender`, `BirthDate`, " \
         "`PassportSeries`, `PassportNumber`, `PhoneNumber`, " \
         "`RoomNumber`, `WithChildren`, `AmountOfResidents`, " \
         "`ArrivalDate`, `DepartureDate`)"


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
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

    def deleteLast(self, id_client):
        self.controller.exec("delete", ("id_client", id_client))

    def addNew(self, new_person):
        # new_person = generate()
        self.controller.exec("insert", (params, new_person))

    def get_everything(self):
        return self.controller.exec("select", ("*", 1, 1))

    def setupTable(self):
        data = self.get_everything()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]) - 1)

        for i in range(len(data)):
            for j in range(len(data[i]) - 1):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j + 1])))

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.show()

