import sys
from PyQt5 import QtWidgets
from Controller.app_controller import App


def main():
    """
    Запуск программы

    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
