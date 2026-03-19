def perimetro_cuadrado(lado,unidades):
    perimetro = lado * 4
    #print(f"El perimetro es {perimetro} {unidades}") # formateado con f
    print("El perimetro es",perimetro, unidades)

perimetro_cuadrado(5,"metros")
perimetro_cuadrado(unidades="metros",lado=5)