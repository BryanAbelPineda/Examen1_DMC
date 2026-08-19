import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="🐍",
    layout="wide"
)

# Menú lateral
modulo = st.sidebar.selectbox(
    "Índice",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# HOME
if modulo == "Home":
    st.title("🐍 Proyecto Aplicado en Streamlit")
    st.subheader("Python Fundamentals")

    st.write("Nombre: Bryan Abel Pineda")
    st.write("Módulo: Python Fundamentals")
    st.write("Año: 2026")

    st.markdown("---")

    st.markdown("""
    ### Descripción

    Esta aplicación integra los ejercicios desarrollados durante el módulo
    de Python Fundamentals utilizando Streamlit.

    ### Tecnologías utilizadas

    - Python
    - Streamlit
    - NumPy
    - Pandas
    - GitHub
    """)

# EJERCICIO 1
elif modulo == "Ejercicio 1":
    st.title("Ejercicio 1")
    st.markdown("Flujo de caja con listas")

# EJERCICIO 2
elif modulo == "Ejercicio 2":
    st.title("Ejercicio 2")
    st.markdown("Registro con NumPy y DataFrame")

# EJERCICIO 3
elif modulo == "Ejercicio 3":
    st.title("Ejercicio 3")
    st.markdown("Uso de funciones desde librería externa")

# EJERCICIO 4
elif modulo == "Ejercicio 4":
    st.title("Ejercicio 4")
    st.markdown("Uso de clases y CRUD")
