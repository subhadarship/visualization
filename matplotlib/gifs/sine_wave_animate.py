import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# figure and axes setup
fig = plt.figure(figsize=(12, 6))
ax = plt.axes(xlim=(-0.25, 2), ylim=(-1.2, 1.2))

sine, = ax.plot([], [], linewidth=4, color='#212B38')
vert, = ax.plot([0, 0], [-2, 2], '--',
                color='k', linewidth=0.5)
point, = ax.plot([], [], 'o', markersize=20,
                 color='#08C6AB')


# animation function, creates the plot frame by frame (i)
def animate(i):
    # create the sine wave
    x_l = np.linspace(0, 2, 1000)
    y_l = np.sin(2 * np.pi * (x_l - 0.01 * i))
    sine.set_data(x_l, y_l)  # assign new line data
    # create the point
    x_p = np.array([0])
    y_p = [np.sin(2 * np.pi * (x_p - 0.01 * i))]
    point.set_data(x_p, y_p)


anim = animation.FuncAnimation(fig, animate, frames=500,
                               interval=20, blit=False)
plt.tight_layout()
anim.save('sine_wave.gif', fps=30, writer='imagemagick')
