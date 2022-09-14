import math as mt

x = mt.pi / 4

y = mt.tan(x)

print("Valor real", y)

seno = 0
coseno = 0

for n in range(0, 8):
    seno = seno + x ** (2 * n + 1) / mt.factorial(2 * n + 1) * (-1) ** n
    coseno = coseno + x ** (2 * n) / mt.factorial(2 * n) * (-1) ** n
    tangente = seno / coseno

    e = abs(tangente - y)
    ep = abs((tangente - y) / y)

    print(f"El {n+1} termino tiene el valor aproximado {tangente}, "
          f"con un error absoluto {e} y un error porcentual {ep}")
