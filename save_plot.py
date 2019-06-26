import matplotlib.pyplot as plt

# generate sample plot
plt.plot(range(100))

# make the layout tight to remove extra whitespace
plt.tight_layout()

# save to files, eps format useful for latex
plt.savefig('test_plot.eps', format='eps')
plt.savefig('test_plot.pdf', format='pdf')
plt.savefig('test_plot.png', format='png')

# show the plot
plt.show()
