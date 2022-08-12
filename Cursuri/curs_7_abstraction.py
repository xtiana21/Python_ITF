# abstraction - functii abstracte
#importam ABC ca sa ne folosim de abstractizare in Python

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod #ce este cu @ se numesc decoratori, adica metoda este abstracta, e o metoda fara corp
    def accelerate(self):
        pass

    @classmethod
    def stop(self):
        print('STOP')


class Ferrari(Car):
    def accelerate(self):
        print('I am accelating from 0 to 100 in 5 seconds')

    def descriere(self):
        print('ferrari')

masina = Ferrari()
masina.descriere()
masina.accelerate()