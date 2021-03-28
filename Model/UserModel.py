from Controller import UserController


class UserModel:
    def __init__(self, date):
        """
        Создание модели пользователя.

        :param date: данные о пользователе в виде списка
        """
        self.__name = date[0]
        self.__surname = date[1]
        self.__gender = date[2]
        self.__birthDate = date[3]
        self.__passportSeries = date[4]
        self.__passportNumber = date[5]
        self.__age = date[6]
        self.__phoneNumber = date[7]
        self.__roomNumber = date[8]
        self.__withChildren = date[9]
        self.__amountOfResidents = date[10]
        self.__arrivalDate = date[11]
        self.__departureDate = date[12]

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
    def age(self):
        return self.__age

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
                 passportNumber, age, phoneNumber, roomNumber,
                 withChildren, amountOfResidents, arrivalDate, departureDate):
        """
        Изменение данных пользователя.

        :param name: имя
        :param surname: фамилия
        :param gender: гендер
        :param birthDate: дата рождения
        :param passportSeries: серия паспорта
        :param passportNumber: номер паспорта
        :param age: возраст
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
        self.__age = age
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
        self.__age,
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