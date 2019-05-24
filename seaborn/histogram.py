import matplotlib.pyplot as plt  # sets up plotting under plt
import numpy as np
import seaborn as sns  # sets up styles and gives us more plotting options

# Create a list of 1000 Normal RVs
x = np.random.normal(size=1000)

sns.set_context("poster")
sns.set_style("ticks")
# This  Function creates a normed Histogram by default.
# If we use the parameter kde=False and norm_hist=False then
# we will be using a count histogram

g = sns.distplot(x,
                 kde_kws={"color": "g", "lw": 4, "label": "KDE Estim", "alpha": 0.5},
                 hist_kws={"color": "r", "alpha": 0.3, "label": "Freq"})

# remove the top and right line in graph
sns.despine()

# Set the size of the graph from here
g.figure.set_size_inches(12, 7)
# Set the Title of the graph from here
g.axes.set_title('Normal Simulation', fontsize=34, color="b", alpha=0.3)
# Set the xlabel of the graph from here
g.set_xlabel("X", size=67, color="g", alpha=0.5)
# Set the ylabel of the graph from here
g.set_ylabel("Density", size=67, color="r", alpha=0.5)
# Set the ticklabel size and color of the graph from here
g.tick_params(labelsize=14, labelcolor="black")

plt.tight_layout()
plt.savefig('histogram.png', format='png')
plt.show()
