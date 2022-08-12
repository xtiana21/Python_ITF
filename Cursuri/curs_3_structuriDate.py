# STRUCTURI DE DATE

'''# putem folosi toate tipurile de date
# poate sa aiba elemente duplicat
# este ordonata
# putem adauga elemente noi sau putem sterge din elemente
# putem modifica lista'''''

# List
import random
# list1 = ['abc', 455, 34.5, True, 'mama', 'primavara', 45]

#lungimea unei liste
# print(len(list1))
# #cum accesam un element
# print(list1[1])
#cum facem slicing
# print(list1[0:4])
# print(list1[:4])
# # ultimul element
# print(list1[-1])
# print(list1[len(list1)-1])
# # suprascriere primul element
# list1[0] = 'Elena'
# # cum adaug
# list1.insert(1,10)
# print(list1)
#
# list1.append('ioana')
# print(list1)

#cum stergem
# list1.pop()  #sterge ultimul element
# print(list1)
#
# list1.pop(0) #sterge elementul 0
# print(list1)

# list1.remove('mama') #sterge elementul mentionat de noi
# print(list1)
#
# list2 = [2,3, 'elena', [1,2,3], ['a', 'e', [3,4,5], 'lola']]
# print(list2[4]) #printeaza elementul 4
# print(list2[4][0]) #printeaza din elementul 4, pozitia 0

# cum iau o valoare random
# luni = ['ianuarie', 'februarie', 'martie', 'aprilie']
# random_nr = random.randint(0, len(luni)-1)
# print(luni[random_nr])
#
# luna_curenta = input('citeste o luna din an:')
# if luna_curenta in luni: # daca luna se afla in lista luni
#     print('luna este buna')

vocale = ['a', 'e', 'i', 'o', 'u']
# voc = input ('Introdu o vocala:')
# if voc in vocale:
#     print(voc*10)
# else:
#     print('Nu este vocala')

# DICTIONARE
# masina = {'brand': 'dacia', 'model': 'spring', 'culoare': 'verde', 'cp':2334}
# print(masina['brand'])
# print(masina.get('brand'))
# print(masina.keys())
# print(masina.values())
# masina['cutie'] = 'automata' # adaugam o valoare noua
# print(masina)
# masina['cutie'] = 'manuala' # suprascriere
# print(masina)
# masina.pop('cutie')
# print(masina)

# produse = {'masina de spalat':[23, 45]}
# print(produse['masina de spalat'][0])
# assert 'pretul produsului' == produse['masina de spalat'][0]

#SET
'''#lista cu valori unice, ex: vocalele
#nu sunt ordonate
#se pot adauga se sterge elemente'''


culori = {'alb', 'rosu', 'verde'}
print(len(culori))
culori.add('albastru') # adaugam element, se afiseaza ultimul
print(culori)
culori.remove('alb') # stergem element selectat de noi
print(culori)

#TUPLE
'''#nu se pot adauga si sterge valori
# nu sunt ordonate
# accepta valori duplicate'''
vocals = ('a', 'e', 'i', 'a')
print(vocals[0]) #printeaza elementul indexat pe pozitia 0
print(len(vocals)) #printeza lungimea sirului
print(vocals.index('a')) #printeaza pe ce pozitie e indexat elementul