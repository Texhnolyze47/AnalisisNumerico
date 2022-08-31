import numpy as np

a= np.matrix([0,1,2,3,4,5])
b= np.matrix([0,1,2,3,4,5])
print(a + b)

# por defecto los valores por teclado de valor string
# tenemos que convertirlo a tipo numerico
c = int(input("Proporciona un numero "))

print(c)

print(c * (a + b))