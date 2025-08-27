import math

def promedio(lista):
    return sum(lista) / len(lista)

def desviacion(lista):
    m = promedio(lista)
    return math.sqrt(sum((x - m)**2 for x in lista) / (len(lista) - 1))

numeros = list(map(float, input("ingrese 10 numeros:").split()))
print(f"el promedio es {promedio(numeros):.5f}")
print(f"la desviacion estandar es {desviacion(numeros):.5f}")
