import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

a = 1.5
b = 1.5
x = np.arange(0.01, 1, 0.01)
y = stats.beta.rvs(a, b, size=10000)
y_act = stats.beta.pdf(x, a, b)
g = sns.distplot(y, kde=False, norm_hist=True,
                 kde_kws={"color": "g", "lw": 4, "label": "KDE Estim", "alpha": 0.5},
                 hist_kws={"color": "r", "alpha": 0.3, "label": "Freq"})
# Note that we plotted on the graph using plt matlabplot function
plt.plot(x, y_act)

# remove the top and right line in graph
sns.despine()

# Set the size of the graph from here
g.figure.set_size_inches(12, 7)
# Set the Title of the graph from here
g.axes.set_title(("Beta Simulation vs. Calculated Beta Density\nFor a=%s,b=%s")
                 % (a, b), fontsize=34, color="b", alpha=0.3)
# Set the xlabel of the graph from here
g.set_xlabel("X", size=67, color="g", alpha=0.5)
# Set the ylabel of the graph from here
g.set_ylabel("Density", size=67, color="r", alpha=0.5)
# Set the ticklabel size and color of the graph from here
g.tick_params(labelsize=14, labelcolor="black")

plt.tight_layout()
plt.savefig('histogram2.png', format='png')
plt.show()
