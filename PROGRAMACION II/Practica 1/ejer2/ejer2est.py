import math

def get_discriminante(a, b, c):
    return b**2 - 4*a*c

def get_raices(a, b, c):
    d = get_discriminante(a, b, c)
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return [r1, r2]
    elif d == 0:
        return [-b / (2*a)]
    else:
        return []  

a, b, c = map(float, input("ingrese a, b, c:").split())
raices = get_raices(a, b, c)

if len(raices) == 2:
    print(f"la ecuacion tiene dos raices {raices[0]:.6f} y {raices[1]:.6f}")
elif len(raices) == 1:
    print(f"la ecuacion tiene una raiz {raices[0]:.6f}")
else:
    print("la ecuacion no tiene raices reales")
