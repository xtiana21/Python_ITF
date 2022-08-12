'''1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else.

 Un operator "if else" ne ajuta sa executam un cod atunci cand o conditie este adevarata
 sau alt cod, daca prima conditie nu este adevarata
 - if - executa o conditie scrisa atunci cand este adevarata
 - else - daca prima conditie nu este adevarata, se executa alt cod'''

print('\n')
print('Exercitiul 2 - Verifica si afiseaza daca x este numar natural sau nu')

x = int(input('Scrie un numar X:'))
if x > 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} nu este un numar natural')


print('\n')
print('Exercitiul 3 - Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru')

if x > 0:
    print(f'Numarul {x} este pozitiv')
elif x == 0:
    print (f'Numarul {x} este neutru')
else:
    print(f'Numarul {x} este negativ')


print('\n')
print('Exercitiul 4 - Verifica si afiseaza daca x este intre -2 si 13')

if x > 13 and x < -2:
    print(f'Numarul {x} se afla in afara intervalului')
else:
    print(f'Numarul {x} se afla in intervalul -2 si 13')

#sau

if x in range(-2,14):
    print(f'Numarul {x} se afla in intervalul -2 si 13')
else:
    print(f'Numarul {x} se afla in afara intervalului -2 si 13')


print('\n')
print('Exercitiul 5 - Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5')

y = int(input('Scrie un numar Y:'))
if x - y < 5:
    print('Diferenta dintre numere este mai mica de 5')
else:
    print('Diferenta dintre numere este egala sau mai mare decat 5')


print('\n')
print('Exercitiul 6 - Verifica daca x NU este intre 5 si 27. (a se folosi ''not'')')

if not(x < 5 or x > 27):
    print('Numarul face parte din interval')
else:
    print('Numarul nu face parte din interval')

#sau

if not x in range (5, 28):
    print(f'Numarul {x} nu face parte din intervalul 5 si 27')
else:
    print(f'Numarul {x} face parte din intervalul 5 si 27')


print('\n')
print('Exercitiul 7 - x si y (int). '
      '\nVerifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare ')

if x == y:
    print('Numerele sunt egale')
elif x > y:
    print(f'Numarul {x} este mai mare decat numarul {y}')
else:
    print(f'Numarul {y} este mai mare decat numarul {x}')

print('\n')
print('Exercitiul 8 - X, y, z - laturile unui triunghi'
      '\nAfiseaza daca triunghiul este isoscel, echilateral sau oarecare. ')

x = float(input('Latura 1:'))
y = float(input('Latura 2:'))
z = float(input('Latura 3:'))

if x == y == z:
    print('Triunghiul este echilateral')
elif x == y  or y == z or x == z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')


print('\n')
print('Exercitiul 9 - Citeste o litera de la tastatura'
      '\nVerifica si afiseaza daca este vocala sau nu')

vocale = ['a', 'e', 'i', 'o', 'u']
litera = input('Scrie o litera:')
if litera in vocale:
    print('Aceasta litera este o vocala')
else:
    print('Aceasta litera nu este o vocala')


print('\n')
print('Exercitiul 10 - Transforma si printeaza notele din sistem romanesc in:'
      '\nPeste 9 => A'
      '\nPeste 8 => B'
      '\nPeste 7 => C'
      '\nPeste 6 => D'
      '\nPeste 4 => E'
      '\n4 sau sub => F')

nota = float(input('Nota ta este:'))

if nota >= 9:
    print('Ai obtinut nota A')
elif nota >= 8:
    print('Ai obtinut nota B')
elif nota >= 7:
    print('Ai obtinut nota C')
elif nota >= 6:
    print('Ai obtinut nota D')
elif nota >= 4:
    print('Ai obtinut nota E')
elif nota <= 4:
    print('Ai obtinut nota F')
else:
    print('Ai picat!')


# c. Optionale (may need google)
print('\n')
print('Exercitiu 11 - Verifica daca x are minim 4 cifre (x e int)'
      '\n(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)')

x = int(input('Introdu un numar pentru verificare lungime:'))
if len(str(x)) >= 4:
    print(f'Numarul {x} are minim 4 cifre')
else:
    print(f'Numarul {x} are mai putin de 4 cifre')


print('\n')
print('Exercitiul 12 - Verifica daca x are exact 6 cifre ')

if len(str(x)) == 6:
    print(f'Numarul {x} are exact 6 cifre')
else:
    print(f'Numarul {x} nu are exact 6 cifre')


print('\n')
print('Exercitiul 13 - Verifica daca x este numar par sau impar (x e int)')

if x % 2 == 0:
    print(f'Numarul {x} este par')
else:
    print(f'Numarul {x} este impar')


print('\n')
print('Exercitiul 14 - x, y, z (int)'
      '\nAfiseaza care este cel mai mare dintre ele')

if x > y and x > z:
    print(f'Numarul {x} este cel mai mare')
elif y > x and y > z:
    print(f'Numarul {y} este cel mai mare')
