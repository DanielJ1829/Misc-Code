import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def pattern(beta, betadot, alpha_deg, npts=2000):
    alpha = np.deg2rad(alpha_deg)
    th = np.linspace(0, 2*np.pi, npts, endpoint=False)
    n = np.stack([np.cos(th), np.sin(th), np.zeros_like(th)], axis=1)

    beta_vec = np.array([beta, 0.0, 0.0])
    betadot_vec = betadot * np.array([np.cos(alpha), np.sin(alpha), 0.0])

    inner = np.cross(n - beta_vec, betadot_vec)
    num_vec = np.cross(n, inner)
    num = np.einsum("ij,ij->i", num_vec, num_vec)

    kappa = 1.0 - n @ beta_vec
    kappa = np.clip(kappa, 1e-6, None)
    p = num / (kappa**5)

    return th, p / np.max(p)

# Initial values
beta0, betadot0, alpha0 = 0.5, 0.2, 90.0

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection="polar")
plt.subplots_adjust(bottom=0.22)

th, p = pattern(beta0, betadot0, alpha0)
(line,) = ax.plot(th, p)
ax.set_title("Normalized dP/dΩ shape (plane cut)")

# Sliders
axb = plt.axes([0.15, 0.12, 0.7, 0.03])
axbd = plt.axes([0.15, 0.08, 0.7, 0.03])
axa = plt.axes([0.15, 0.04, 0.7, 0.03])

sb = Slider(axb, "beta", 0.0, 0.99, valinit=beta0, valstep=0.01)
sbd = Slider(axbd, "betadot", 0.0, 2.0, valinit=betadot0, valstep=0.02)
sa = Slider(axa, "alpha(deg)", 0.0, 180.0, valinit=alpha0, valstep=1.0)

def update(val):
    th, p = pattern(sb.val, sbd.val, sa.val)
    line.set_data(th, p)
    ax.set_title(f"Normalized dP/dΩ shape   β={sb.val:.2f}, βdot={sbd.val:.2f}, α={sa.val:.0f}°")
    fig.canvas.draw_idle()

sb.on_changed(update)
sbd.on_changed(update)
sa.on_changed(update)

plt.show()