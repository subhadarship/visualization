import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import animation, cm
from matplotlib import patches as mpatches
from matplotlib.colors import ListedColormap


def make_sun(ax, cx, cy, r):
    def make_grad(cx, cy, r, alpha):
        circ = mpatches.Circle((cx, cy), r, facecolor='none')
        ax.add_patch(circ)

        plt.imshow([[1, 1], [0, 0]],
                   cmap=cm.plasma,
                   interpolation='bicubic',
                   aspect='auto',
                   extent=(cx - r, cx + r, cy - r, cy + r),
                   alpha=alpha,
                   clip_path=circ,
                   clip_on=True)

    make_grad(cx, cy, r + .2, alpha=.4)
    make_grad(cx, cy, r + .4, alpha=.4)
    make_grad(cx, cy, r + .8, alpha=.4)
    make_grad(cx, cy, r + .16, alpha=.4)
    make_grad(cx, cy, r, alpha=1)

    ax.plot([cx - r, cx + r], [cy - (r * 0.8), cy - (r * 0.8)],
            linewidth=r * .4, color='k')

    ax.plot([cx - r, cx + r], [cy - (r * 0.6), cy - (r * 0.6)],
            linewidth=r * .3, color='k')

    ax.plot([cx - r, cx + r], [cy - (r * 0.4), cy - (r * 0.4)],
            linewidth=r * .2, color='k')

    ax.plot([cx - r * 1.1, cx + r * 1.1], [cy - (r * 0.2), cy - (r * 0.2)],
            linewidth=r * .1, color='k')


def make_skyline(ax, min_x, max_x, min_y, max_y, towers=30,
                 colour='k', heights=None):
    if heights is None:
        heights = np.random.randint(0, max_y - min_y, towers)

    x = np.linspace(min_x, max_x, towers)

    ax.bar(x, heights, width=(max_x / towers) * 2, align='edge',
           bottom=min_y, color=colour)


def make_stars(ax, min_x, max_x, min_y, max_y, stars=100):
    # !!! TODO: to add alpha so that at min_y alpha = 0 and at max_y/2 alpha = 1
    x = np.random.uniform(min_x, max_x, stars)
    y = np.random.uniform(min_y, max_y, stars)
    alpha_multiplier = np.random.uniform(.5, 1, len(x))
    size = np.random.uniform(1, 6, len(x))

    for i in range(len(y)):
        # calculate relative height
        h = (y[i] - min_y) / (max_y - min_y)

        ax.scatter(x[i], y[i], alpha=h * alpha_multiplier[i] * .1,
                   s=size + .4, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h * alpha_multiplier[i] * .1,
                   s=size + .3, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h * alpha_multiplier[i] * .1,
                   s=size + .2, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h * alpha_multiplier[i] * .1,
                   s=size + .1, c='#ffffff', zorder=0)
        ax.scatter(x[i], y[i], alpha=h * alpha_multiplier[i] * .6,
                   s=size, c='#ffffff', zorder=0)

    return np.array([x, y, alpha_multiplier, size]).T


background = '#000000'
horizon = {'grad': cm.gnuplot(range(28)),  # only take black to purple part of gradient
           'dist': 18}
ground = {'grad': cm.gnuplot(range(12)),  # only black -> purple gradient
          'dist': 50}

matplotlib.rcParams['axes.facecolor'] = background

# key parameters
perspective = (0, 5)
motion_lines = 10
frames = 200
xlim = (-100, 100)
ylim = (-50, 70)

# figure and axes setup
fig = plt.figure(figsize=(20, 12))
ax = plt.axes(xlim=xlim, ylim=ylim)
exp_debug = False

# create gradient ground foreground
plt.imshow([[0, 0], [1, 1]],
           cmap=ListedColormap(ground['grad']),
           interpolation='bicubic',
           aspect='auto',
           extent=(xlim[0], xlim[1], 0, -ground['dist']))

make_sun(ax, 0, 40, 20)
stars = make_stars(ax, xlim[0], xlim[1], 10, ylim[1])

# create gradient background
plt.imshow([[0, 0], [1, 1]],
           # only black-to-purple part of gnuplot
           cmap=ListedColormap(horizon['grad']),
           interpolation='bicubic',
           aspect='auto',
           extent=(xlim[0], xlim[1], 0, horizon['dist']),
           zorder=-1)

make_skyline(ax, xlim[0], xlim[1], 0, 15, towers=70, colour='#000000')


