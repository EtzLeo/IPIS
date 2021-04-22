from PyQt5 import QtWidgets
from View import main_window
from Controller.DBController import DBController
from Controller.UserController import UserController
from Controller.edit_controller import EditController


class App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        """
        Конструктор класса главного окна приложения
        """
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setSortingEnabled(False)

        self.db_controller = DBController(host, user, database)
        self.user_controller = None

        self.refreshButton.clicked.connect(self.refresh_table)
        self.addButton.clicked.connect(self.add_line)
        self.editButton.clicked.connect(self.edit_line)
        self.deleteButton.clicked.connect(self.delete_line)

        self.refresh_table()

    def refresh_table(self):

        """
        Ручное обновление таблицы

        :return:
        """
        self.tableWidget.setRowCount(0)
        self.user_controller = UserController(self.db_controller.exec("select",
                                                                      ["*", 1, 1]))
        users = self.user_controller.get_users
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(len(users))
        for i in range(len(users)):
            user = list(map(str, users[i].getUserData()))
            for j in range(12):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(user[j]))
        self.tableWidget.show()

    def add_line(self):
        """
        Добавление новой строки в таблицу. Вызов вспомогательного окна и обновление таблицы после

        :return:
        """
        edit = EditController()
        edit.exec_()
        if edit.user:
            self.user_controller.currentUser = edit.user
            self.user_controller.save()
            self.db_controller.exec("insert", [params_str, tuple(map(str, edit.user.getUserData()))])
            self.refresh_table()

    def edit_line(self):
        """
        Изменение строки в таблице. Вызов вспомогательного окна и обновление таблицы после

        :return:
        """
        self.get_selected()
        if self.user_controller.currentUser:
            edit = EditController(self.user_controller.currentUser, False)
            edit.exec_()
            if edit.user:
                self.user_controller.setNewUserData(*edit.user.getUserData()[2::])
                values = list(map(str, edit.user.getUserData()))
                pairs = ["{} = \'{}\'".format(params[i], values[i]) for i in range(len(params))]
                self.db_controller.exec("update", [", ".join(pairs),
                                                   "ID_Client", self.user_controller.currentUser.id])
            self.refresh_table()


    def delete_line(self):
        """
        Удаление строки из таблицы

        :return:
        """
        self.get_selected()
        if self.user_controller.currentUser is not None:
            self.db_controller.exec("delete", ["ID_Client", self.user_controller.currentUser.id])
            self.refresh_table()

    def get_selected(self):
        """
        Получение выделенной строки таблицы, установка ее значения в качестве current_user

        :return:
        """
        person = self.tableWidget.selectedItems()
        if not person:
            self.show_warning()
        else:
            self.user_controller.findCurrentUser(int(person[4].text()), int(person[5].text()))

    @staticmethod
    def show_warning():
        """
        Показ предупреждающего окна

        :return:
        """
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

params = ('Name', 'Surname', 'Gender', 'BirthDate',
          'PassportSeries', 'PassportNumber', 'PhoneNumber',
          'RoomNumber', 'WithChildren', 'AmountOfResidents',
          'ArrivalDate', 'DepartureDate')

params_str = """(Name, Surname, Gender, BirthDate,
                 PassportSeries, PassportNumber, PhoneNumber,
                 RoomNumber, WithChildren, AmountOfResidents,
                 ArrivalDate, DepartureDate)"""