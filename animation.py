#matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib import animation
import IPython.display
import scipy
import sympy.vector
def f(r, z, t):
    sin_sq = r**2/(r**2+z**2)
    cos_sq = (np.cos(2*np.pi*(t-np.sqrt(r**2+z**2))))**2
    r_sq = r**2+z**2
    return sin_sq*cos_sq/r_sq

x1_grid, x2_grid = np.meshgrid(np.linspace(-2,2, 200),np.linspace(-2,2, 200))
fig = plt.figure(figsize=(9, 9), dpi=1080/18)
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2), aspect='equal')
mesh = ax.pcolormesh(x1_grid, x2_grid, np.zeros_like(x1_grid), cmap=cm.coolwarm, vmin=0, vmax=2)
a_text = ax.text(0.02, 0.85, '', transform=ax.transAxes, fontsize=30)
cb = plt.colorbar(mesh)

def animate(time):
    ft = f(x1_grid, x2_grid, time)
    mesh.set_array(ft.ravel())
    a_text.set_text('$t$ = {:.3f}'.format(time))
    return mesh, a_text

anim = animation.FuncAnimation(
    fig, 
    animate, 
    frames=np.linspace(0, 5, 500), 
    interval=50, 
    blit=True,
    repeat=False
)
plt.close(fig)
IPython.display.HTML(anim.to_html5_video())