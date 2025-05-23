class Animal:
    def falar(self):
        print("Todo animal pode emitir um som se quiser.")

class Gato(Animal): #Gato herda características do Animal
    def falar(self):
        print("O gato mia ato.")


class Cachorro(Animal):
    def falar(self):
        print("O cachorro late alto.")



a = Animal() 
a.falar()    

g = Gato()
g.falar()

c = Cachorro()
c.falar()