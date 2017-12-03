import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

cmap = mpl.cm.cool #colour map is set as the "jet" colour map which is blue to red
print cmap(1)
fig = plt.figure(figsize=(8, 2)) #makes a figure
ax1 = fig.add_axes([0.05, 0.8, 0.03, 1]) #x,y place ; x,y length
ax2 = fig.add_axes([0.05, 0.4, 0.3, 0.1])
# ax1 = fig.add_axes([0.2572e+01, 0.8214e+00, 0.5689e+01, -0.8214e+00, -0.2572e+01, -0.4292e+01, 0.4292e+01, -0.5689e+01])
norm = mpl.colors.LogNorm(0.001,1) #creates the range of the colour map
cb1 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap, norm=norm, orientation='vertical')
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, orientation='horizontal')
plt.show()

plt.plot(np.arange(0,10,1),np.arange(0,20,2)**2,color=cmap(1))
plt.show()