# mostenirea
class Chef: #clasa parinte - lucruri generale
    def make_salad(self):
        print('salad')
    def fries(self):
        print('fries')
    def eggs(self):
        print('eggs')
class Italian_Chef(Chef): #clasa copil mosteneste clasa Chef
    def make_pizza(self):
        print('pizza')
class Japanese_Chef(Chef): #clasa copil mosteneste clasa Chef
    def make_sushi(self):
        print('sushi')

andreea = Italian_Chef()
andreea.make_pizza()
andreea.eggs()
