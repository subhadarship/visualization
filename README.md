# visualization

## how to save plot in `eps` or `pdf` or `png` format?
see [`save_plot.py`](https://github.com/subhadarship/visualization/blob/master/save_plot.py)

note: `eps` and `pdf` formats are useful for `LaTeX`

## using matplotlib

see [`matplotlib/`](https://github.com/subhadarship/visualization/tree/master/matplotlib)

## using seaborn

see [`seaborn/`](https://github.com/subhadarship/visualization/tree/master/seaborn)

## dimensionality reduction

see [`matplotlib/dimensionality_reduction.py`](https://github.com/subhadarship/visualization/blob/master/matplotlib/dimensionality_reduction.py)

## plotting heatmap

see [`matplotlib/plot_heatmap.py`](https://github.com/subhadarship/visualization/blob/master/matplotlib/plot_heatmap.py), [`matplotlib/plot_matrix.py`](https://github.com/subhadarship/visualization/blob/master/matplotlib/plot_matrix.py), [`seaborn/plot_heatmap.py`](https://github.com/subhadarship/visualization/blob/master/seaborn/plot_heatmap.py)

([`seaborn/plot_heatmap.py`](https://github.com/subhadarship/visualization/blob/master/seaborn/plot_heatmap.py) is the best choice)

## plot for paper

see [`matplotlib/paper.ipynb`](https://github.com/subhadarship/visualization/blob/master/matplotlib/paper.ipynb)

Note that the following two are equivalent ([see reference](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html))
```
plot(x, y, 'go--', linewidth=2, markersize=12)
```
```
plot(x, y, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
```

## plotting error (standard deviations)

see [`matplotlib/show_errors.ipynb`](https://github.com/subhadarship/visualization/blob/master/matplotlib/show_error.ipynb)

## find optimal k in kmeans
see [`matplotlib/find_optimal_k_in_kmeans.ipynb`](https://github.com/subhadarship/visualization/blob/master/matplotlib/find_optimal_k_in_kmeans.ipynb)

full credit: [this link](https://github.com/netsatsawat/tutorial_KmeansClustering/blob/master/Tutorial_K%20Means%20Clustering.ipynb)

## poster
see [`matplotlib/poster/`](https://github.com/subhadarship/visualization/tree/master/matplotlib/poster)

credit: [this link](https://github.com/Perishleaf/data-visualisation-scripts/tree/master/matplotlib_2019_temp)

## useful resources
- [xkcd colors](https://xkcd.com/color/rgb/)
- [matplotlib markers](https://matplotlib.org/3.1.1/api/markers_api.html)
- [matplotlib line styles](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html)

