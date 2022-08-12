#pollymorphism - cand exista doua metode cu acelasi nume, dar pot sa aiba forme diferite

#built polyphormic function
def add(a,b,c):
    return a+b+c

print(add(3,4,5))
def addd(a,b,c=0): #predefinesc  by default un parametru
    return a+b+c

print(addd(3,4)) #nu mai sunt obligata sa ofer toati 3 parametrii

def descriere(nume, prenume='Muresan'): #presetez un parametru ca sa pot apela functia si cu un singur parametru
    print(f'Numele este {nume}, prenumele este {prenume}')
descriere('Ion')

class Bird: #clasa parinte
    def descriere(self):
        print('I am a bird')
    def fly(self):
        print('Flu, fly, I am flying')

class Parrot(Bird):
    def talk(self):
        print('I can talk')
    def fly(self):   #suprascrie fly-ul din clasa parinte
        print('I canot fly, I am sick!')

coco = Parrot()
coco.descriere()
coco.fly()
coco.talk()
coco.fly()