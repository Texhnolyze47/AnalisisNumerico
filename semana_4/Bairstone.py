import numpy as np
import sympy as cm

#a = np.array([1,-3,2.75,2.125,3.875,1.2])
r =s=-1
a = np.array([1.2,-3.875,2.125,2.75,-3.5,1])
n = int(len(a))
b = np.zeros(n)
b[n-1] = a[n-1]
b[n-2] = a[n-2] + r * b[n-1]


for i in range(3,-1,-1):
    b[i] = a[i] + r * b[i + 1] + s * b[i+2]

print(b)

c = np.zeros(n)
c[n-1] = b[n-1]
c[n-2] = b[n-2] + r * c[n-1]
for i in range(n-3,0,-1):
    c[i] = b[i] + r * c[i+1] + s * c[i+2]

print(c)