# define glow building line function
def grid_line(x, y, c='#bc13fe'):
    plt.plot(x, y, color=c, linewidth=5, alpha=.2)
    plt.plot(x, y, color=c, linewidth=4, alpha=.2)
    plt.plot(x, y, color=c, linewidth=3, alpha=.2)
    plt.plot(x, y, color=c, linewidth=2.5, alpha=.2)
    plt.plot(x, y, 'w', linewidth=2, alpha=.6)


# exponential function for horizontal line movement
def exp(x, start, end, scale=0.02):
    if x >= start:
        x = x - start
        return np.exp(x * scale)
    else:
        x = end + x - start
        return np.exp(x * scale)


# creating vertical lines, originate at 0, 10 then mask all above horizon (y=0)
for i in range(int(xlim[0] * 10), int(xlim[1] * 10), int(xlim[1] / 2)):
    x = np.linspace(perspective[0], i, 60)
    y = np.linspace(perspective[1], ylim[0], 60)
    # masking anything above horizon line
    y = np.ma.masked_where(y > 0, y)
    # plotting our perspective line
    grid_line(x, y)

# initialise motion dictionary
motion = {}
# create motion lines
for i in range(motion_lines):
    motion[str(i)] = {}
    # initialise motion line
    motion[str(i)]['glow1'], = ax.plot([], [], linewidth=5,
                                       color='#bc13fe', alpha=.2)
    motion[str(i)]['glow2'], = ax.plot([], [], linewidth=4,
                                       color='#bc13fe', alpha=.2)
    motion[str(i)]['glow3'], = ax.plot([], [], linewidth=3,
                                       color='#bc13fe', alpha=.2)
    motion[str(i)]['glow4'], = ax.plot([], [], linewidth=2.5,
                                       color='#bc13fe', alpha=.2)
    motion[str(i)]['line'], = ax.plot([], [], linewidth=2,
                                      color='w', alpha=.6)

# create horizon line (we'll make a few to create illusion of distance density
grid_line([xlim[0], xlim[1]], [0, 0])
grid_line([xlim[0], xlim[1]], [-.25, -.25])
grid_line([xlim[0], xlim[1]], [-.75, -.75])

if exp_debug:
    x = np.linspace(0, 50, 50)
    for j in range(motion_lines):
        plt.figure(figsize=(8, 8))
        # get start position for exponential func
        start = (50 / motion_lines) * j
        # y is assigned using the exponential function
        y = [exp(x_, start, 50) for x_ in x]
        grid_line(x, y)
        plt.tight_layout()
        plt.savefig(f'exp_{j}.png')

    plt.figure(figsize=(16, 8))
    c = ['#bc13fe', '#1b03a3', '#0A9C9C', '#39ff14', '#ccff00',
         '#FAED27', '#FD5F00', '#ff073a', '#ff2965', '#ff69b4']
    for j in range(motion_lines):
        # get start position for exponential func
        start = (50 / motion_lines) * j
        # y is assigned using the exponential function
        y = [exp(x_, start, 50) for x_ in x]
        grid_line(x, y, c=c[j])
    plt.tight_layout()
    plt.savefig('exp_all.png')

# select random sample of the stars to make sparkle
stars = stars[stars[:, 1] > 30]  # only stars in the upper part of the sky
select = np.random.randint(0, len(stars), int(len(stars) * 0.6))
stars = stars[list(select)]


# animation function, creates the plot frame by frame (i)
def animate(i):
    # movement lines will decrease y position exponentially with i
    x = [xlim[0], xlim[1]]
    # assign new line data for motion lines
    for j in range(motion_lines):
        # get start position for exponential func
        start = (frames / motion_lines) * j
        # y is assigned using the exponential function
        y = [-exp(i, start, frames) + 1] * 2
        # set data for each line
        for line in motion[str(j)]:
            motion[str(j)][line].set_data(x, y)

    # make the stars sparkle
    for star in stars:
        alpha = np.random.uniform(0, .3)
        ax.scatter(star[0], star[1], s=star[2] + .4, alpha=alpha,
                   c='#ffffff', zorder=0)
        dark = np.random.uniform(0, .3)
        ax.scatter(star[0], star[1], s=star[2] + .4, alpha=dark,
                   c='#000000', zorder=0)


anim = animation.FuncAnimation(fig, animate, frames=int(frames / 10),
                               interval=20, blit=False)
plt.tight_layout()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
anim.save('synthwave.gif', fps=60, writer='imagemagick')
