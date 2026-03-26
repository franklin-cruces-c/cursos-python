class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anhos(self):
        self.edad +=1
        #print(f"Feliz cumpleaños #{self.edad} {self.nombre}")
        print("Feliz cumpleaños #",self.edad, self.nombre)

class Empleado(Persona):
    def __init__(self,horas_totales,nombre,edad):
        super(Empleado,self).__init__(nombre,edad)
        self.horas_totales= horas_totales


    def trabajar(self,horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Has trabajado hoy {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")

Nidia = Empleado(30,"Nidia",37)
Nidia.trabajar(8)
Nidia.cumplir_anhos()
