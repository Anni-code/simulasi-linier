# Persyaratan: pip install numpy matplotlib streamlit

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def main():
    st.title('Sistem Persamaan Linear Interaktif')
    
    # Membuat slider di sidebar
    st.sidebar.header('Koefisien Persamaan 1')
    a1 = st.sidebar.slider('a1', -5.0, 5.0, 2.0, 0.1)
    b1 = st.sidebar.slider('b1', -5.0, 5.0, -1.0, 0.1)
    c1 = st.sidebar.slider('c1', -10.0, 10.0, 1.0, 0.1)
    
    st.sidebar.header('Koefisien Persamaan 2')
    a2 = st.sidebar.slider('a2', -5.0, 5.0, -1.0, 0.1)
    b2 = st.sidebar.slider('b2', -5.0, 5.0, 2.0, 0.1)
    c2 = st.sidebar.slider('c2', -10.0, 10.0, 3.0, 0.1)
    
    # Menghitung persamaan garis
    x = np.linspace(-10, 10, 400)
    y1 = (c1 - a1 * x) / b1
    y2 = (c2 - a2 * x) / b2
    
    # Membuat plot
    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(x, y1, label=f'{a1}x + {b1}y = {c1}')
    ax.plot(x, y2, label=f'{a2}x + {b2}y = {c2}')
    
    # Mencari solusi
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([c1, c2])
    
    try:
        sol = np.linalg.solve(A, B)
        ax.plot(sol[0], sol[1], 'ro', label=f'Solusi ({sol[0]:.2f}, {sol[1]:.2f})')
        st.success(f"Solusi unik: ({sol[0]:.2f}, {sol[1]:.2f})")
    except np.linalg.LinAlgError:
        st.error("Tidak ada solusi unik (garis sejajar atau berimpit)")
    
    # Formatting plot
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()