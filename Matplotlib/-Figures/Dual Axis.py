import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a ** 4

x = np.arange(0,10)
y = 2 * x

# Creates blank canvas
fig = plt.figure()
'''<Figure size 432x288 with 0 Axes>'''


axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # Large figure
axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25]) # Smaller figure

# Larger Figure Axes 1
axes1.plot(a, b)

# Use set_ to add to the axes figure
axes1.set_xlabel('X Label')
axes1.set_ylabel('Y Label')
axes1.set_title('Big Figure')

# Insert Figure Axes 2
axes2.plot(a,b)
axes2.set_xlim(8,10)
axes2.set_ylim(4000,10000)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Zoomed In')

plt.savefig('Matplotlib\-Figures\Dual-Axis.png')
plt.show()