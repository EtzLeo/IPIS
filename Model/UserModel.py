from Controller import UserController


class UserModel:
    def __init__(self, data):
        """
        Создание модели пользователя.

        :param data: данные о пользователе в виде списка
        """
        self.__id = data[0]
        self.__name = data[1]
        self.__surname = data[2]
        self.__gender = data[3]
        self.__birthDate = data[4]
        self.__passportSeries = data[5]
        self.__passportNumber = data[6]
        self.__phoneNumber = data[7]
        self.__roomNumber = data[8]
        self.__withChildren = data[9]
        self.__amountOfResidents = data[10]
        self.__arrivalDate = data[11]
        self.__departureDate = data[12]

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def gender(self):
        return self.__gender

    @property
    def birthDate(self):
        return self.__birthDate

    @property
    def passportSeries(self):
        return self.__passportSeries

    @property
    def passportNumber(self):
        return self.__passportNumber

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @property
    def roomNumber(self):
        return self.__roomNumber

    @property
    def withChildren(self):
        return self.__withChildren

    @property
    def amountOfResidents(self):
        return self.__amountOfResidents

    @property
    def arrivalDate(self):
        return self.__arrivalDate

    @property
    def departureDate(self):
        return self.__departureDate

    def resetWith(self, name, surname, gender, birthDate, passportSeries,
                 passportNumber, phoneNumber, roomNumber,
                 withChildren, amountOfResidents, arrivalDate, departureDate):
        """
        Изменение данных пользователя.

        :param name: имя
        :param surname: фамилия
        :param gender: гендер
        :param birthDate: дата рождения
        :param passportSeries: серия паспорта
        :param passportNumber: номер паспорта
        :param phoneNumber: номер телефона
        :param roomNumber: номер комнаты
        :param withChildren: наличие детей
        :param amountOfResidents: количество постояльцев
        :param arrivalDate: дата прибытия
        :param departureDate: дата отъезда
        """
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__birthDate = birthDate
        self.__passportSeries = passportSeries
        self.__passportNumber = passportNumber
        self.__phoneNumber = phoneNumber
        self.__roomNumber = roomNumber
        self.__withChildren = withChildren
        self.__amountOfResidents = amountOfResidents
        self.__arrivalDate = arrivalDate
        self.__departureDate = departureDate

    def getUserData(self):
        """
        Получение данных пользователя в виде списка.

        :return: список пользовательских данных
        """
        list = [self.__name,
        self.__surname,
        self.__gender,
        self.__birthDate,
        self.__passportSeries,
        self.__passportNumber,
        self.__phoneNumber,
        self.__roomNumber,
        self.__withChildren,
        self.__amountOfResidents,
        self.__arrivalDate,
        self.__departureDate]
        return list

    def __str__(self):
        """
        Перегрузка метода toString.

        :return: объект в виде строки
        """
        return (str(self.__name) + " " + str(self.__surname) + " " + str(self.__gender) + " " + str(self.__birthDate) + " "
        + str(self.__passportSeries) + " " + str(self.__passportNumber) + " " + str(self.__age) + " "
        + str(self.__phoneNumber) + " " + str(self.__roomNumber) + " " + str(self.__withChildren) + " "
        + str(self.__amountOfResidents) + " " + str(self.__arrivalDate) + " " + str(self.__departureDate))