import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]
bar_colors = ['red', 'blue', 'yellow', 'orange', 'olive']

ax.bar(fruits, counts, label=bar_colors, color=bar_colors)

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()