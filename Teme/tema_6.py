# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

print('Exercitiul 1')
print('....................................................................................')

''' Clasa Cerc
Atribute: raza, culoare

Constructor pt ambele atribute

Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()'''
from pip._internal.utils.misc import tabulate

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza {self.raza}.')

    def aria(self):
        return self.raza*self.raza*3.14

    def diametru(self):
        return 2*self.raza

    def circumferinta(self):
        return 3.14*self.diametru()

cerc_1 = Cerc(4,'albastru')
cerc_1.descriere_cerc()
print(f'Cercul are aria {cerc_1.aria()}')
print(f'Cercul are diametrul {cerc_1.diametru()}')
print(f'Cercul are circumferinta {cerc_1.circumferinta()}')
print('....................................................................................')

cerc_2 = Cerc(2, 'galben')
cerc_2.descriere_cerc()
print(f'Al doilea cerc are aria {cerc_2.aria()}')
print(f'Al doilea cerc are diametrul {cerc_2.diametru()}')
print(f'Al doilea cerc are circumferinta {cerc_2.circumferinta()}')
print('....................................................................................')

cerc_3 = Cerc(7, 'violet')
cerc_3.descriere_cerc()
print(f'Ultimul cerc are aria {cerc_3.aria()}')
print(f'Ultimul cerc are diametrul {cerc_3.diametru()}')
print(f'Ultimul cerc are circumferinta {cerc_3.circumferinta()}')


print('\n')
print('Exercitiul 2')
print('....................................................................................')

''' Clasa Dreptunghi

Atribute: lungime, latime, culoare

Constructor pt toate atributele

Metode:
- descrie()
- aria()
- perimetrul()
- schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. 
Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. 
Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si are culoarea {self.culoare}')

    def aria_dreptunghi(self):
        return self.lungime * self.latime

    def perimetru_dreptunghi(self):
        return 2 * (self.lungime + self.latime)

    def schimb_culoare(self, noua_culoare):
        self.culoare = noua_culoare

dreptunghi_1 = Dreptunghi(2,4, 'verde')
dreptunghi_1.descriere_dreptunghi()
print(f'Dreptunghiul 1 are aria {dreptunghi_1.aria_dreptunghi()}')
print(f'Dreptunghiul 1 are perimetrul {dreptunghi_1.perimetru_dreptunghi()}')
dreptunghi_1.schimb_culoare('roz')
dreptunghi_1.descriere_dreptunghi()
print('....................................................................................')

dreptunghi_2 = Dreptunghi(2,3,'gri')
dreptunghi_2.descriere_dreptunghi()
print(f'Dreptunghiul 2 are aria {dreptunghi_2.aria_dreptunghi()}')
print(f'Dreptunghiul 2 are perimetrul {dreptunghi_2.perimetru_dreptunghi()}')
dreptunghi_2.schimb_culoare('negru')
dreptunghi_2.descriere_dreptunghi()
print('....................................................................................')

dreptunghi_3 = Dreptunghi(4,6,'rosu')
dreptunghi_3.descriere_dreptunghi()
print(f'Dreptunghiul 3 are aria {dreptunghi_3.aria_dreptunghi()}')
print(f'Dreptunghiul 3 are perimetrul {dreptunghi_3.perimetru_dreptunghi()}')
dreptunghi_3.schimb_culoare('portocaliu')
dreptunghi_3.descriere_dreptunghi()


print('\n')
print('Exercitiul 3')
print('....................................................................................')

''' Clasa Angajat

Atribute: nume, prenume, salariu

Constructor pt toate atributele

Metode:
- descrie()
- nume_complet()
- salariu_lunar()
- salariu_anual()
- marire_salariu(procent)'''


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        print(f'Angajatul are numele {self.nume}, prenumele {self.prenume} si castiga salariul de {self.salariu} lei')

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return 12*self.salariu

    def marire_salariu(self, n):
        return self.salariu + self.salariu * n/100

angajat_1 = Angajat('Popescu', 'Anca', 4500)
angajat_1.descriere_angajat()
print(f'Numele complet al angajatului 1 este {angajat_1.nume_complet()}')
print(f'Salariul lunar al angajaului {angajat_1.nume_complet()} este {angajat_1.salariu_lunar()} lei')
print(f'Salariul anual al angajatului {angajat_1.nume_complet()} este {angajat_1.salariu_anual()} lei')
print(f'In urma maririi de salariu, angajatul {angajat_1.nume_complet()} primeste salariul de {angajat_1.marire_salariu(5)} lei')
print('....................................................................................')

angajat_2 = Angajat('Ionescu', 'Marian', 8700)
angajat_2.descriere_angajat()
print(f'Numele complet al angajatului 1 este {angajat_2.nume_complet()}')
print(f'Salariul lunar al angajaului {angajat_2.nume_complet()} este {angajat_2.salariu_lunar()} lei')
print(f'Salariul anual al angajatului {angajat_2.nume_complet()} este {angajat_2.salariu_anual()} lei')
print(f'In urma maririi de salariu, angajatul {angajat_2.nume_complet()} primeste salariul de {angajat_2.marire_salariu(5)} lei')


print('\n')
print('Exercitiul 4')
print('....................................................................................')

''' Clasa Cont

Atribute: iban, titular_cont, sold

Constructor pentru toate

