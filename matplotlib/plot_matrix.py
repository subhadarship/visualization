import matplotlib.pyplot as plt
import numpy as np

rows, cols = 4, 5
arr = np.random.rand(rows, cols)
row_names = list(range(1, rows + 1))
col_names = list(range(1, cols + 1))

# plot matrix
plt.matshow(arr, cmap=plt.cm.Oranges)

# annotate cells
for (i, j), value in np.ndenumerate(arr):
    plt.text(j, i, f'{value:.2f}', horizontalalignment='center')
    # note the interchange of i and j above

# show colour bar
plt.colorbar()

# set limits to colour bar
plt.clim(vmin=0, vmax=1)

# set ticks
plt.tick_params(top=False, bottom=True,
                labeltop=False, labelbottom=True)
plt.yticks(range(rows), row_names)
plt.xticks(range(cols), col_names)

# set x and y labels
plt.xlabel('x-label name (diana)')
plt.ylabel('y-label name (sam)')
plt.show()
