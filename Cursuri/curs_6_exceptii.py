# in try punem codul predispus la eroare
try:
    lista = [1,2,3,4]
    print(lista[4]) #practic printam elementul 5 care nu exista, indexul incepe de la 0
except IndexError as e:
    print('lungimea listei nu e corecta. incerci sa printezi o pozitie care nu exista')


try:
    print (mama)
except NameError as e:
    mama = 'ioana'
    print('variabila nu a fost definita si am definit-o')
print(mama)