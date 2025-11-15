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