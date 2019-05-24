import matplotlib.pyplot as plt  # sets up plotting under plt
import seaborn as sns  # sets up styles and gives us more plotting options

# load tips dataset
tips = sns.load_dataset("tips")  # loads as a pandas dataframe
print(tips.head())

sns.set(style="ticks")

flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]

# This Function takes as input a custom palette
g = sns.barplot(x="sex", y="tip", hue="day",
                palette=sns.color_palette(flatui), data=tips, ci=None)

# remove the top and right line in graph
sns.despine()

# Set the size of the graph from here
g.figure.set_size_inches(12, 7)
# Set the Title of the graph from here
g.axes.set_title('Do We tend to \nTip high on Weekends?',
                 fontsize=34, color="b", alpha=0.3)
# Set the xlabel of the graph from here
g.set_xlabel("Gender", size=67, color="g", alpha=0.5)
# Set the ylabel of the graph from here
g.set_ylabel("Mean Tips", size=67, color="r", alpha=0.5)
# Set the ticklabel size and color of the graph from here
g.tick_params(labelsize=14, labelcolor="black")

plt.tight_layout()
plt.savefig('barplot.png', format='png')
plt.show()
