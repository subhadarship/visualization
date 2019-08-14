from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# data
iris = datasets.load_iris()
X = iris.data
y = iris.target
labels = iris.target_names
colours = ['red', 'purple', 'green']

###############
##### PCA #####
###############

pca = PCA(n_components=2, whiten=True)

# fit
pca.fit(X)

# transform to get data with reduced dim
X_pca = pca.transform(X)

# plot
plt.figure(figsize=(6, 5))
for i, label in enumerate(labels):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], c=colours[i], label=label)
plt.title('PCA')
plt.legend()
plt.show()
plt.close()

################
##### tSNE #####
################

random_seed = 123

tsne = TSNE(n_components=2, random_state=random_seed)

# fit and transform to get data with reduced dim
X_tsne = tsne.fit_transform(X)

# plot
plt.figure(figsize=(6, 5))
for i, label in enumerate(labels):
    plt.scatter(X_tsne[y == i, 0], X_tsne[y == i, 1], c=colours[i], label=label)
plt.title('tSNE')
plt.legend()
plt.show()
plt.close()
