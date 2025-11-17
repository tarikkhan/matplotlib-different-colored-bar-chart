import matplotlib.animation as animation
import numpy as np
def width_animation(bars, fig):
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
    return anim

def height_animation(bars, fig, ax, height_list, original_values):
    new_heights = []
    for height in height_list:
        new_heights.append(np.linspace(0, height, 50))

    
    def init():
        for bar in bars:
            bar.set_height(0.)
        return bars

    def update(frame):
        for index, bar in enumerate(bars):
            bar.set_height(new_heights[index][frame])
        if frame == 49:
            ax.bar_label(bars, labels=original_values, padding=5)
        return bars

    anim = animation.FuncAnimation(
            fig,
            update,
            init_func=init,
            frames=50,
            interval=20,
            repeat=False
    )
    return anim