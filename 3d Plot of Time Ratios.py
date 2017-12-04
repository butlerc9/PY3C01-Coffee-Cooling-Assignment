import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure() #starts new figure
ax = fig.add_subplot(111, projection='3d')

T0_Values = np.arange(22., 100., .5)
TD_Values = np.arange(17., 95., .5)

x, y = np.meshgrid(T0_Values, TD_Values) #creates a matrix

def surfaceplot(x, y):
    return (   np.log((x-17)/(y-12))   )/(   np.log((x-22)/(y-17))   )
print x/y



z = surfaceplot(x, y)

plt.xlabel('Initial Coffee Temperature (C)')
plt.ylabel('Drinkable Coffee Temperature (C)')
ax.set_zlabel('Ratio of tb and tc')
ratio = ax.plot_surface(x, y, z,color='g',linewidth=.5)

ax.set_zlim(0., 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

plt.show()