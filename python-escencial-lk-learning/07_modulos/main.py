from figuras.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras.circulo import area_circulo, perimetro_circulo

lado = 5
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)

perimetro = perimetro_cuadrado(lado)

print(perimetro)

radio = 5
circulo = {
    "lado": radio,
    "area": area_cuadrado(radio),
    "perimetro": perimetro_cuadrado(radio)
}

print(circulo)
