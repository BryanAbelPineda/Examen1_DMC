import streamlit as st

st.image("Logos/Python_Logo.png", width = 100)
st.title("Trabajo Práctico - Modulo Python Fundamentals")
st.sidebar.title("Menú")
st.write("Elaborado por: Bryan Abel Pineda Sulca")
st.sidebar.image("Logos/DMC_logo.png",width = 200)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":


    st.markdown("---")

    st.markdown("### Información General")
    st.write("""
    Esta aplicación corresponde al trabajo práctico del módulo
    Python Fundamentals. Aquí se desarrollan los ejercicios
    solicitados utilizando Streamlit como herramienta de visualización.
    """)

    st.markdown("### Descripción del Proyecto")
    st.write("""
    El proyecto integra distintos ejercicios relacionados con
    programación en Python, manejo de datos y desarrollo de
    aplicaciones interactivas.
    """)

    st.markdown("### Tecnologías Utilizadas")
    st.markdown("""
    - Python
    - Streamlit
    - NumPy
    - Pandas
    - GitHub
    """)

