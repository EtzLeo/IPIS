import sys
from PyQt5 import QtWidgets
from Controller import app_controller


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = app_controller.App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
