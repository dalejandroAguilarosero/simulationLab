import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Ejemplo: Slider + Gráfica Matplotlib")

# Slider para ajustar la frecuencia
frecuencia = st.slider("Frecuencia (Hz)", min_value=1, max_value=20, value=5)

# Datos
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(frecuencia * x)

# Crear la figura con Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title(f"Onda senoidal (f = {frecuencia} Hz)")

# Mostrar en Streamlit
st.pyplot(fig)