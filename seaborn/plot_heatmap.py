import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

rows, cols = 4, 5
arr = np.random.rand(rows, cols)
row_names = list(range(1, rows + 1))
col_names = list(range(1, cols + 1))

# plot matrix
sns.heatmap(
    arr,
    vmin=0, vmax=1,  # set limits to colour bar
    cmap=plt.cm.Oranges,
    square=True,  # shape of each cell is a square (arr need not be a square matrix)
    annot=True,  # annotate cells
    xticklabels=col_names,
    yticklabels=row_names
)

# set x and y labels
plt.xlabel('x-label name (diana)')
plt.ylabel('y-label name (sam)')
plt.tight_layout()
plt.show()
