import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 4, 5, 6, 7, 9, 12, 15])
y = np.array([np.log(x[0]), np.log(x[1]),np.log(x[2]), np.log(x[3])])
y = np.log(x)
n = len(x)
m = np.zeros((n - 1, n - 1))
for i in range(n - 1):
    m[i, 0] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])

for i in range(1, n):
    for j in range(n - 1 - i):
        m[j, i] = (m[j + 1, i - 1] - m[j, i - 1]) / (x[j + 1] - x[j])

print(m)

xx = np.arange(x[0], np.amax(x) + 0.001, 0.001)
yy = [0]
w = 1
# serie de potencias
for i in range(n):
    w = (xx-x[i]) * w
    yy = yy + m[0, i] * w
    #yy = y[0] + m[0, 0] * (xx,-x[0]) + m[0, 1] * (xx-x[0]) * (xx-x[1]) + m[0,2] * (xx-x[1]) * (xx-x[2])
plt.plot(x,y,"r*",xx,yy, "b:")
plt.show()
# b0 = y[0]
# b1 = (y[1]-y[0]) / (x[1]-x[0])
# b2 = (y[2]-y[1]) / (x[2]-x[1]) - (y[1]-y[0]) / (x[1]-x[0]) / (x[2]-x[0])
#
# xx = np.arange(x[0], x[n-1] + 0.001, 0.001)
# yy =b0 + b1 * (xx-x[0])+b2*(xx-x[0])*(xx-x[1])
# plt.plot(x,y,"r*",xx,yy,"b:")
# plt.show()
