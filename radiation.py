import numpy as np
import matplotlib.pyplot as plt

#2D polar plot: r(theta) = sin^2(theta)

theta = np.linspace(0, 2*np.pi, 2000)
r = np.sin(theta)**2
fig = plt.figure()
ax = fig.add_subplot(111, projection="polar")
ax.plot(theta, r)
ax.set_title(r"Radiation pattern: $dP/d\Omega \propto \sin^2\theta$")
plt.show()