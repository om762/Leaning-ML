import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,100)
y = x**2
# print(x)
# print(y)

plt.plot(x, y)
plt.xlabel("X Axis ->")
plt.ylabel("Y Axis ->")
plt.xlim(0,100) # Lower Limit, Upper Limit
plt.ylim(0,10000) # Lower Limit, Upper Limit
plt.title('Quadratic Curve')
plt.savefig('Matplotlib\Basics\Plot-Image.png')
plt.show()