#  1. Functie care sa calculeze si sa returneze suma a 2 numere
print('\n')
print('Exercitiul 1 - returneaza suma a doua numere')

def sumNr (a, b):
    return a + b
print(f'Suma numerelor este: {sumNr(7,4)}')
print('........................................')
print(f'Suma numerelor este: {sumNr(43242,42343)}')


# # 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

print('\n')
print('Exercitiul 2 - returneaza True daca nr este par, False daca este impar')

def nrPar (numar):
    return numar % 2 == 0

print(f'Numarul tau este: {nrPar(5)}')
print('........................................')
print(f'Numarul tau este: {nrPar(4)}')

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

print('\n')
print('Exercitiul 3 - returneaza numarul total de caractere din numele complet')

def nrCaractereNume(nume, prenume):
    return len(nume + prenume)

print(nrCaractereNume('Stan','Cristiana'))
print('........................................')
print(nrCaractereNume('Stan','Valentin'))


# 4. Functie care returneaza aria dreptunghiului

print('\n')
print('Exercitiul 4 - returneaza aria dreptungiului')

def ariaDreptunghi (lungime, latime):
    return lungime * latime

print(f'Aria dreptunghiului este {ariaDreptunghi(5,8)}')
print('........................................')
print(f'Aria dreptunghiului este {ariaDreptunghi(321,8)}')


# 5. Functie care returneaza aria cercului

print('\n')
print('Exercitiul 5 - returneaza aria cerc')


def ariaCerc (raza):
    return 3.14 * (raza*raza)

print(f'Aria cercului este: {ariaCerc(8)}')
print('........................................')
print(f'Aria cercului este: {ariaCerc(25)}')


# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

print('\n')
print('Exercitiul 6 - True daca cuvantul tau contine caracterul u, False daca nu')

def caracterInString (string):
    caracter = 'u'
    return caracter in string

print(caracterInString('canicula'))
print('........................................')
print(caracterInString('plaja'))


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y

print('\n')
print('Exercitiul 7 - nr de caractere lower si upper din cuvantul tau')

def nrCaractereLowUp(string):
    no_low = 0
    no_up = 0
    for i in string:
        if i.islower():
            no_low += 1
            print(f'Numarul de caractere lower case este {no_low} caractere')
        elif i.isupper():
            no_up += 1
            print(f'Numarul de caractere upper case este {no_up} caractere')

nrCaractereLowUp('AlaBalaPortoCala')
print('........................................')
nrCaractereLowUp('AlbastruDeMetil')


# cuvant = input('Scrie un string: ')
# no_low = 0
# no_up = 0
# for i in cuvant:
#     if i.islower():
#         no_low += 1
#     elif i.isupper():
#         no_up +=1
# print(f'Numarul de caractere lower case este {no_low}')
# print(f'Numarul de caractere upper case este {no_up}')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

print('\n')
print('Exercitiul 8 - primeste o lista de numere, returneaza lista doar cu numerele pozitive')

numere = [1,2,3,-3,-2,-1]
def nr_pos(lista_numere):
    for numar in lista_numere:
        if numar >= 1:
            print(numar)
nr_pos(numere)
print('........................................')
nr_pos([4,5,6,-7,-8,-11,-12])

# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.

print('\n')
print('Exercitiul 9 - Comparare numere')

def comparare_numere(nr_1, nr_2):
    if nr_1 > nr_2:
        print(f'Numarul {nr_1} este mai mare decat numarul {nr_2}')
    elif nr_2 > nr_1:
        print(f'Numarul {nr_2} este mai mare decat numarul {nr_1}')
    else:
        print('Numerele sunt egale')

comparare_numere(8,2)
print('........................................')
comparare_numere(1,5)
print('........................................')
comparare_numere(3,3)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

print('\n')
print('Exercitiul 10 - functie care primeste un nr si un set de numere')

def function(number, set = {}):
    if number in set:
        print ('Nu am adaugat numarul in set. Numarul exista deja in set')
        return False
    else:
        set.add(number)
        print('Am adaugat numarul nou in set')
        return True
function(6,{4,5,6})
print('........................................')
function(7,{1,2,3,4})

# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

print('\n')
print('Exercitiul 11 - functie care primeste o luna din an si returneaza cate zile are acea luna')

