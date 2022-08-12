# structuri repetitive, acelasi cod se repeta de mai multe ori - avem mai multe iteratii

# while - executa atata timp cat conditia este adevarata
# numar = int(input('scrie un numar'))
# # cat timp conditia de mai jos este adevarata (numarul este diferit de 10), atata timp o sa citim numere de la tastatura
# while numar != 10:
#     numar = int(input('scrie un numar'))
#     print(f'numarul tare are o diferenta de {numar - 10} de numarul 10')
# print('valoarea este corecta')

# while are nevoie de o valoare de inceput i
# ex - produsul numerelor pana la 10
# i = 1
# produs = 1
# # trebuie sa ne asiguram ca ii adaugam
# while i <= 11:
#     produs = produs * i #produs *=i
#     i+=2
# print(produs)

# for
# ex - produsul numerelor pana la 10

# produs2 = 1
# for i in range (1,12,2):
#     produs2 = produs2 * i
# print(produs2)

# la liste, cand aveti nevoie de pozitia elementelor parcurgeti lista cu for i in range

# for each
# se foloseste atunci cand nu avem nevoie de pozitia elementului
# ex - printare elemente dintr-o lista
# masini = ['cielo', 'dacia', 'audi']
# for masina in masini:
#     print(masina)

# continue - sare peste o iteratie
# produs2 = 1
# for i in range (1,12,2):
#     if i % 7 == 0: #daca i se imparte la 7 sare la urmatoarea iteratie
#         continue
#     produs2 = produs2 * i
# print(produs2)

# break - opreste iteratia (for sau while)
# ex - atunci cand produsul este 500 sa se opreasca
produs2 = 1
# for i in range (1,12,2):
#     if i % 7 == 0:
#         continue
#     produs2 *= 1
#     if produs2 >= 500:
#         break
# print(produs2)

lista = [2, 3, 56, 7, 8, 89]
max = lista[0]
for element in lista:
    if element > max:
        max = element
print(max)


# functii
# ex - identif element maxim
def maxim():
    lista = [2, 3, 56, 7, 8, 89]
    max = lista[0]
    for element in lista:
        if element > max:
            max = element
    print(max)


lista = [4, 6, 7, 8, 9, 22]


def perimetrulDreptunghiului(lungime, latime):
    print(f'perimetrul dreptunghiului este {lungime * latime}')


perimetrulDreptunghiului(4, 5)
perimetrulDreptunghiului(67, 56)


def descrierePersoana(nume, varsta, oras):
    print(f'Ma numesc {nume}, am {varsta} si sunt din {oras}')


descrierePersoana('Cristiana', 30, 'Bucuresti')


# elementele din paranteze se numesc parametri si pot fi oricati
# este important de respectat ordinea parametrilor

# putem sa declaram parametri by default
def descrierePersoana(nume, varsta, oras='constanta'):
    print(f'Ma numesc {nume}, am {varsta} si sunt din {oras}')


descrierePersoana('Cristiana', 30)


def is_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


print(is_par(6))


def is_par2(numar):
    if numar % 2 == 0:
        return 'numar par'
    else:
        return 'numar impar'


print(is_par2(10))

# ex - avem o lista de numere, folosim o metoda cu parametru si return
numere = [2,3,4,5,67,89,90]
i=0
media = 0
while i < len(numere):
    print(numere[i])
    media += numere[i]
    i+=1
media = media / len(numere)
print(media)

def media(lista_numere):
    i = 0
    media = 0
    while i < len(lista_numere):
        media += lista_numere[i]
        i += 1
    media = media / len(lista_numere)
    return media

print (media(numere))
print (media([2,3,4,5,6]))

def media2(lista_numere):
    media = 0
    for numar in lista_numere:
        media += numar
    media = media / len(lista_numere)
    return media
print(media2(numere))
print(media2[2,3,4,5,6])