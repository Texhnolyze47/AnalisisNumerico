import math as mt


x = mt.pi / 4

seno = 0
coseno = 0


for n in range(0, 50):
    seno += math.pow(-1,n) / mt.factorial(2 * n + 1) * math.pow(x, 2*n + 1)
    coseno += pow(-1, n)* mt.pow(x,2 * n) / mt.factorial(2*n)
    tangente = seno / coseno
    print("valor aproximado ", tangente)











