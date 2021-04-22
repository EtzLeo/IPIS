from Model.gender_model import GenderModel


class GenderController:
    def __init__(self, genderList):
        """
        Создание контроллера.

        :param currentGender: текущий гендер
        :param genderList: список всех гендеров
        """
        self.__currentGender = None
        self.__genderList = [GenderModel(gender) for gender in genderList]

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

    def set_current(self, gender):
        self.__currentGender = GenderModel(gender)
