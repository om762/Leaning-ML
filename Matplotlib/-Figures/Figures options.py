import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = 2 * x

# Creates blank canvas
fig = plt.figure(dpi = 242, figsize=(10,5), facecolor='#aabbcc' )
'''<Figure size 432x288 with 0 Axes>'''


axes = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # Large figure

# Insert Figure Axes 2
axes.plot(x,y)
# axes.set_xlim(8,10)
# axes.set_ylim()
axes.set_xlabel('X')
axes.set_ylabel('Y')
axes.set_title('Zoomed In')

plt.savefig('Matplotlib\-Figures\Dual-Axis.png')
plt.show()