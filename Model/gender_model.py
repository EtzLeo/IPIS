class GenderModel:
    def __init__(self, gender):
        if type(gender) != str:
            self.gender = gender[0]
        else:
            self.gender = gender

    def __str__(self):
        return str(self.gender)