def calendarLunileAnului(luna):
    luni_28 = ['Februarie']
    luni_30 = ['Aprilie', 'Iunie', 'Septembrie', 'Noiembrie']
    luni_31 = ['Ianuarie', 'Martie', 'Mai', 'Iulie', 'August', 'Octombrie']
    if luna in luni_31:
        print(f'Luna {luna} are 31 de zie.')
    elif luna in luni_30:
        print(f'Luna {luna} are 30 de zile.')
    elif luna in luni_28:
        print(f'Luna {luna} are 28 de zile.')
    else:
        print('Nu ai introdus o luna')

calendarLunileAnului('Februarie')
print('........................................')
calendarLunileAnului('Martie')
print('........................................')
calendarLunileAnului('Aprilie')

# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

print('\n')
print('Exercitiul 12 - functie calculator')

def calculator(nr1, nr2):
    a = nr1 + nr2
    print(f'Suma: {a}')
    b = nr1 - nr2
    print(f'Diferenta: {b}')
    c = nr1 * nr2
    print(f'Inmultirea: {c}')
    d = nr1 / nr2
    print(f'Impartirea: {d}')

calculator(3,3)
print('........................................')
calculator(6,5)

# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
print('\n')
print('Exercitiul 13 - functie care ne spune de cate ori apare fiecare cifra dintr-o lista')
lista_cifre = [1,1,1,1,4,4,5,5,5,6,7,6,9,9,7,6,3]
def functieCifre(lista_cifre):
    frecventa = {}
    for cifre in lista_cifre:
        frecventa[cifre] = lista_cifre.count(cifre)
    for key, value in frecventa.items():
        print("% d : % d" % (key, value))

functieCifre(lista_cifre)
print('........................................')
functieCifre([4,4,4,4,4,4,4,4,6,6,7,5,3,2,2,2,2,2])

# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
print('\n')
print('Exercitiul 14 - functie care returneaza valoarea maxima dintre 3 numere')

def nr_max(a,b,c):
    return max(a,b,c)
print(f'Numarul cu valoarea maxima este: {nr_max(3,7,2)}')
print('........................................')
print(f'Numarul cu valoarea maxima este: {nr_max(1,2,3)}')


# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
print('\n')
print('Exercitiul 15 - functie care returneaza suma tuturor numerelor pana la numarul ales')

def suma_numerelor(s):
    sum = 0
    i = 0
    while i <= s:
        sum += i
        i += 1
    return sum

print(f'Suma numerelor pana la numarul ales este {suma_numerelor(6)}')
print('........................................')
print(f'Suma numerelor pana la numarul ales este {suma_numerelor(3)}')

# BONUS:
# 16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
print('\n')
print('Exercitiul 16 - functie care returneaza numerele comune din 2 liste')

list1 = [1,2,3,3,4,5]
list2 = [3,5,6,6,7]
def nr_comune(list1, list2):
    return set(list1).intersection(list2)

print(nr_comune(list1,list2))
print('........................................')
print(nr_comune([3,4,5,6,7,7,8], [1,2,2,3,3,4,5,6,7]))

# 17. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
print('\n')
print('Exercitiul 17 - functie care aplica o reducere de pret')


def reducere_pret(pret,reducere):
    if reducere <= 100:
        pret_final = (100 - reducere) * pret / 100
        print(f'Pretul final dupa reducere este de: {pret_final}')
    else:
        print ('Reducerea este invalida.')

reducere_pret(40, 10)
print('........................................')
reducere_pret(10, 50)

# 18. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)
print('\n')
print('Exercitiul 18 - functie care afiseaza data si ora')

import datetime
tara = "Romania"
def ora_romaniei(tara):
    ora_curenta = datetime.datetime.now()
    return ora_curenta
print(f'Data si ora in Romania: {ora_romaniei(tara)}')


# 19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
print('\n')
print('Exercitiul 19 - functie care afiseaza cate zile mai sunt pana la ziua ta')

def DaysLeftFunction():
    today = datetime.date.today()
    birthday = datetime.date(2022,12,21)
    diff = birthday - today
    print (f'Mai sunt {diff.days} de zile pana la ziua mea')
DaysLeftFunction()

# def get_user_birthday():
#     year = int(input('When is your birthday? [YY] '))
#     month = int(input('When is your birthday? [MM] '))
#     day = int(input('When is your birthday? [DD] '))
#     birthday = datetime.datetime(year,month,day)
#     return birthday
#
# def calculate_dates(original_date, now):
#     date1 = now
#     date2 = datetime.datetime(now.year, original_date.month, original_date.day)
#     delta = date2 - date1
#     return delta
#
# bd = get_user_birthday()
# now = datetime.datetime.now()
# w = calculate_dates(bd,now)
# print(w)


