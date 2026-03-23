def perimetro_cuadrado(lado,unidades):
    perimetro = lado * 4
    #print(f"El perimetro es {perimetro} {unidades}") # formateado con f
    print("El perimetro es",perimetro, unidades)

perimetro_cuadrado(5,"metros")
perimetro_cuadrado(unidades="metros",lado=5)

#retornar valores de una funcion
print("Retornando valores de funciones")
def area_cuadrado(lado):
    area = lado * lado
    return area

def perimetro_cuadrado(lado):
    """Calcular el perímetro de un cuadrado

    Esta función recibe el valor de un lado de un cuadrado y a partir 
    de este calcula y retorna su perímetro

    Args:
         lado (int): medida  del lado del cuadrado

    Returns:
         perimetro (int): perímetro del cuadrado
    """    
    perimetro = lado * 4
    return perimetro

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)
print(f"Cuadrado=> Area: {area} Permitro: {perimetro}")

# funcion de retorno multiple
def calcular_cuadrado(lado):
    area = lado * lado 
    perimetro = lado * 4
    return area,perimetro

print("Retornando multiples valores a multiples variables")

area,perimetro = calcular_cuadrado(5)
print(f"Area:{area}  Permitero:{perimetro}")
print("Retornando multiples valores a una tupla")
resultado= calcular_cuadrado(5)
print("Resultado:",resultado)