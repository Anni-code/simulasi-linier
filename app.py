import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_system(a1, b1, c1, a2, b2, c2):
    x = np.linspace(-10, 10, 400)
    y1 = (c1 - a1 * x) / b1
    y2 = (c2 - a2 * x) / b2

    fig, ax = plt.subplots()
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
    
    st.pyplot(fig)

st.title("Simulasi Sistem Persamaan Linear")

a1 = st.slider("a1 (koefisien x pertama)", -5.0, 5.0, 2.0, step=0.1)
b1 = st.slider("b1 (koefisien y pertama)", -5.0, 5.0, -1.0, step=0.1)
c1 = st.slider("c1 (konstanta pertama)", -10.0, 10.0, 1.0, step=0.1)
a2 = st.slider("a2 (koefisien x kedua)", -5.0, 5.0, -1.0, step=0.1)
b2 = st.slider("b2 (koefisien y kedua)", -5.0, 5.0, 2.0, step=0.1)
c2 = st.slider("c2 (konstanta kedua)", -10.0, 10.0, 3.0, step=0.1)

plot_system(a1, b1, c1, a2, b2, c2)
