import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 20)
y = x*5

a = np.random.randint(10, 20, 20)
b = a * 2

fig, axis = plt.subplots(2,2)
axis[0][0].plot(x,y)
axis[0][1].plot(a,b)
axis[1][0].plot(x,y)
axis[1][1].plot(x,y)

plt.show()