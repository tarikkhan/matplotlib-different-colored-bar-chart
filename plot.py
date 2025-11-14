import matplotlib.pyplot as plt
from helpers import scale_values


fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]

new_counts = scale_values(counts)

bar_colors_labels = ['red', 'blue', 'yellow', 'orange', 'olive']

ax.bar(fruits, new_counts, label=bar_colors_labels, color=bar_colors_labels)

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()