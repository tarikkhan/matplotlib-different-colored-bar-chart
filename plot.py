import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from helpers import scale_values


fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'banana', 'orange', 'olive']
counts = [40, 100, 300, 55, 120]

new_counts = scale_values(counts)

bar_colors_labels = ['red', 'blue', 'gold', 'orange', 'olive']

bars = ax.bar(fruits, new_counts, color=bar_colors_labels, label=bar_colors_labels)


def init():
    for bar in bars:
        bar.set_width(0.1)
    return bars

def update(frame):
    width = np.linspace(0.1, 0.8, 50)
    for bar in bars:
        bar.set_width(width[frame])
    return bars

anim = animation.FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=50,
        interval=20,
        repeat=False
)

ax.set_ylabel('Fruit Supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()