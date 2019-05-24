import matplotlib.pyplot as plt
import seaborn as sns

# load iris data
iris = sns.load_dataset("iris")
print(iris.head())

# Create a Pairplot
g = sns.pairplot(iris, hue="species", palette="muted", size=5,
                 vars=["sepal_width", "sepal_length"], kind='reg', markers=['o', 'x', '+'])

# To change the size of the scatterpoints in graph
g = g.map_offdiag(plt.scatter, s=35, alpha=0.5)

# remove the top and right line in graph
sns.despine()
# Additional line to adjust some appearance issue
plt.subplots_adjust(top=0.9)

# Set the Title of the graph from here
g.fig.suptitle('Relation between Sepal Width and Sepal Length',
               fontsize=34, color="b", alpha=0.3)

plt.tight_layout()
plt.savefig('pairplot.png', format='png')
plt.show()
