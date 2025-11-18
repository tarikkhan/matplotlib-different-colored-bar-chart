import matplotlib.pyplot as plt
import numpy as np

from helpers import scale_values
from animate import width_animation, height_animation


fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]
starting_height = np.zeros(len(counts))

new_counts = scale_values(counts)

bar_colors= ['red', 'blue', 'gold', 'orange', 'olive']

bars = ax.bar(fruits, starting_height, color=bar_colors, label=fruits)



# width_animation = width_animation(bars, fig)
height_animation = height_animation(bars, fig, ax, new_counts, counts)

# bar label code


# axes styles
ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
ax.set_ylim((0, 1.2))
plt.show()