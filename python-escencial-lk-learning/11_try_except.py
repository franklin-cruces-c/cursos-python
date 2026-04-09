def calcular_promedio(lista):
    assert len(lista)>0 , "La lista está vacía"
    return sum(lista)/len(lista)

try:
    promedio = calcular_promedio(lista=[1,2,3])
    print(promedio)
except Exception as e:
    print ("la funcion no calculó el promedio")


def calcular_promedio(lista):
    assert len(lista)>0 , "La lista está vacía"
    return sum(lista)/len(lista)

try:
    promedio = calcular_promedio(lista=[])
    print(promedio)
except Exception as e:
    print ("la funcion no calculó el promedio")
    print(e)

try:
    promedio = calcular_promedio(lista=[""])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print ("la funcion no calculó el promedio")
    print(e)