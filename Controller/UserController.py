from Model.UserModel import UserModel


class UserController:
    currentUser = None
    """
        Текущий постоялец.
    """

    isNewUser = True
    """
    Является ли постоялец вновь созданным
    """

    def __init__(self, users):
        """
        Создание контроллера пользователя.

        :param users: список посетителей отеля
        """

        self.__users = [UserModel(user) for user in users]

    @property
    def get_users(self):
        return self.__users

    def findCurrentUser(self, passportSeries, passportNumber):
        """
        Поиск текущего пользователя в списке пользователей.

        :param passportSeries: серия паспорта
        :param passportNumber: номер паспорта
        :param arrivalDate: дата заселения
        :return: текущий пользователь
        """
        for user in self.__users:
            if (user.passportSeries == passportSeries and
                    user.passportNumber == passportNumber):
                self.currentUser = user
                self.isNewUser = False
                break
        return self.currentUser

    def save(self):
        """
        Сохранение данных постояльца, если он новый.
        """
        if self.isNewUser:
            self.__users.append(self.currentUser)
        self.isNewUser = False

    def setNewUserData(self, gender, birthDate, passportSeries,
                       passportNumber, phoneNumber, roomNumber,
                       withChildren, amountOfResidents, arrivalDate, departureDate):
        """
        Изменение данных постояльца.

        :return: постоялец с новым набором данных
        """
        if not self.isNewUser:
            user = UserModel([self.currentUser.id, self.currentUser.name, self.currentUser.surname,
                             gender, birthDate, passportSeries,
                             passportNumber, phoneNumber, roomNumber,
                             withChildren, amountOfResidents, arrivalDate, departureDate])

            ind = self.__users.index(self.currentUser)
            self.__users.insert(ind, user)
            self.__users.remove(self.currentUser)
            self.currentUser = user
        return self.currentUser

    def drop_current_user(self):
        self.currentUser = None
        self.isNewUser = True

    def __str__(self):
        """
        Перегрузка метода toString.

        :return: объект в виде строки
        """
        return (str(self.__users) + " " + str(self.currentUser) + " " + str(self.isNewUser))
