#Condicionales
a = 5
b = 7
if a == b:
 print("Son iguales")
else:
  print("No son iguales")

if a > b:
 print("a es mayor que b")
else:
  print("b es mayor que a")
  
if a > b:
 print("a es mayor que b")
elif a == b:
  print("a y b son iguales")
else:
  print("b es mayor que a")

a = False

if a :
  print("a es verdadero")
else:
  print("a es falso")

#Ciclos
# For
print("***** Ciclo For ****")
for letra in "kaminando con programacion":
    print (letra)

lenguajes = ["python", "java", "golang"] 
for elemento in lenguajes:
  print(elemento)
print("*** con break")
for elemento in lenguajes:
  print(elemento)
  if elemento == "java":
    break
print("*** con continue")
for elemento in lenguajes:
  if elemento == "java":
    continue
  print(elemento)
print("*** con range")
for elemento in range(5):
 print(elemento)
print("*** con range desde el 1")
for elemento in range(1,5):
 print(elemento)

print("***** Ciclo While ****")
i = 1
while i <= 5:
  print(i)
  i += 1

print("***** con break ****")
i = 1
while i <= 5:
  print(i)
  i += 1
  if(i == 3):
    break
 # iterando sobre una lista
print("iterando sobre una lista") 

lenguajes = ["python","java","golang"]
for elemento in lenguajes:
   print(elemento)
print("ahora con for index")
for index in range(len(lenguajes)):
  print("indice",index)
  print("lenguaje->",lenguajes[index])

print("***** iterando sobre una lista con while")
i=0
n= len(lenguajes)

while(i<n):
  print(lenguajes[i])
  i+=1

print("***** Iterando sobre un diccionario ciclo For")
lenguaje = {
  "nombre": "python",
  "creador": "Guido van Rossum"
}

for clave in lenguaje:
  print("clave:", clave)
  print("valor",lenguaje[clave])

print("***** con items")

for elemento in lenguaje.items():
  print(elemento)