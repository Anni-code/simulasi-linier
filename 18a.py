import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_triangle_and_lines(y, m):
    P = np.array([2, 4])
    Q = np.array([2, 6])
    R = np.array([4, y])
    
    fig, ax = plt.subplots()
    
    # Plot segitiga PQR
    triangle = np.array([P, Q, R, P])  # Loop back to P
    ax.plot(triangle[:, 0], triangle[:, 1], 'bo-', label='Segitiga PQR')
    
    # Plot garis l
    x_vals = np.linspace(-1, 5, 100)
    y_vals = m * x_vals  # Garis l dari (0,0)
    ax.plot(x_vals, y_vals, 'r--', label=f'Garis l (m={m})')
    
    ax.set_xlim(-1, 5)
    ax.set_ylim(-5, 20)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_title(f"Simulasi dengan y={y}, m={m}")
    st.pyplot(fig)

# Streamlit UI
y = st.slider("Pilih nilai y", min_value=-4.0, max_value=16.0, step=0.5, value=8.0)
m = st.slider("Pilih nilai m", min_value=-2.0, max_value=3.0, step=0.1, value=1.0)

if st.button("Tampilkan Simulasi"):
    plot_triangle_and_lines(y, m)
