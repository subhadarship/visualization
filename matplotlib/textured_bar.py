import matplotlib.pyplot as plt

names = ['cotton', 'bajra', 'corn']
diana = [400, 500, 600]
sam = [400, 500, 600]
idx = [i for i, names in enumerate(names)]

plt.bar(idx, diana, color='cyan', hatch="/", label='diana')
plt.bar(idx, sam, bottom=diana,
        color='red', hatch='\\',
        label='sam')
plt.title('crops owned')
plt.ylabel('number of acres')
plt.xlabel('crops')

# set xticks
plt.xticks(idx, names)

# create 'draggable' legend with 2 cols, custom prob size
plt.legend(ncol=2, prop={'size': 14}).draggable()
plt.show()
