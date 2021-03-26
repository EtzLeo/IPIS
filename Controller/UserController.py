from Model import UserModel


class UserController:
    currentUser = UserModel  # текущий постоялец
    isNewUser = True    # является ли постоялец вновь созданным

    def __init__(self, users):
        """
        Создание контроллера пользователя.

        :param users: список посетителей отеля
        """
        self.__users = users

    def findCurrentUser(self, passportSeries, passportNumber, arrivalDate):
        for user in self.__users:
            if (user.passportSeries == passportSeries and
                user.passportNumber == passportNumber and
                user.arrivalDate == arrivalDate):
                self.currentUser = user
                self.isNewUser = False
        return self.currentUser


    def save(self):
        """
        Сохранение данных постояльца, если он новый.
        """
        if self.isNewUser:
            self.__users.append(self.currentUser)
        self.isNewUser = False


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
        if self.isNewUser == False:
            user = UserModel.UserModel(self.currentUser.name, self.currentUser.surname,
                                       gender, birthDate, passportSeries,
                                       passportNumber, age, phoneNumber, roomNumber,
                                       withChildren, amountOfResidents, arrivalDate, departureDate
                                       )

            ind = self.__users.index(self.currentUser)
            self.__users.insert(ind, user)
            self.__users.remove(self.currentUser)
            self.currentUser = user
        return self.currentUser

    def __str__(self):
        return (str(self.__users) + " " + str(self.currentUser) + " " + str(self.isNewUser))