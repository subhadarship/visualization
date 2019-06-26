import matplotlib.pyplot as plt

# Data to plot
labels = 'a', 'b', 'c', 'd'
sizes = [10, 30, 120, 40]  # total = 200
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0.1, 0)  # explode 3rd slice (slice for 'c')
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=10)
plt.axis('equal')
plt.show()
