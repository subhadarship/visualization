![Alt Text](https://media.giphy.com/media/l0MYGN6pCa23vnUnS/giphy.gif)

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
see [`matplotlib/poster/create_poster.ipynb`](https://github.com/subhadarship/visualization/tree/master/matplotlib/poster/create_poster.ipynb)

for customizing, see [`matplotlib/poster/customize.ipynb`](https://github.com/subhadarship/visualization/blob/master/matplotlib/poster/customize.ipynb)

credit: [this link](https://github.com/Perishleaf/data-visualisation-scripts/tree/master/matplotlib_2019_temp)

## gifs
see [`matplotlib/gifs/create_gif.ipynb`](https://github.com/subhadarship/visualization/tree/master/matplotlib/gifs/create_gif.ipynb)

credits: [this link](https://towardsdatascience.com/quick-code-exporting-matplotlib-animations-49cd0ecf32ba), [this link](http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-as-interactive-javascript-widgets/)

how to create synthwave: [`matplotlib/gifs/create_synthwave.py`](https://github.com/subhadarship/visualization/tree/master/matplotlib/gifs/create_synthwave.py) (credits: [this link](https://towardsdatascience.com/creating-synthwave-with-matplotlib-ea7c9be59760))

## cool circular bar plot
see https://github.com/probablyvivek/Comics/blob/main/Marvel.ipynb

## insert image in a plot
see https://github.com/hbshrestha/Data_Analytics/blob/main/notebooks/Inserting%20image%20to%20a%20plot%20in%20Matplotlib.ipynb

## useful resources
- colours
  - [xkcd colors](https://xkcd.com/color/rgb/)
  - [colormind](http://colormind.io/)
  - [colordesigner](https://colordesigner.io/)
- [matplotlib markers](https://matplotlib.org/3.1.1/api/markers_api.html)
- [matplotlib line styles](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html)

## LICENSE

[MIT](https://github.com/subhadarship/visualization/tree/master/LICENSE)
