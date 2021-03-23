import UserModel

class UserController:
    def __init__(self, users, currentUser, isNewUser):
        """
        Создание контроллера пользователя.

        :param users: список посетителей отеля
        :param currentUser: текущий постоялец
        :param isNewUser: является ли постоялец вновь созданным
        """
        self.__users = users
        self.__currentUser = currentUser
        self.__isNewUser = isNewUser


    def save(self):
        """
        Сохранение данных постояльца, если он новый.
        """
        if self.__isNewUser:
            self.__users.append(self.__currentUser)
        self.__isNewUser = False


    def getUserData(self):
        """
        Получение сохраненного списка постояльцев.

        :return: список постояльцев
        """
        return self.__users

    def setNewUserData(self, gender, birthDate, passportSeries,
                 passportNumber, age, phoneNumber, roomNumber,
                 withChildren, amountOfResidents, arrivalDate, departureDate):
        """
        Изменение данных постояльца.

        :return: постоялец с новым набором данных
        """
        if self.__isNewUser == False:
            user = UserModel.UserModel(self.__currentUser.name, self.__currentUser.surname,
                             gender, birthDate, passportSeries,
                             passportNumber, age, phoneNumber, roomNumber,
                             withChildren, amountOfResidents, arrivalDate, departureDate
                             )

            ind = self.__users.index(self.__currentUser)
            self.__users.insert(ind, user)
            self.__users.remove(self.__currentUser)
            self.__currentUser = user
        return self.__currentUser

    def __str__(self):
        return (str(self.__users) + " " + str(self.__currentUser) + " " + str(self.__isNewUser))