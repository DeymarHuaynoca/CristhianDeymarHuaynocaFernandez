def tiene_solucion(a, b, c, d):
    return (a * d - b * c) != 0

def get_x(a, b, c, d, e, f):
    return (e * d - b * f) / (a * d - b * c)

def get_y(a, b, c, d, e, f):
    return (a * f - e * c) / (a * d - b * c)

a, b, c, d, e, f = map(float, input("ingrese a, b, c, d, e, f:").split())

if tiene_solucion(a, b, c, d):
    print("x :", get_x(a, b, c, d, e, f))
    print("y :", get_y(a, b, c, d, e, f))
else:
    print("la ecuación no tiene solucion")


