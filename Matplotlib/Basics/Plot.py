import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = x**2
# print(x)
# print(y)

plt.plot(x, y)
plt.xlabel("X Axis ->")
plt.ylabel("Y Axis ->")
plt.xlim(0,9) # Lower Limit, Upper Limit
plt.ylim(0,81) # Lower Limit, Upper Limit
plt.savefig('Matplotlib\Basics\Plot-Image.png')
plt.show()