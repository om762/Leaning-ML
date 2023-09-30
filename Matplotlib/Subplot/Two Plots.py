import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,10,11)
b = a ** 4

x = np.arange(0,10)
y = 2 * x

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(12,8))

# SET YOUR AXES PARAMETERS FIRST

# Parameters at the axes level
axes[0][0].plot(a,b)
axes[0][0].set_title('0 0 Title')


axes[1][1].plot(x,y)
axes[1][1].set_title('1 1 Title')
axes[1][1].set_xlabel('1 1 X Label')

axes[0][1].plot(y,x)
axes[1][0].plot(b,a)

# THEN SET OVERALL FIGURE PARAMETERS

# Parameters at the Figure level
fig.suptitle("Figure Level",fontsize=16)


plt.show()