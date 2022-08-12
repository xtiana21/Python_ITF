print('Exercitiul 1 - In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila')
# O variabila reprezinta un loc/ o zona, in care se stocheaza date
print('O variabila reprezinta un loc/ o zona, in care se stocheaza date')

print('\n')
print('Exercitiul 2 - Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri: string, int, float, bool')

oras = 'Brasov'
altitudine = 638
numar_locuitori = 253.200
oras_resedinta = True

print(f'{oras}, {altitudine}, {numar_locuitori}, {oras_resedinta}')


print('\n')
print('Exercitiul 3 - Utilizati functia type pentru a verifica daca au tipul de date asteptat')

print(type(oras))
print(type(altitudine))
print(type(numar_locuitori))
print(type(oras_resedinta))

print('\n')
print('Exercitiul 4 - Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)')

numar_locuitori = round(numar_locuitori)
print(numar_locuitori)
print(type(numar_locuitori))
print(f'Numarul de locuitori al orasului Brasov este {numar_locuitori} mii.')

print('\n')
print('Exercitiul 5 - folositi print() si printati in consola 4 propozitii folosind cele 4 variabile')

print(f'Urmeaza sa petrec vacanta in orasul {oras}.')
print(f'Orasul {oras}, se afla la o altitudine de {altitudine} metri.')
print(f'Orasul {oras}, are {numar_locuitori} de locuitori.')
print(f'Orasul {oras}, este oras resedinta pentru judet: {oras_resedinta}.')

print('\n')
print('Exercitiul 6 - citeste de la tastatura numele, citeste de la tastatura prenumele, afiseaza:Numele complet are x caractere')

nume = input('Numele este:')
prenume = input('Prenumele este:')
print(f'Numele complet are {len(nume)+len(prenume)} caractere.')

print('\n')
print('Exercitiul 7 - citeste de la tastatura lungimea, citeste de la tastatura latimea, Afiseaza: Aria dreptunghiului este: ')

lungimea = input('Lungimea este:')
latimea = input('latimea este:')
lungimea = int(lungimea)
latimea = int(lungimea)

print(f'Aria dreptunghiului este {lungimea * latimea} cm.')

print('\n')
print('Exercitiul 8 - Avand stringul: Coral is either the stupidest animal or the smartest rock. Afisati de cate ori apare cuvantul: the')

propozitie = 'Coral is either the stupidest animal or the smartest rock'
numar = propozitie.count('the')

print(f'Cuvantul the apare in propozitie de {numar} ori.')

print('\n')
print('Exercitiul 9 - acelasi string, inlocuieste the cu THE peste tot, printeaza rezultatul')

print(propozitie.replace('the', 'THE'))

print('\n')
print('Exercitiul 10 - acelasi string de mai sus, folositi un assert ca sa verificati daca acest string contine doar numere')

assert not propozitie.isnumeric()
# not - ca sa treaca mai departe

print('\n')
print('Exercitiul 11 -  citeste de la tastatura un string de dimensiune impara, afiseaza caracterul din mijloc')

text_dimediune_impara = input('Un text de dimensiune impara')
pozitie = len(text_dimediune_impara)//2
print(f'{text_dimediune_impara} are caracterul din mijloc {text_dimediune_impara[pozitie]}')

print('Sau')

def caracter_mijloc (txt):
    return txt[(len(txt) - 1) // 2:(len(txt) + 2) // 2]
culoare = input('Scrie o culoare:')
print(f'{culoare} are cacacterul din mijloc {caracter_mijloc(culoare)}')

print('\n')
print('Exercitiul 12 - Folosind assert, verificati daca un string este palindrom')

atentie = 'radar'
assert atentie == atentie [::-1]

print('\n')
print('Exercitiul 13 - folosind o singura linie de cod, citeste un string de la tastatura (ex: alabala portocala) si salveaza fiecare cuvant intr-o variabila. Acum printeaza ambele variabile pent verificare')

text1, text2 = input("Scrie un text din 2 cuvinte: ").split()
print(text1)
print(text2)

print('\n')
print('Exercitiul 14 - citeste un string de la tastatura (eg: alabala portocala)salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite) capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter=> alAbAlA portocAla')

text = input("Scrie un text:")
primul_caracter = text[0]
text_modificat = text[0] + text[1:-1].replace(primul_caracter,primul_caracter.capitalize()) + text[0]
print(text)
print(text_modificat)

print('\n')
print('Exercitiul 15 - citeste un user de la tastatura. Citeste o parola. Afiseaza: parola pt user x este ***** si are x caractere. ***** se va calcula dinamic. Indiferent de dimensiunea parolei, trebuie sa afiseze corect: parola abc => *** parola abcd => ****')

user = input('Scrie username:')
parola = input ('Scrie parola:')
parola_ascunsa = '*'*len(parola)

print(f'parola pt userul {user} este {parola_ascunsa} si are {len(parola)} caractere')


