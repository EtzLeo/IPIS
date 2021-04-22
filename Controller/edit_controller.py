from PyQt5 import QtWidgets
from View import edit_window
from PyQt5.QtCore import QDate
from datetime import date
from Model.UserModel import UserModel
from Controller.GenderController import GenderController


class EditController(QtWidgets.QDialog, edit_window.Ui_Dialog):
    def __init__(self, genders, user=None, isNew=True):
        """
        Конструктор класса вспомогательного окна

        :param user: ссылка на текущего пользователя
        :param isNew: является ли пользователь новым
        """
        super().__init__()
        self.setupUi(self)

        self.user = user
        self.isNew = isNew
        self.gender_controller = GenderController(genders)

        if self.isNew:
            self.clear_form()
        else:
            self.fill_form()

        self.clearButton.clicked.connect(self.clear_form)
        self.saveButton.clicked.connect(self.save_changes)
        self.genderEdit.editTextChanged.connect(self.add_gender)

    def clear_form(self):
        """
        Очистка полей формы

        :return:
        """
        self.reset_items()

        self.nameEdit.setText("")
        self.surnameEdit.setText("")
        self.genderEdit.setCurrentIndex(-1)
        self.birthdateEdit.setDate(date.today())
        self.pseriesEdit.setText("")
        self.pnumberEdit.setText("")
        self.phoneEdit.setText("")
        self.roomEdit.clear()
        self.childrenEdit.setCurrentIndex(-1)
        self.residentsEdit.clear()
        self.arrivalEdit.setDate(date.today())
        self.departureEdit.setDate(date.today())

    def reset_items(self):
        self.genderEdit.clear()
        for gender in self.gender_controller.genderList:
            self.genderEdit.addItem(str(gender))

    def fill_form(self):
        """
        Заполнение полей формы данными о пользователе

        :return:
        """
        self.reset_items()

        fields = self.user.getUserData()
        self.nameEdit.setText(fields[0])
        self.surnameEdit.setText(fields[1])
        self.genderEdit.setCurrentText(fields[2])
        self.birthdateEdit.setDate(fields[3])
        self.pseriesEdit.setText(str(fields[4]))
        self.pnumberEdit.setText(str(fields[5]))
        self.phoneEdit.setText(fields[6])
        self.roomEdit.setValue(int(fields[7]))
        self.childrenEdit.setCurrentIndex(int(fields[8]))
        self.residentsEdit.setValue(int(fields[9]))
        self.arrivalEdit.setDate(fields[10])
        self.departureEdit.setDate(fields[11])

    def add_gender(self):
        """
        Добавление нового гендера

        :return:
        """
        self.gender_controller.set_current(self.genderEdit.currentText())
        if self.gender_controller.isNew():
            self.gender_controller.saveCurrent()

    def get_fields(self):
        """
        Получение значений всех полей формы

        :return: список всех собранных значений
        """
        return [self.nameEdit.text(),
                self.surnameEdit.text(),
                self.genderEdit.currentText(),
                self.birthdateEdit.date().toPyDate(),
                self.pseriesEdit.text(),
                self.pnumberEdit.text(),
                self.phoneEdit.text(),
                self.roomEdit.text(),
                self.childrenEdit.currentIndex(),
                self.residentsEdit.text(),
                self.arrivalEdit.date().toPyDate(),
                self.departureEdit.date().toPyDate()]

    def save_changes(self):
        """
        Сохранение изменений, внесенных в форму. Закрытие вспомогательного окна

        :return:
        """
        fields = self.get_fields()
        if "" not in fields:
            if self.isNew:
                self.user = UserModel([None] + fields)
            else:
                self.user.resetWith(*fields)
            self.close()
        else:
            self.show_warning()

    @staticmethod
    def show_warning():
        """
        Показ предупреждающего окна

        :return:
        """
        warn = QtWidgets.QMessageBox()
        warn.setWindowTitle("Внимание")
        warn.setText("Некоторые поля не заполнены")
        warn.setInformativeText("Для этой операции необходимо заполнить все поля")
        warn.setIcon(QtWidgets.QMessageBox.Warning)
        warn.setDefaultButton(QtWidgets.QMessageBox.Ok)
        warn.exec()


