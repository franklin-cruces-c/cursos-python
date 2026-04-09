def validar_x(x):
    if x<1:
        raise Exception("La variable x debe ser mayor a 1")
    else:
        print("x es mayor a 1")

x= 7
validar_x(x)
x = 0.3
validar_x(x)
