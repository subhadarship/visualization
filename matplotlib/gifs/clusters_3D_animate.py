import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


# create cluster builder
def cluster(center, radius=10, n=50):
    c = np.asarray(center)
    xx, yy, zz = np.random.uniform(c - radius, c + radius, size=(n, 3)).T
    return xx, yy, zz


# create random cluster
xx1, yy1, zz1 = cluster((25, 15, 5))
xx2, yy2, zz2 = cluster((5, 5, 20))

# create a figure
fig = plt.figure()
# initialise 3D Axes
ax = Axes3D(fig)
ax.grid(False)


# create the initialiser with our two clusters
def init():
    ax.scatter(xx1, yy1, zz1, marker='o', s=40, c='#08C6AB', alpha=0.6)
    ax.scatter(xx2, yy2, zz2, marker='o', s=40, c='#37465B', alpha=0.6)
    return fig,


# create animate function, this will adjust the view one step at a time
def animate(i):
    ax.view_init(elev=10.0, azim=i)
    return fig,


# create the animated plot
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)
# save as a GIF
anim.save('clusters.gif', fps=30, writer='imagemagick')
