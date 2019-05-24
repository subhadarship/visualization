import matplotlib.pyplot as plt  # sets up plotting under plt
import seaborn as sns  # sets up styles and gives us more plotting options

# load tips dataset
tips = sns.load_dataset("tips")  # loads as a pandas dataframe
print(tips.head())

# We dont Probably need the Gridlines. Do we? If yes comment this line
sns.set(style="ticks")

# So this function creates a faceted plot. The plot is parameterized by the following:

# col : divides the data points into days and creates that many plots
# palette: deep, muted, pastel, bright, dark, and colorblind. change the colors in graph. Experiment with these
# col_wrap: we want 2 graphs in a row? Yes.We do
# scatter_kws: attributes for points
# hue: Colors on a particular column.
# size: controls the size of graph

g = sns.lmplot(x="tip", y="total_bill", ci=None, data=tips, col="day",
               palette="muted", col_wrap=2, scatter_kws={"s": 100, "alpha": .5},
               line_kws={"lw": 4, "alpha": 0.5}, hue="day", x_jitter=1.0, y_jitter=1.0, height=6)

# remove the top and right line in graph
sns.despine()
# Additional line to adjust some appearance issue
plt.subplots_adjust(top=0.9)

# Set the Title of the graph from here
g.fig.suptitle('Total Bill vs. Tip', fontsize=34, color="r", alpha=0.5)

# Set the xlabel of the graph from here
g.set_xlabels("Tip", size=50, color="r", alpha=0.5)

# Set the ylabel of the graph from here
g.set_ylabels("Total Bill", size=50, color="r", alpha=0.5)

# Set the ticklabel size and color of the graph from here
titles = ['Thursday', 'Friday', 'Saturday', 'Sunday']
for ax, title in zip(g.axes.flat, titles):
    ax.tick_params(labelsize=14, labelcolor="black")

plt.tight_layout()
plt.savefig('scatterplot_subplots.png', format='png')
plt.show()
