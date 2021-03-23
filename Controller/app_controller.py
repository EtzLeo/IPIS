from PyQt5 import QtWidgets
from View import main_window
from Controller.DBController import DB_Controller
from Controller.UserController import UserController
from Controller.edit_controller import EditController
# from Controller.temporary.generate_line import generate


# params = "(`Name`, `Surname`, `Gender`, `BirthDate`, " \
#          "`PassportSeries`, `PassportNumber`, `PhoneNumber`, " \
#          "`RoomNumber`, `WithChildren`, `AmountOfResidents`, " \
#          "`ArrivalDate`, `DepartureDate`)"


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_controller = DB_Controller(host, user, database)
        self.user_controller = UserController("some data")

        self.refreshButton.click.connect(self.refresh_table)
        self.addButton.click.connect(self.add_line)
        self.editButton.click.connect(self.edit_line)
        self.deleteButton.click.connect(self.delete_line)

    def refresh_table(self):
        for i in range(len(self.user_controller.getUserData())):
            for j in range(12):
                self.tableWidget.setItem(i, j, str(self.user_controller.getUserData()[i][j + 1]))
        self.tableWidget.show()

    def add_line(self):
        edit = EditController(self.user_controller)
        edit.show()
        self.refresh_table()

    def edit_line(self):
        person = self.get_selected()
        if person is not None:
            edit = EditController(self.user_controller, person)
            edit.show()
            self.refresh_table()

    def delete_line(self):
        person = self.get_selected()
        if person is not None and self.ask_twice():
            self.db_controller.exec("delete", person)
            self.refresh_table()

    def get_selected(self):
        person = self.tableWidget.selectedItems()
        if person is None:
            self.show_warning()
        else:
            for user in self.user_controller.getUserData():
                if user.__passportSeries == person[4] and user.__passportNumber == person[5]:
                    return user



host = "localhost"
user = "root"
database = "hotel"
