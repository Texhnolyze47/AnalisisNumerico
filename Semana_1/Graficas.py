import numpy as np
import matplotlib.pyplot as plt

# y = x^2
x = np.arange(-2, 2, .1)
# se eleva a la segunda potencia
y = x ** 2

plt.plot(x, y)
plt.show()
