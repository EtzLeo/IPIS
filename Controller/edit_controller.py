from PyQt5 import QtWidgets
from View import edit_window


class EditController(QtWidgets.QDialog, edit_window.Ui_Dialog):
    def __init__(self, user_controller):
        super().__init__()
        self.setupUi()

        self.clearButton.click.connect(self.clear_form)
        self.saveButton.click.connect(self.save_changes)

        self.user_controller = user_controller

