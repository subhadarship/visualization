import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, cm
from mpl_toolkits.mplot3d import Axes3D

# create a figure
fig = plt.figure()
# initialise 3D Axes
ax = Axes3D(fig)
# remove background grid, fill and axis
ax.grid(False)
ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
plt.axis('off')
# tighter fit to window
plt.tight_layout()

# create surface values
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
xx, yy = np.meshgrid(x, y)
r = np.sqrt(xx ** 2 + yy ** 2)
z = np.cos(r)


# create the initialiser with the surface plot
def init():
    ax.plot_surface(xx, yy, z, cmap=cm.gnuplot,
                    linewidth=0, antialiased=False)
    return fig,


# create animate function, this will adjust the view one step at a time
def animate(i):
    ax.view_init(elev=30.0, azim=i)
    return fig,


# create the animated plot
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
# save as a GIF
anim.save('surface_rotation.gif', fps=30, writer='imagemagick')
