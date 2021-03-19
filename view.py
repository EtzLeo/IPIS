import sys, main_view
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = main_view.App()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
