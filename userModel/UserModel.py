class UserModel:
    def __init__(self, name, surname, gender, birthDate, passportSeries,
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