Metode:
- afisare_sold() - Titularul x are in contul y suma de n lei
- debitare_cont(suma)
- creditare_cont(suma)'''


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')

    def debitare_cont(self, n):
        print(f'Titularul {self.titular_cont} a cheltuit suma de {n} lei, iar soldul a ramas de {self.sold - n} lei')

    def creditare_cont(self, n):
        print(f'Titularul {self.titular_cont} a incasat suma de {n} lei, iar acesta are acum disponibil in cont {self.sold + n} lei')

client_1 = Cont('RO001', 'Marin Andrei', 3400)
client_1.afisare_sold()
client_1.debitare_cont(430)
client_1.creditare_cont(700)
print('....................................................................................')

client_2 = Cont('RO002', 'Cristea Adina', 2700)
client_2.afisare_sold()
client_2.debitare_cont(230)
client_2.creditare_cont(150)


#BONUS: (daca aveti timp si doriti sa lucrati suplimentar)


print('\n')
print('Exercitiul 5')
print('....................................................................................')

''' Clasa Factura

Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
Constructor: toate atributele, fara serie

Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total
Telefon |      7       |       700       | 49000'''


from tabulate import tabulate
from datetime import datetime

class Factura:
    seria = 'SR'
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def descriere(self):
        print (f'{self.seria}, {self.numar}, {self.nume_produs}, {self.cantitate}, {self.pret_buc}')

    def schimba_cantitatea(self, n):
        self.cantitate = n
        print(f'Noua cantitate este {n}')

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        print(f'Noul pret este {pret}')

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        print(f'Noul nume al produsului este {nume}')

    def genereaza_factura(self):
        print(f'Factura seria {self.seria}, numarul {self.numar}')
        azi = datetime.now()
        print(f'Data si ora {azi}')
        col_names = ['Produs', 'cantitate', 'pret bucata', 'total']
        data = [[ self.nume_produs, self.cantitate, self.pret_buc, self.cantitate*self.pret_buc]]
        print(tabulate(data, headers=col_names))


produs1 = Factura(11, 'Masina de spalat', 1, 2500)
produs1.descriere()
produs1.schimba_cantitatea(2)
produs1.schimba_pretul(2000)
produs1.schimba_nume_produs('Masina de spalat vase')
produs1.descriere()
produs1.genereaza_factura()
print('....................................................................................')

produs2 = Factura(12, 'Laptop', 1, 4500)
produs2.descriere()
produs2.schimba_cantitatea(3)
produs2.schimba_pretul(3000)
produs2.schimba_nume_produs('Asus')
produs2.descriere()
produs2.genereaza_factura()

print('\n')
print('Exercitiul 6')
print('....................................................................................')

''' Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)

Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
- descrie() (se vor printa toate atributele, inafara de culori_disponibile)
- inmatriculare() - va schimba atributul inmatriculata in True
- vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
- accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
- franeaza() - masina se va opri si va avea viteza 0'''


class Masina:
    marca = 'Audi'
    viteza_actuala = 0
    culoare = 'alb'
    culori_disponibile = {'alb', 'negru', 'gri', 'rosu', 'albastru'}
    inmatriculat = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        print(f'{self.marca}, {self.viteza_actuala}, {self.culoare}, {self.inmatriculat}')

    def vopseste(self, culoare_noua):
        if culoare_noua in self.culori_disponibile:
            print(f'Masina se vopseste in noua culoare aleasa {culoare_noua}')
        else:
            print('Culoarea aleasa nu se afla in culorile disponibile')

    def accelereaza(self, viteza):
        if viteza < 0:
            print(f'Viteza {viteza} este negativa')
        elif viteza > self.viteza_maxima:
            print(f'Masina accelereaza maxim pana la {self.viteza_maxima} ')

    def franeaza(self):
        print('Masina se va opri si va avea viteza 0 km/h')


masina1 = Masina
masina1.descriere(Masina)
masina1.inmatriculat = True
masina1.descriere(Masina)
masina1.vopseste(Masina,'gri')
masina1.vopseste(Masina, 'navi')
masina1.accelereaza(Masina, -1)
masina1.franeaza(Masina)


print('\n')
print('Exercitiul 7')
print('....................................................................................')

''' Clasa To do list
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)

La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
- adauga_task(nume, descriere) - se va adauga in dict
- finalizeaza_task(nume) - se va sterge din dict
- afiseaza_todo_list() - doar cheile
-afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare

Daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
Daca raspunde da - il cerem detalii task si salvam nume+detalii in dict'''


class ToDoList:
    dict = {}

    def adauga_task(self, nume, descriere):
        self.dict[nume] = descriere

    def finalizare_task(self, nume):
        try:
            self.dict.pop(nume)
        except KeyError as e:
            print('Taskul nu se afla in lista de to do')

    def afiseaza_todolist(self):
        for key in self.dict.keys():
            print(key)


    def afiseaza_detalii_suplimentare(self, nume):
        if nume not in self.dict.keys():
            raspuns = input('Vrei sa il adaug in dict?')
            if raspuns.lower() == 'da':
                detalii = input ('da-mi detalii pt task')
                self.dict[nume] = detalii
            else:
                print('la revedere')
        else:
            print(f'Taskul {nume}, are ca descriere {self.dict.get[nume]}')

to_do = ToDoList()
to_do.adauga_task('stergere tabla', 'curatare burete')
to_do.afiseaza_todolist()
to_do.finalizare_task('testeaza emag')

to_do.afiseaza_detalii_suplimentare('tema 7')

