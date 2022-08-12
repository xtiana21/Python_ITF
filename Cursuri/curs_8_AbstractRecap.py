from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura* self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua raza e {latura}')
        self.__latura == latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura == None

patrat = Patrat(3)
print(patrat.aria())
print(patrat.latura)
patrat.latura = 5
print(patrat.aria())