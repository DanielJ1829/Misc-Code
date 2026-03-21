import time
import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio

def compute_julia(x, y, c, iterations=300, bound=2.0):
    """
    Compute Julia set iteration counts for f(z) = z^2 + c
    on a grid defined by 1D arrays x, y.
    Returns a 2D array 'iterray' of escape iterations.
    """
    xx, yy = np.meshgrid(x, y)
    z = xx + 1j * yy           #start at each point z = x + i y
    iterray = np.zeros(z.shape, dtype=int)
    mask = np.ones(z.shape, dtype=bool)

    for i in range(iterations):
        z[mask] = z[mask] ** 2 + c
        escaped = np.abs(z) >= bound
        newly_escaped = escaped & mask
        iterray[newly_escaped] = i
        mask &= ~escaped
        if not mask.any():
            break

    # Points that never escaped get iterations
    iterray[mask] = iterations
    return iterray


def plot_julia(x, y, iterray, cmap="virids", title=None, show=True, save_path=None):
    """
    Plot a single Julia set frame.
    """
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    graph = ax.contourf(x, y, iterray, cmap=cmap)
    plt.colorbar(graph)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    if title:
        plt.title(title)
    if save_path is not None:
        plt.savefig(save_path, dpi=300)
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig, ax


def make_rotating_julia_gif(gif_name="julia_rotation-1.gif",n_frames=600,fps=60,xlim=(-1.5, 1.5),ylim=(-1.5, 1.5),resolution=400,iterations=250,bound=2.0,cmap="viridis",):
    """
    Make a GIF of Julia sets for f(z) = z^2 + c as c moves along the unit circle:
        c(theta) = exp(i * theta), theta in [0, 2π).
    n_frames = number of theta samples (e.g. 600 for 10s at 60 fps).
    """

    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    thetas = np.linspace(0, 2 * np.pi, n_frames, endpoint=False)

    frames = []
    t0 = time.time()

    for idx, theta in enumerate(thetas):
        c = np.exp(1j * theta)  # c = e^{i theta}
        iterray = compute_julia(x, y, c, iterations=iterations, bound=bound)

        # Plot without showing, grab RGB buffer
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.set_aspect('equal')
        graph = ax.contourf(x, y, iterray, cmap=cmap)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(rf"$c = e^{{i\theta}},\ \theta = {theta:.2f}$")
        plt.tight_layout()

        fig.canvas.draw()
        w, h = fig.canvas.get_width_height()
        frame = np.frombuffer(fig.canvas.tostring_argb(), dtype=np.uint8)
        frame = frame.reshape((h, w, 4))
        frames.append(frame)
        plt.close(fig)

        if (idx + 1) % 50 == 0:
            t_i = time.time()
            print(f"Generated {idx + 1}/{n_frames} frames in {t_i-t0:.1f} seconds")

    t1 = time.time()
    print(f"Generated {n_frames} frames in {t1 - t0:.1f} seconds. Writing GIF…")

    imageio.mimsave(gif_name, frames, fps=fps)
    print(f"Saved GIF to {gif_name}")


if __name__ == "__main__":
    #Create static image in prettiest spot
    x = np.linspace(-1.5, 1.5, 500)
    y = np.linspace(-1.5, 1.5, 500)
    c_static = -0.5251993 + -0.5251993 * (1j)

    t_start = time.time()
    iterray_static = compute_julia(x, y, c_static, iterations=300, bound=2.0)
    t_end = time.time()
    print('Static image time taken: {:.2f} s'.format(t_end - t_start))
    plot_julia(x, y, iterray_static, cmap="viridis",title=f"Julia set for c = {c_static.real:.3f} + {c_static.imag:.3f}i")
    
    
    
    make_rotating_julia_gif(
        gif_name="julia_rotation-1.gif",
        n_frames=240,   # 10s at 60 fps
        fps=30,
        resolution=200,
        iterations=250,
        bound=2.0,
        cmap="viridis",
    )