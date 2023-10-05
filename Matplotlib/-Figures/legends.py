import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20, 50)

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,x, label = 'Identity')
ax.plot(x, x**2, label = 'Sqaure')
ax.legend(loc = [0.50, 0.9])
plt.show()