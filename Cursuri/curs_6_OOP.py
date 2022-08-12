class Caine:                #definim o clasa
    rasa = 'labrador'       #oferin atribute/field-uri
    varsta = 2
    este_agresiv = False
    are_pedigree = True
    culoare = 'negru'

    def __init__(self, rasa, varsta, este_agresiv, are_pedigree, culoare): # constructor
        self.rasa = rasa
        self.varsta = varsta
        self.este_agresiv = este_agresiv
        self.are_pedigree = are_pedigree
        self.culoare = culoare
    # trebuie respectat numarul de atribute si ordinea lor atunci cand le folosim in alte obiecte
    # print(f'Rasa este {rasa}') # pot sa printez fara self. atunci cand printez in

    def descriere(self):
        print(f'Am un caine {self.rasa}, are {self.varsta} ani, este agresiv {self.este_agresiv}')

    def ani_omenesti(self):
        print(f'cainele are {self.varsta*7} ani omenesti')

    def estAgresiv(self):
        return self.este_agresiv

zoro = Caine('labrador', 2, False, True, 'negru')

print(f'Rasa lui Zoro este {zoro.rasa}')
print(f'Varsta lui Zoro este {zoro.varsta}')
print(f'Culoarea lui Zoro este {zoro.culoare}')

zoro.descriere()
print(zoro.estAgresiv())

assert zoro.are_pedigree
if zoro.estAgresiv():
    print('du-l la dresaj')
else:
    print('este o alegere buna')


spark = Caine('buldog', 10, False, False, 'maro')
azorel = Caine('dog german', 5, True, False, 'alb')

print(f'Spark are {spark.ani_omenesti()} ani omemesti')

class Elev:
    def __init__(self, nume, varsta, profil, medie_generala):
        self.nume = nume
        self.varsta = varsta
        self.profil = profil
        self.medie_generala = medie_generala

    def descriere(self):
        print(f'Ma numesc {self.nume}, am {self.varsta} ani, studiez {self.profil} si am media {self.medie_generala}.')


alin = Elev('Alin', 16, 'real', 9)
victor = Elev('Victor', 15, 'uman', 8)
claudia = Elev('Claudia', 15, 'real', 8.5)

alin.descriere()
claudia.descriere()
victor.descriere()

claudia.medie_generala = 10   #supracrierea unui field
claudia.descriere()



