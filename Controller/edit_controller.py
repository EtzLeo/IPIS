from PyQt5 import QtWidgets
from View import edit_window
from Controller.GenderController import GenderController
from datetime import date


class EditController(QtWidgets.QDialog, edit_window.Ui_Dialog):
    def __init__(self,  db_controller, user=None, isNew=True):

        """
        Конструктор класса вспомогательного окна

        :param db_controller: ссылка на родительский контроллер базы данных
        :param user: ссылка на текущего пользователя
        :param isNew: является ли пользователь новым
        """

        super().__init__()
        self.setupUi()

        self.user = user
        self.isNew = isNew
        self.db_controller = db_controller
        self.gender_controller = GenderController(self.db_controller.exec("select",
                                                                          ["distinct gender", 1, 1]))

        if self.isNew:
            self.clear_form()
        else:
            self.fill_form()

        self.clearButton.click.connect(self.clear_form)
        self.saveButton.click.connect(self.save_changes)
        self.genderEdit.addItems(self.gender_controller.GET_GENDERS_LIST())
        self.genderEdit.editTextChanged.connect(self.add_gender)

    def clear_form(self):

        """
        Очистка полей формы

        :return:
        """

        self.nameEdit.setText()
        self.surnameEdit.setText()
        self.genderEdit.setCurrentIndex(-1)
        self.birthdateEdit.setDate(date.today())
        self.pseriesEdit.setText()
        self.pnumberEdit.setText()
        self.phoneEdit.setText()
        self.roomEdit.setText()
        self.childrenEdit.setCurrentIndex(-1)
        self.residentsEdit.setText()
        self.arrivalEdit.setDate(date.today())
        self.departureEdit.setDate(date.today())

    def fill_form(self):

        """
        Заполнение полей формы данными о пользователе

        :return:
        """

        fields = self.user.GET_USER_DATA()
        self.nameEdit.setText(fields[1])
        self.surnameEdit.setText(fields[2])
        self.genderEdit.setCurrentText(fields[3])
        self.birthdateEdit.setDate(fields[4])
        self.pseriesEdit.setText(fields[5])
        self.pnumberEdit.setText(fields[6])
        self.phoneEdit.setText(fields[7])
        self.roomEdit.setText(fields[8])
        self.childrenEdit.setCurrentIndex(int(fields[9]))
        self.residentsEdit.setText(fields[10])
        self.arrivalEdit.setDate(fields[11])
        self.departureEdit.setDate(fields[12])

    def add_gender(self):

        """
        Добавление нового гендера

        :return:
        """

        self.gender_controller.SET_CURRENT_GENDER(self.genderEdit.currentText())

    def get_fields(self):

        """
        Получение значений всех полей формы

        :return: кортеж всех собранных значений
        """

        return (self.nameEdit.text(),
                self.surnameEdit.text(),
                self.genderEdit.currentText(),
                self.birthdateEdit.date(),
                self.pseriesEdit.text(),
                self.pnumberEdit.text,
                self.phoneEdit.text(),
                self.roomEdit.text(),
                self.childrenEdit.currentIndex(),
                self.residentsEdit.text(),
                self.arrivalEdit.date(),
                self.departureEdit.date())

    def save_changes(self):

        """
        Сохранение изменений, внесенных в форму. Закрытие вспомогательного окна

        :return:
        """

        if self.gender_controller.IS_NEW_GENDER:
            self.gender_controller.SAVE_CURRENT()
        self.user.setNewUserData(*self.get_fields())
        if self.isNew:
            self.db_controller.exec("insert", [params, self.get_fields()])
        else:
            self.db_controller.exec("update", [params, self.get_fields(), "id_client",
                                               self.user.GET_USER_DATA()[0]])
        self.close()


params = """(`Name`, `Surname`, `Gender`, `BirthDate`, 
            "`PassportSeries`, `PassportNumber`, `PhoneNumber`, 
            "`RoomNumber`, `WithChildren`, `AmountOfResidents`, 
            "`ArrivalDate`, `DepartureDate`)"""
