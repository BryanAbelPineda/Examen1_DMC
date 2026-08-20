import streamlit as st

st.image("Logos/Python_Logo.png", width = 100)
st.title("Especialización en Python  for Analytics ")
st.sidebar.title("Menú")
st.write("Proyecto Academica")
st.sidebar.image("Logos/DMC_logo.png",width = 200)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":


    st.markdown("---")

    st.header("Módulo 1 – Fundamentos de Programación")
    st.image("Logos/Logo_Log.png", width = 100)

    st.markdown("### Elaborado por: Bryan Abel Pineda Sulca")
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

