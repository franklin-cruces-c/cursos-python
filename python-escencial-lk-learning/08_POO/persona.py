class Persona2:
    def __init__(self):
        print("estoy en el constructor de la clase persona")

paco = Persona2()


class Animal:
    reino="Animal"
    def __init__(self,nombre, tipo):
        self.tipo=tipo
        self.nombre=nombre

perro = Animal("perro","mamifero")

print(perro.nombre)
print(perro.tipo)
print(perro.reino)

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anhos(self):
        self.edad +=1
        #print(f"Feliz cumpleaños #{self.edad} {self.nombre}")
        print("Feliz cumpleaños #",self.edad, self.nombre)

Nidia = Persona("Nidia",37)
Nidia.cumplir_anhos()
        

