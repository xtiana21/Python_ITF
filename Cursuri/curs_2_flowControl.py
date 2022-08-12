'''
operatori
if, if else
if, else if, else
'''

# operatori de atribuire
x = 10
x = x + 5
print(x)

# acelasi lucru, dar se recomanda variantele de mai jos

x += 5
print(x)

x *= 3
print(x)

x /= 2
print(x)

# operatori de comparare: <, >, =, >=, <=, !=
assert 5 == 5
assert "Maria" == "Maria" # operator de egalitate
assert "Maria" != "maria" # operatori de diferentiere

# operatori logici:
# and (toate conditiile trebuie sa fie adevarate)
assert x > 25 and x < 35

# or (cel putin una dintre conditii trebuie sa fie adevarata)
assert x > 25 or x < 20

# not (schimba rezultatul: din True in False si invers)
print (not(5==5))


# operatori flow control

# if, if else
# daca o conditie este adevarata, atunci se executa un cod;
# daca nu este adevarata, atunci se executa alt cod


#if
# numar = int(input('Dati un numar:')) #ofer o valoare de la tastatura
# if numar <= 20:
#     print ('Numarul este bun')


# if else
# parola = input ('Scrieti o parola:')
# if parola == 'Ana':
#     print('Bine ai venit')
# else:
#     print('Mai incearca')


nota = float(input('Nota ta este:'))
if nota > 4.5:
    print ('Ai trecut!')
else:
    print ('Ai picat!')

calificativ = input('Nota obtinuta')
if calificativ == 'A' or calificativ == 'a':
    print ('Nota foarte buna')
elif calificativ == 'B':
    print('Nota buna')
elif calificativ == 'C':
    print('Nota mica')
elif calificativ == 'D':
    print('Nota proasta')
else:
    print('Ai picat!')


# recapitulare

#if
zi = input('Alege o zi')
if zi == 'marti' or zi == 'Marti':
    print('azi avem curs')

if zi.lower() == 'marti':
    print('azi avem curs')



#if else

NOTA_DE_TRECERE_EXAMEN = 4.5
NOTA_DE_TRECERE_PURTARE = 7

nota_examen = float(input('Introdu nota examen:'))
nota_purtare = int(input('Introdu nota purtare:'))

if nota_examen >= NOTA_DE_TRECERE_EXAMEN and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
    print('Ai trecut clasa!')
    if nota_examen == 10 and nota_purtare == 10:
        print('Ai luat premul 1!')
else:
    print('Ai picat!')



#if, elif, else

varsta = int(input('Varsta este:'))
if varsta < 14:
    print('Este minor')
elif varsta < 18:
    print('Este minor cu buletin')
else:
    print('Este major')

nume = input('nume')
if not(nume) == 'Vasile':
    print('numele nu e corect')