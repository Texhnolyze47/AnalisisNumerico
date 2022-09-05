import numpy as np

a = np.zeros(4)

# for i in range(4):
#     a[i] = float(input("Introduzca un dato numerico"))
#
# print(a)

# for i in range(1,5):
#     a[i-1] = float(input("Introduzca un dato numerico"))
#
# print(a)

i = 0
while i < 4:
    a[i] = float(input("Introduzca un dato numerico"))
    if a[i] % 2 == 0:
        print("El numero par es ", a[i])
    else:
        print("El numero es impar ", a[i])
    i += 1

print(a)
