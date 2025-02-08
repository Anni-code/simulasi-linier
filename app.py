import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def plot_system(a1, b1, c1, a2, b2, c2):
    x = np.linspace(-10, 10, 400)
    y1 = (c1 - a1 * x) / b1
    y2 = (c2 - a2 * x) / b2

    plt.figure(figsize=(6,6))
    plt.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
    plt.plot(x, y2, label=f'{a2}x + {b2}y = {c2}')

    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])

    try:
        sol = np.linalg.solve(A, B)
        plt.plot(sol[0], sol[1], 'ro', label=f'Solusi ({sol[0]:.2f}, {sol[1]:.2f})')
    except np.linalg.LinAlgError:
        plt.title("Tidak ada solusi unik")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

interact(plot_system,
         a1=FloatSlider(min=-5, max=5, step=0.1, value=2),
         b1=FloatSlider(min=-5, max=5, step=0.1, value=-1),
         c1=FloatSlider(min=-10, max=10, step=0.1, value=1),
         a2=FloatSlider(min=-5, max=5, step=0.1, value=-1),
         b2=FloatSlider(min=-5, max=5, step=0.1, value=2),
         c2=FloatSlider(min=-10, max=10, step=0.1, value=3))
