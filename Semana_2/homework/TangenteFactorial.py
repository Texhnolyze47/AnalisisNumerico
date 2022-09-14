import math as mt

x = mt.pi / 4

y = mt.tan(x)

print("Valor real", y)

seno = 0
coseno = 0

for n in range(0, 6):
    seno += mt.pow(-1, n) / mt.factorial(2 * n + 1) * mt.pow(x, 2 * n + 1)
    coseno += pow(-1, n) * mt.pow(x, 2 * n) / mt.factorial(2 * n)
    tangente = seno / coseno

    e = abs(tangente - y)
    ep = abs((tangente - y) / y)
    print("valor aproximado ", tangente)

    print("Error absoluto", e)
    print("Error porcentual", ep)
