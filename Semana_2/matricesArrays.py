import numpy as np
# Las matrices son multidimensionales
# Esto hace que se crea una matriz con ceros
c = np.zeros((2,2))

print(c)

a = np.matrix([[1,2],[3,4]])

print(a)
b= np.matrix([[5,6],[7,8]])


print(b)

print(a + b)

# Los arrays son linealeas
# a = np.array([[1,2],[3,4]])
# print(a)
# b= np.array([[5,6],[7,8]])
#
# print(b)
#
# print(a + b)