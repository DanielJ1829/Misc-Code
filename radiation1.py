import numpy as np
import matplotlib.pyplot as plt

# ------------- 3D "radiation pattern surface": radius = sin^2(theta) -------------
# theta: polar angle from +z axis; phi: azimuth around z
theta = np.linspace(0, np.pi, 240)
phi = np.linspace(0, 2*np.pi, 240)
TH, PH = np.meshgrid(theta, phi, indexing="ij")

# Intensity pattern (up to a constant)
R = np.sin(TH)**2

# Spherical -> Cartesian (surface radius depends on theta)
X = R * np.sin(TH) * np.cos(PH)
Y = R * np.sin(TH) * np.sin(PH)
Z = R * np.cos(TH)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True)

ax.set_title(r"3D surface for $dP/d\Omega \propto \sin^2\theta$ (z = accel axis)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Make it less visually misleading (equal-ish aspect)
try:
    ax.set_box_aspect([1, 1, 1])
except Exception:
    pass

plt.show()