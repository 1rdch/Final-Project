import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# -----------------------------
# Parameters
# -----------------------------
res = 120
size = 10
base_height = 0.5
peak_height = 3.0
num_peaks = 6
wave_amp = 0.8
wave_freq = 5


# -----------------------------
# Create XY grid
# -----------------------------
x = np.linspace(-size, size, res)
y = np.linspace(-size, size, res)
X, Y = np.meshgrid(x, y)


# -----------------------------
# Base undulating surface
# -----------------------------
Z = base_height * (
    np.sin(0.25 * X) * np.cos(0.25 * Y) +
    0.3 * np.sin(0.45 * X + 1.2 * Y)
)


# -----------------------------
# Add random Gaussian peaks
# -----------------------------
np.random.seed(3)

for _ in range(num_peaks):
    px = np.random.uniform(-size * 0.7, size * 0.7)
    py = np.random.uniform(-size * 0.7, size * 0.7)
    pr = np.random.uniform(1.8, 3.5)

    Z += peak_height * np.exp(-((X - px)**2 + (Y - py)**2) / (2 * pr**2))


# -----------------------------
# Add radial wave (rib effect)
# -----------------------------
R = np.sqrt(X**2 + Y**2)
Z += wave_amp * np.sin(wave_freq * R)


# -----------------------------
# Plot (Surface + Wireframe edges)
# -----------------------------
fig = plt.figure(figsize=(12, 9), dpi=120)
ax = fig.add_subplot(111, projection='3d')

# surface (white, smooth shading)
ax.plot_surface(
    X, Y, Z,
    rstride=1, cstride=1,
    color="#f2f2f2",
    edgecolor="none",
    linewidth=0,
    antialiased=True
)

# wireframe edges (black)
ax.plot_wireframe(
    X, Y, Z,
    rstride=6, cstride=6,
    color="black",
    linewidth=0.5
)

# clean visual style
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_box_aspect([1, 1, 0.35])

ax.view_init(elev=28, azim=35)
ax.set_title("Parametric Vault — Multi-Peak + Wave (Surface + Edges)", fontsize=14)

plt.show()
