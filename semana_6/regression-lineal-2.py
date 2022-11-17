import numpy as np
import matplotlib.pyplot as plt
from  numpy.linalg import inv

x = np.random.randint(0, 100, size=10)
y = np.random.randint(0, 100, size=10)
n = len(x)

b = sum(n * sum(x * y) - sum(x) * sum(y))/(n*sum(x**2) - sum(x) ** 2)
a = sum(y) / n - sum(x) / n * b

xx = np.arange( min(x) -0.5, max(x) + 0.5,0.001)
yy = a * b * xx
print(a,b)

plt.plot(x,y,'g*',xx,yy,'r:')
x0 = sum(x)
x1= sum(x ** 2)
y0 = sum(y)
y1 = sum(x*y)
mp = np.matrix([[n,x0],[x0,x1]])
mr = np.matrix([y0][y1])
mp = inv(mp)
mr = mp * mr
yy1 = [0,0] + mr[1,0] * xx
plt.plot(xx,yy1,'k:')
plt.show()

## desarallar para orden 2 pero solo pidiendo los datos


