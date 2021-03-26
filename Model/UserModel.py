class UserModel:
    def __init__(self, date):
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

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    def resetWith(self, name, surname, gender, birthDate, passportSeries,
                 passportNumber, age, phoneNumber, roomNumber,
                 withChildren, amountOfResidents, arrivalDate, departureDate):
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
        return (str(self.__name) + " " + str(self.__surname) + " " + str(self.__gender) + " " + str(self.__birthDate) + " "
        + str(self.__passportSeries) + " " + str(self.__passportNumber) + " " + str(self.__age) + " "
        + str(self.__phoneNumber) + " " + str(self.__roomNumber) + " " + str(self.__withChildren) + " "
        + str(self.__amountOfResidents) + " " + str(self.__arrivalDate) + " " + str(self.__departureDate))