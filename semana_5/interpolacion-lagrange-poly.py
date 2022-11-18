import matplotlib.pyplot as plt
import numpy as np

def lagrange_interpolation(x,y,xx):
    n = len(x)
    sum = 0
    for i in range(n):
        product = y[i]
        for j in range(n):
            if i != j:
                product = product*(xx - x[j])/(x[i]-x[j])
        sum = sum + product
    return sum

#x = [1, 3, 5, 7, 13]
#y = [800, 2310, 3090, 3940, 4755]
x = [1, 4, 6]
y = [0, 1.386294, 1.791760]
#x = [1,4,6, 5, 3, 1.5, 2.5, 3.5]
#y = [0, 1.3862944, 1.7917595, 1.6094379, 1.0986123 , 0.4054641, 0.9162907, 1.2527630]
plt.scatter(x,y)
xx = np.linspace(0, 8, 100)
yy = [lagrange_interpolation(x,y,i) for i in xx]

xo= np.linspace(0.01,8,200)
#plt.plot(xo, np.log(xo), label="f(x)=lnx", color="black")
plt.plot(xx,yy)
plt.show()