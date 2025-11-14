import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]

old_range = np.max(counts) - np.min(counts)
new_range = 1 - 0.2
new_counts = (((counts - np.min(counts)) * new_range) / old_range) + 0.2

bar_colors = ['red', 'blue', 'yellow', 'orange', 'olive']

ax.bar(fruits, new_counts, label=bar_colors, color=bar_colors)

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()