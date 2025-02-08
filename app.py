import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Fungsi untuk plotting sistem persamaan linier
def plot_system(a1, b1, c1, a2, b2, c2):
    x = np.linspace(-10, 10, 400)
    
    # Hindari pembagian dengan nol
    if b1 != 0:
        y1 = (c1 - a1 * x) / b1
    else:
        y1 = np.full_like(x, c1 / a1)  # Garis vertikal

    if b2 != 0:
        y2 = (c2 - a2 * x) / b2
    else:
        y2 = np.full_like(x, c2 / a2)  # Garis vertikal

    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
    ax.plot(x, y2, label=f'{a2}x + {b2}y = {c2}')

    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])

    try:
        sol = np.linalg.solve(A, B)
        ax.plot(sol[0], sol[1], 'ro', label=f'Solusi ({sol[0]:.2f}, {sol[1]:.2f})')
    except np.linalg.LinAlgError:
        ax.set_title("Tidak ada solusi unik")

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    
    return fig

# Streamlit UI
st.title("Simulasi Sistem Persamaan Linier")

a1 = st.slider("a1", -5.0, 5.0, 2.0, 0.1)
b1 = st.slider("b1", -5.0, 5.0, -1.0, 0.1)
c1 = st.slider("c1", -10.0, 10.0, 1.0, 0.1)
a2 = st.slider("a2", -5.0, 5.0, -1.0, 0.1)
b2 = st.slider("b2", -5.0, 5.0, 2.0, 0.1)
c2 = st.slider("c2", -10.0, 10.0, 3.0, 0.1)

fig = plot_system(a1, b1, c1, a2, b2, c2)
st.pyplot(fig)
