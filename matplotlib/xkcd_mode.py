import matplotlib.pyplot as plt

# enable xkcd mode
plt.xkcd()

# plot
plt.plot(range(100, 110), color='c')
plt.xticks(range(10), [f'{(1 + x)} pm' for x in range(10)])
plt.ylabel('number of movie goers')
plt.xlabel('time of day')
plt.title('Pirates of the Caribbean!')

plt.show()
