import matplotlib.pyplot as plt  # sets up plotting under plt
import seaborn as sns  # sets up styles and gives us more plotting options

# load tips dataset
tips = sns.load_dataset("tips")  # loads as a pandas dataframe
print(tips.head())

# We dont Probably need the Gridlines. Do we? If yes comment this line
sns.set(style="ticks")

# Here we create a matplotlib axes object. The extra parameters we use
# "ci" to remove confidence interval
# "marker" to have a x as marker.
# "scatter_kws" to provide style info for the points.[s for size]
# "line_kws" to provide style info for the line.[lw for line width]

g = sns.regplot(x="tip", y="total_bill", data=tips, ci=False,
                scatter_kws={"color": "darkred", "alpha": 0.3, "s": 90},
                line_kws={"color": "g", "alpha": 0.5, "lw": 4}, marker="x")

# remove the top and right line in graph
sns.despine()

# Set the size of the graph from here
g.figure.set_size_inches(12, 8)
# Set the Title of the graph from here
g.axes.set_title('Total Bill vs. Tip', fontsize=34, color="r", alpha=0.5)
# Set the xlabel of the graph from here
g.set_xlabel("Tip", size=67, color="r", alpha=0.5)
# Set the ylabel of the graph from here
g.set_ylabel("Total Bill", size=67, color="r", alpha=0.5)
# Set the ticklabel size and color of the graph from here
g.tick_params(labelsize=14, labelcolor="black")

plt.tight_layout()
plt.savefig('scatterplot.png', format='png')
plt.show()
