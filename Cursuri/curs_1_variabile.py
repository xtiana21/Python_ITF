print('buna seara!')

marca_masina = 'Mazda'

print(type(marca_masina)) # aflam tipul variabilei

# atribuirea aceleiasi valori la mai multe stringuri
lungime = latime = 5
print(lungime)
print(latime)

varsta = 4
varsta = int(varsta)
print(type(varsta)) # type casting (schimbam tipul de variabila)

assert varsta == 4 # verificarea variabilei

#cursant1 = input("Vreau numele primului cursant")
#print(cursant1)

#input statement
#lungime = int(input("lungimea este"))
#latime = int(input("latimea este"))
#print(f'Aria este {lungime*latime}')


compunere = "Ana are mere"
print(compunere[0]) # printeaza primul caracter
print(compunere[0:4]) # printeaza primele 4 caractere
print(compunere[8:12]) # printeaza caracterele 8-12
print(compunere[8:12:2]) # printeaza caracterele de la 8 la 12 din 2 in 2
print(compunere[1::2]) # printeaza una nu una da dintr-un string
print(len(compunere)) # lungimea stringului
print(compunere[::-1]) # printeaza propozitia invers
print(compunere[len(compunere)-1]) # ultimul caracter
print(compunere[0:len(compunere)]) # printare string intreg



# metodele pe care le punem in fata variabilei le putem printa direct
compunere = compunere.replace('Ana','Maria')

# metodele pe care le folosim cu . dupa  variabila trebuie sa le suprascriem variabilei
compunere = compunere.upper()
print(compunere)

# variabilele ce au is in nume declara True sau False
print(compunere.isnumeric())

assert compunere.islower() == False


nume = 'ion'
print(nume*3)

#pyton -- version => verificare versiune python


