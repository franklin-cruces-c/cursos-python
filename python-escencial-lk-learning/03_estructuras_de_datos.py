#estructuras de datos

#listas
lenguajes = ["python","java","golang"]
print(lenguajes)

lista = [1, 2.0,True, "python", 1]
print(lista)
print(lista[0])
print(len(lista))
print(lenguajes[2])
print(lenguajes[-1]) #orden inverso indice negativo va desde el ultimo
print(lenguajes[-3])
# print(lenguajes[-5]) #  IndexError: list index out of range

print(lenguajes[0:2]) # 2 elementos desde la posicion 0

programacion = [lenguajes,"dedicacion", "practica"] #listas anidadas
print(programacion)
print(programacion[0][0])
lenguajes[0]= "dart" # se reemplaza un elemento de la lista
print(lenguajes)
lenguajes.append("python") #agrega elementos al final de la lista
print(lenguajes)
otros_lenguajes = ["c","c++"]
print(lenguajes)
lenguajes.extend(otros_lenguajes) # se concatenan las listas
print(lenguajes)
lenguajes.append(otros_lenguajes) # se agrega como lista anidada
print(lenguajes)



#tuplas  -> las tuplas no permiten modificar sus elementos 
t_lenguajes = ("python", "c","c++") # similar a un registro de DB
print(t_lenguajes)
t_lenguajes = "python", "c","c++" # tambien se puede declarar sin parentesis
print(t_lenguajes)
print(t_lenguajes[0])
print(t_lenguajes[-1])
#t_lenguajes[0]= "java"  # las tuplas no permiten modificar los valores de sus elementos
# TypeError: 'tuple' object does not support item assignment

#diccionarios

#set