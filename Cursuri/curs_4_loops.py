# while - executa conditia, atat timp cat este adevarata

# exercitiu 1: printati numerele pana la 5

i = 0 # de unde porneste numaratoarea
while i<= 5: # pana unde printeaza numerele
    print(i)
    i = i + 1 # oferim incrementare - conditia ca sa nu intre in ciclu infinit

# exercitiu 2: printati suma numerelor pana la 10

suma = 0 # oferim valoare sumei
i = 1 # de unde porneste adunarea
while i<= 10: # pana unde calculeaza suma
    suma += i #calcularea sumei
    i = i + 1 # stabilire incrementare
print(f'Suma numerelor pana la 10 este {suma}')



# while else - se executa o singura data la final daca conditia e true sau false, e optional
# de unde incpem - initializare, decrementare, incrementare

j = 10
produs = 1
while j <= 10:
    print(i)
    produs *= 1
    j = j+2
else:
    print('s-a terminat')
print(produs)


# executa o bucata de cod pentru fiecare element dintr-un interval, dintr-o lista
sum = 0
prod = 1
for i in range (20,0,-5):
    print(i)
    sum +=i
    prod *= i
else:
    print('e gata')
print(sum)
print(prod)

# am o lista d culori in care inlocuiesc alb cu roz
culori = ['portocaliu', 'alb', 'rosu', 'albastru', 'alb', 'negru']
print(culori)

for i in range (0, len(culori)):
    print(f'culoarea este {culori[i]}')
    if (culori[i] == 'alb'):
        culori[i] = 'roz'
print(culori)

# for each - nu avem nevoie de pozitie si range, ia efectiv fiecare element din lista
numar = 0
for culoare in culori: # pentru fiecare culoare din lista culori
    print(culoare)
    if culoare[0]== 'r':
        numar += 1
print(numar)

note = [2,3,4,5,10]
# cati elevi au peste 10
numar_elevi = 0
for nota in note:
    if nota >= 5:
        numar_elevi += 1
print(f'numarul elevilor cu nota de trecere este {numar_elevi}')


i=1
while i in range(1,10):
    print(i)
    i+=1