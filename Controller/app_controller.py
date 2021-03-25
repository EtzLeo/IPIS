from PyQt5 import QtWidgets
from View import main_window
from Controller.DBController import DBController
from Controller.UserController import UserController
from Controller.edit_controller import EditController


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_controller = DBController(host, user, database)
        self.user_controller = None

        self.refreshButton.click.connect(self.refresh_table)
        self.addButton.click.connect(self.add_line)
        self.editButton.click.connect(self.edit_line)
        self.deleteButton.click.connect(self.delete_line)

        self.refresh_table()

    def refresh_table(self):
        self.user_controller = UserController(self.db_controller.exec("select",
                                                                      ["*", 1, 1]))
        for i in range(len(self.user_controller.getUserData())):
            for j in range(12):
                self.tableWidget.setItem(i, j, str(self.user_controller.getUserData()[i][j + 1]))
        self.tableWidget.show()

    def add_line(self):
        edit = EditController(self.db_controller)
        edit.show()
        self.user_controller.save()
        self.refresh_table()

    def edit_line(self):
        self.get_selected()
        if self.user_controller.current_user is not None:
            edit = EditController(self.db_controller, self.user_controller.current_user,
                                  self.user_controller.isNewUser)
            edit.show()
            self.user_controller.save()
            self.refresh_table()

    def delete_line(self):
        self.get_selected()
        if self.user_controller.current_user is not None:
            self.db_controller.exec("delete", self.user_controller.current_user.GET_USER_DATA())
            self.refresh_table()

    def get_selected(self):
        person = self.tableWidget.selectedItems()
        if person is None:
            self.show_warning()
        else:
            self.user_controller.FIND_CURRENT_USER(person[4], person[5], person[10])

    @staticmethod
    def show_warning():
        warn = QtWidgets.QMessageBox()
        warn.setWindowTitle("Внимание")
        warn.setText("Ни одна строка не выбрана")
        warn.setInformativeText("Для этой операции необходимо выбрать строку")
        warn.setIcon(QtWidgets.QMessageBox.Warning)
        warn.setDefaultButton(QtWidgets.QMessageBox.Ok)
        warn.exec()


host = "localhost"
user = "root"
database = "hotel"
