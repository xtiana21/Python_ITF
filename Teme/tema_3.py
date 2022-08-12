print(f'Exercitiul 1 - Declara o lista note_muzicale in care sa pui do re mi etc pana la do')
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

print('a. Afiseaz-o')
print(note_muzicale)

print('b. Inverseaza ordinea folosind slicing si suprascrie aceasta lista')
note_muzicale = note_muzicale[::-1]

print('c. Printeaza varianta actuala (inversata)')
print(f' Lista inversata :{note_muzicale}')

print('d. Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, '
      'adica sa ii inverseze ordinea')
note_muzicale.reverse()

print('e. Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala')
print(note_muzicale)


'''Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista
sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat
si permanentizeaza aceste modificari.
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.'''


print('\n')
print('Exercitiul 2 - De cate ori apare ''do''?')

print(f"Nota DO apare de {note_muzicale.count('do')} ori.")


print('\n')
print('Exercitiul 3 - Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]'
      '\nGasiti 2 variante sa le uniti intr-o singura lista.')


list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]

print(list1 + list2) # varianta 1

list3 = list1 + list2 # varianta 2
print(list3)

list1.extend(list2)
print(list1)


print('\n')
print('Exercitiul 4 - Sortati si afisati lista generata la ex anterior')
print(list1)
list1.sort()
print(f'Lista sortata: {list1}')

print('Stergeti numarul 0 folosind o functie')
list1.remove(0)
print('Afisati iar lista')
print(list1)


print('\n')
print('Exercitiul 5 - Folosind un if verificati lista generata la ex3 si afisati:'
      '\n- Lista este goala'
      '\n- Lista nu este goala')

if len(list1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')


print('\n')
print('Exercitiul 6 - Folositi o functie care sa stearga lista de la ex3')

list1.clear()
print(list1)


print('\n')
print('Exercitiul 7 - Copy paste la ex 5. Verificati inca o data. Acum ar trebui sa se afiseze ca lista e goala')

if len(list1) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')


print('\n')
print('Exercitiul 8 - Avand dictionarul dict1 = {Ana : 8, Gigel : 10, Dorel : 5}. '
      'Folositi o functie ca sa afisati Elevii (cheile)')

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1)
print(dict1.keys())


print('\n')
print('Exercitiul 9 - Printati cei 3 elevi si notele lor')
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

print(f"Ana a luat nota {dict1['Ana']}.")
print(f"Gigel a luat nota {dict1['Gigel']}.")
print(f"Dorel a luat nota {dict1['Dorel']}.")


print('\n')
print('Exercitiul 10 - Dorel a facut contestatie si a primit 6. '
      'Modificati nota lui Dorel in 6. '
      'Printati nota dupa modificare.')

dict1['Dorel'] = 6
print(dict1)
print(f"Dorel a luat nota {dict1['Dorel']}.")


print('\n')
print('Exercitiul 11 - Gigel se transfera din clasa. '
      '\nCautati o functie care sa il stearga. '
      '\nVine un coleg nou. Adaugati Ionica, cu nota 9. '
      '\nPrintati noii elevi.')

dict1.pop('Gigel')
print(dict1)
dict1['Ionica'] = 9
print(dict1)


print('\n')
print('Exercitiul 12 - Set'
      '\nzile_sapt = {luni, marti, miercuri, joi, vineri, sambata, duminica}'
      '\nweekend = {sambata, duminica}'
      '\nAdaugati in zilele_sapt ‘luni’'
      '\nAfisati zile_sapt')

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print('Raspuns:')
zile_sapt.add('luni')
print(zile_sapt)


print('\n')
print('Exercitiul 13 - Folositi un if si verificati daca:'
      '\nWeekend este un subset al zilelor din sapt '
      '\nWeekend nu este un subset al zilelor din sapt')

print('Raspuns:')
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din saptamana')
else:
    print('Weekend nu este subset')


print('\n')
print('Exercitiul 14 - Afisati diferentele dintre aceste 2 seturi')

print(f'Diferentele dintre cele doua seturi sunt: {zile_sapt.difference(weekend)}.')


print('\n')
print('Exercitiul 15 - Afisati intersectia elementelor din aceste 2 seturi.')

print(f'Intersectia dintre cele doua seturi este: {zile_sapt.intersection(weekend)}.')

# c. Optionale (may need google)
print('\n')
print('Exercitiul 16')

'''Ne imaginam o echipa de fotbal pt teren sintetic.

3 Schimbari maxime admise

Declara o Lista cu 5 jucatori

Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
-	Efectuam schimbarea
-	Stergem jucatorul scos din lista
-	Adaugam jucatorul intrat
-	Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
-	Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
-	Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”'''

jucatori = ['Adi', 'Relu', 'Razvan', 'Alex', 'Vali']
print(jucatori)

SCHIMBARI_MAX = 3
JUCATOR = str(input('Scrie numele jucatorului pe care vrei sa-l inlocuiesti:'))
schimbari_efectuate = int(input('Cate schimbari s-au facut pana acum pe teren?(maxim 3)'))


if JUCATOR in jucatori and schimbari_efectuate <= SCHIMBARI_MAX:
    print('Efectuam schimbarea')
    jucatori.remove(JUCATOR)
    print(jucatori)
    jucator_nou = jucatori.append(input('Ce jucator adaugi in teren?'))
    print(jucatori)
    print(f'A intrat {jucator_nou}, a iesit {JUCATOR}, mai aveti {SCHIMBARI_MAX - schimbari_efectuate} schimbari la dispozitie.')
else:
    print(f'Nu se poate efectua schimbarea, deoarece jucatorul {JUCATOR} nu este in teren.')
    print(f'Mai aveti {SCHIMBARI_MAX- schimbari_efectuate} schimbari.')


jucatori = ['Adi', 'Relu', 'Razvan', 'Alex', 'Vali', 'Remus']
JUCATOR = str(input('Scrie numele unui jucator'))
schimbari_efectuate = int(input('Numarul schimbarii'))

if JUCATOR in jucatori and schimbari_efectuate >= SCHIMBARI_MAX:
    print(f'Nu se poate efectua schimbarea, deoarece jucatorul {JUCATOR} este deja in teren.')
else:
    jucatori.append(JUCATOR)
    print(f'Echipa s-a completat cu jucatorul {JUCATOR}')
    print(f'Mai aveti {SCHIMBARI_MAX - schimbari_efectuate} schimbari la dispozitie.')





