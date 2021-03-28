class GenderController():
    def __init__(self, currentGender, genderList):
        """
        Создание контроллера.

        :param currentGender: текущий гендер
        :param genderList: список всех гендеров
        """
        self.__currentGender = currentGender
        self.__genderList = genderList

    @property
    def genderList(self):
        return self.__genderList

    @property
    def currentGender(self):
        return self.__currentGender

    def isNew(self):
        """
        Является ли текущий гендер новым.

        :return: в случае, если гендер новый - True, иначе - False
        """
        for gender in self.__genderList:
            if gender == self.__currentGender:
                return False
        return True

    def saveCurrent(self):
        """
        Сохранение текущего гендера в список гендеров.

        :return:
        """
        if self.isNew():
            self.__genderList.append(self.__currentGender)