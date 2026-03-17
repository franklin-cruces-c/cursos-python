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

#diccionarios -> similar a hashmaps de java o json en javascript
 

lenguaje_diccionario = { 
    "nombre":"python",
    "creador": "Guido"
}
print(lenguaje_diccionario)
print(lenguaje_diccionario["nombre"]) #acceder a elementos por clave

lenguaje_diccionario["anio_lanzamiento"]=1991
print(lenguaje_diccionario)



lenguaje_diccionario["anio_lanzamiento"]=1991
print(lenguaje_diccionario)

lenguaje_diccionario["caracteristicas"]=['sencillo','facil',"genial"]
print(lenguaje_diccionario)
print(lenguaje_diccionario.items())
print(lenguaje_diccionario.keys())
print(lenguaje_diccionario.values())

#set igual que en java no permite valores repetidos. Si se agregan los omite

set1= {1,2,3}
print(set1)
set2= {1,1,1,2,3,3}
print(set2)
set3= {1,2.0,"Texto", True}
print(set3)
set3.add(4) # agregar un elemento
print(set3)
set1.update([4,5,6]) # actualizar el set agregando una lista de elementos
print(set1)
print(len(set1)) # cantidad de elementos que tiene el set
set1.discard(6) # eliminar un elemento del set (se hace por valor ej: 6)
print(set1) 
set1.remove(3) # eleminar un elemento -> genera error si el elemento no existe
print(set1)
set1.clear() # limpia el set, lo deja vacío
print(set1)