else:
    print(f'Numarul {z} este cel mai mare')

# sau

print(f'Numarul cel mai mare este: {max(x,y,z)}')


print('\n')
print('Exercitiul 15 - X, y, z - reprezinta unghiurile unui triunghi'
      '\nVerifica si afiseaza daca triunghiul este valid sau nu')

unghi1 = int(input('Valoare unghi 1:'))
unghi2 = int(input('Valoare unghi 2:'))
unghi3 = int(input('Valoare unghi 3:'))

if unghi1 + unghi2 + unghi3 == 180:
    print('Triunghiul este valid')
else:
    print('Triunghiul nu este valid')


print('\n')
print('Exercitiul 16 - Avand stringul: ''Coral is either the stupidest animal or the smartest rock'''
      '\n- cititi de la tastatura un int x'
      '\n- afiseaza stringul fara ultimele x caractere'
      '\nex: daca ati ales 7 => ''Coral is either the stupidest animal or the smarte''')

prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('Introdu valoare pentru stergere string: '))
print(prop[0:len(prop)-x])

#sau

print(prop[:-x])


print('\n')
print('Exercitiul 17 - acelasi string:'
      '\n- declara un string nou care sa fie format din primele 5 caractere + ultimele 5')

prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop[:5] + prop[-5:])

#sau

text_nou = prop[0:5]+prop[len(prop)-5: len(prop)-1]
print(text_nou)


print('\n')
print('Exercitiul 18 - Acelasi string'
      '\nsalveaza intr-o variabila si afiseaza indexul de start al cuvantului rock'
      '\n(hint: este o functie care te ajuta sa faci asta)'
      '\nfolosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant'
      '\noutput: ''Coral is either the stupidest animal or the smartest''' )

text = 'Coral is either the stupidest animal or the smartest rock'
start = text.find("rock")
print(text[:start])

print('\n')
print('Exercitiul 19 - Citeste de la tastatura un string:'
      '\n- verifica daca primul si ultimul caraacter sunt la fel'
      '\n- se va folosi un assert'
      '\n- atentie: se doreste ca programul sa fie case insensitive (''apA'' e acceptat)')

text = input("Scrie un text pentru verificare prima si ultima litera")
assert text[0].lower() == text[-1].lower()

print('\n')
print('Exercitiul 20 - Avand stringul ''0123456789'''
      '\n- afisati doar numerele pare'
      '\n- acum afisati doar numerele impare'
      '\n(hint: folositi slicing, controlati din pas)')

sir_numere = '0123456789'
print(sir_numere[0:11:2])
print(sir_numere[1:11:2])

# Bonus la cerere:
print('\n')
print(f'Exercitiul 21 - Verificare imbarcare persoane ')

'''Verificare imbarcare persoane
Tineti urmatoarele date:
- Varsta
- Insotit de mama
- Insotit de tata
- Pasaport
- Act permisiune mama
- Act permisiune tata

Conditii de imbarcare:
- Daca pers are varsta peste 18 ani si are pasaport
- Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
- Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

Aici vreau sa testati codul cu toate variantele posibile
Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results

Ex:
- Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
- Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca'''

varsta = int(input('Varsta:'))
este_insotit_de_mama = bool(input('Este insotit de mama?'))
este_insotit_de_tata = bool(input('Este insotit de tata?'))
are_pasaport = bool(input('Are Pasaport?'))
are_act_permisiune_mama = bool(input('are act permisiune mama'))
are_act_permisiune_tata = bool(input('are act permisiune tata'))

if varsta >=18 and are_pasaport:
    print('Se poate imbarca')
elif varsta<18 and are_pasaport and este_insotit_de_mama and este_insotit_de_tata:
    print('Se poate imbarca')
elif varsta<18 and are_pasaport and este_insotit_de_mama and are_act_permisiune_tata:
    print('Se poate imbarca')
elif varsta<18 and are_pasaport and este_insotit_de_tata and are_act_permisiune_mama:
    print('Se poate imbarca')
else:
    print('Nu se poate imbarca. Nu indeplineste toate conditiile pentru imbarcare')


print('\n')
print(f'Exercitiul 22 - Joc ghicit zarul')

'''Cauta pe net si vezi cum se genereaza un numar random
Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
Luati un nr ghicit de la utilizator
Verificati si afisati daca utilizatorul a ghicit

3 optiuni:
-   Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
-	Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
-	Ai ghicit. Felicitari? Ai ales x si zarul a fost y'''

import random
numar_zar = random.randint(1,6)
numar_ghicit = int(input("Ghiceste numarul:"))

if numar_zar == numar_ghicit:
    print(f'Ai ghicit! Ai ales {numar_ghicit} si zarul a fost {numar_zar}')
else:
    if numar_zar > numar_ghicit:
        print(f'Ai pierdut! Ai ales un numar mai mic. Ai ales {numar_ghicit} dar a fost {numar_zar}')
    else:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit} dar a fost {numar_zar}')
