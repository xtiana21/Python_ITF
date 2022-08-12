# daca metoda returneaza doar o operatie
def sum(a, b):
    return a + b


def is_oven(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


def is_oven2(number):
    return number % 2 == 0


def is_oven3(numar):
    if numar % 2 == 0:
        print(f'{numar} este par')
    else:
        print(f'{numar} este impar')


print(sum(3, 4))
print(sum(7, 8))

print(is_oven(10))
print(is_oven(1))
print(is_oven2(10))
print(is_oven2(1))
is_oven3(10)
is_oven3(1)
