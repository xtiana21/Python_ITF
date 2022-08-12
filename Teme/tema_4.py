import random

# 1. Avand lista
print('\n')
print('Exercitiul 1')
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

# a)	Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’

print('a')
for i in range (0, len(masini)):
    print(f'Masina mea preferata este {masini[i]}')


# b)	Faceti acelasi lucru cu un for each
print('\n')
print('b')
for masina in masini:
    print(f'Masina mea preferata este {masina}')

# c)	Faceti acelasi lucru cu un while
print('\n')
print('c')
i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

# 2.Aceeasi lista
# Folositi un for
# In for
#    Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# Printati varianta finala a listei

print('\n')
print('Exercitiul 2')
for masina in range (1, 8):
    print(masini[masina].upper())

# 3. Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam

print('\n')
print('Exercitiul 3')
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dvs')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam!')

# 4.
# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x

print('\n')
print('Exercitiul 4')
for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    else:
        print(f'S-ar putea sa va placa masina {masina}')
# 5.
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# -	Salvati aceste masini in masini_vechi
# -	Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

print('\n')
print('Exercitiul 5')

masini_vechi = []
for i in range (len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lastun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'

print(f'Masinile noi sunt {masini}')
print(f'Masinile vechi sunt {masini_vechi}')

# 6.
# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista

print('\n')
print('Exercitiul 6')

pret_masini = {'Dacia': 6800,  'Lastun': 500, 'Opel': 1100, 'Audi': 19000,'BMW': 23000}
buget = int(input('Ce buget aveti pentru masina? :'))

for masina,pret in pret_masini.items():
    if buget >= pret:
        print(f'Pentru un buget de {pret} euro puteti alege masina {masina}')


#7. Avand lista
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

print('\n')
print('Exercitiul 7')


numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
total = 0

for numar in numere:
    if numar == 3:
        total += 1
print(f'Nr. 3 apare de {total} ori')

# 8.
# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

print('\n')
print('Exercitiul 8')

sum = 0
for numar in numere:
    sum  = sum + numar
print(f'Suma este: {sum}')

# 9.
# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)

print('\n')
print('Exercitiul 9')

max = numere[0]
for numar in numere:
    if numar > max:
        max = numar
print(f'Cel mai mare numar din lista este {max}')

# 10.
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

print('\n')
print('Exercitiul 10')

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
print(f'Noua lista este: {numere}')

# c. Optionale (may need google)
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

print('\n')
print('Exercitiul 11')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
    elif i < 0:
        numere_negative.append(i)
    else:
        print('0 e neutru')
    if i % 2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)

print(f' Numerele negative sunt: {numere_negative}')
print(f' Numerele pozitive sunt: {numere_pozitive}')
print(f' Numerele pare sunt: {numere_pare}')
print(f' Numerele impare sunt: {numere_impare}')

# 12.
# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4

print('\n')
print('Exercitiul 12')

aux = 0
for i in range (len(alte_numere)):
    for j in range (i + 1, len(alte_numere)):
        if alte_numere[i] > alte_numere[j]:
            aux = alte_numere[i]
            alte_numere[i] = alte_numere[j]
            alte_numere[j] = aux
print(f'Ordinea crescatoare a listei este: {alte_numere}')


# 13.
# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# -	Nr secret e mai mare
# -	Nr secret e mai mic
# -	Felicitari! Ai ghicit!

print('\n')
print('Exercitiul 13')

numar_random = random.randint(1, 30)
print("numarul de ghicit e ", numar_random)
numar_ghicit = int(input('\nGhiceste numarul: '))
while numar_random != numar_ghicit:
    if not numar_ghicit in range(1,31):
        print('Numarul trebuie sa fie intre 1 si 30!')
        numar_ghicit = int(input('Ghiceste numarul: '))
        continue
    elif numar_ghicit < numar_random:
        print('Nr secret e mai mare!')
        numar_ghicit = int(input('Ghiceste numarul: '))
        continue
    elif numar_ghicit > numar_random:
        print('Nr secret e mai mic!')
        numar_ghicit = int(input('Ghiceste numarul: '))
        continue
    else:
        break
print('Felicitari! Ai ghicit!')

# 14.
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
#
# Ex:3
# 1
# 22
# 333

print('\n')
print('Exercitiul 14')

n = int(input('\nIntroduceti un numar mai mic decat 10: '))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print('')

# 15.
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]

# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

print('\n')
print('Exercitiul 15')

tastatura_telefon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')