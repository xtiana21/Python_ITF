'''ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria (optional)
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

INHERITANCE
Clasa Patrat - mosteneste FormaGeometrica
constructor pt latura
ENCAPSULATION
latura este proprietate privata
Implementati getter, setter, deleter pt latura
Implementati metoda ceruta de interfata (optional, doar daca ati ales sa implementati metoda abstracta aria)

Clasa Cerc - mosteneste FormaGeometrica
constructor pt raza
raza este proprietate privata
Implementati getter, setter, deleter pt raza
Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte (optional, doar daca ati ales sa implementati metoda abstracta aria)

POLYMORPHISM
Definiti o noua metoda descrie - printati ‘Eu nu am colturi’


Creati un obiect de tip Patrat si jucati-va cu metodele lui
Creati un obiect de tip Cerc si jucati-va cu metodele lui'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14                                # contine un field

    @abstractmethod
    def aria(self):                          # contine metoda abstracta
        pass

    def descrie(self):                       # contine o metoda cu un print
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        return self.__latura * self.__latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print (f'Getter: latura este {self.__latura}')

    @latura.setter
    def latura(self, latura):
        print(f'Noua latura este: {latura}')
        self.__latura == latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura == None


class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: raza este {self.__raza}')

    @raza.setter
    def raza(self, raza):
        print(f'Setter: noua raza este {raza}')
        self.__raza == raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: am sters raza')

    def descrie(self):
        print('Eu nu am colturi')

    def aria(self):
        return self.__raza * self.__raza * self.PI

patrat = Patrat(3)
print(patrat.aria)
patrat.descrie
patrat.latura

cerc = Cerc(4)
print(cerc.aria)
print(cerc.raza)
cerc.descrie
cerc.raza







