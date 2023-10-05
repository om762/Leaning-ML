import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20, 15)

fig = plt.figure()
ax = fig.add_axes((0,0,1,1))

# for i in range(20,40):
#     ax.plot(x, x+i, color = '#'+str(i)+ str(i) + str(round(33*2, 2)))

# possible linestype options ‘--‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x, color = 'red', linewidth = 4, ls = '-.')

# Link for markers -> https://matplotlib.org/stable/api/markers_api.html
ax.plot(x, x**2, color = 'blue', lw = 2, linestyle = '--', marker = '$Om762$', markersize = 40)
plt.show()