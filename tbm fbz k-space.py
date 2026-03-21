#%%
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
E_0 = -13.6
a = 1
t = 6
b_1 = np.arange(-np.pi/a, np.pi/a, 0.25)
b_2 = np.arange(-np.pi/a, np.pi/a, 0.25)
B_1,B_2 = np.meshgrid(b_1, b_2)
E_prime = E_0/t-2*(np.cos(B_1*a)+np.cos(B_2*a)) #E_prime = E/t

# Plot the surface.
surf = ax.plot_surface(B_1, B_2, E_prime, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-4,4)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')
ax.set_title('First Brillouin Zone: Energy in a square lattice (a=1)')
ax.set_xlabel('-pi<b_1<pi')
ax.set_ylabel('-pi<b_2<pi')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()