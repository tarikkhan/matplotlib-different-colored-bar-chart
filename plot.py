import matplotlib.pyplot as plt


from helpers import scale_values
from animate import width_animation


fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]

new_counts = scale_values(counts)

bar_colors_labels = ['red', 'blue', 'gold', 'orange', 'olive']

bars = ax.bar(fruits, new_counts, color=bar_colors_labels, label=bar_colors_labels)


width_animation = width_animation(bars, fig)

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()