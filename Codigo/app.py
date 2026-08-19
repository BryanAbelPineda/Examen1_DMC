import streamlit as st

st.title("Trabajo Práctico - Modulo Python Fundamentals")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Bryan Abel Pineda Sulca")
st.image("Logos/Python_Logo.png", width = 100)
st.sidebar.image("Logos/DMC_logo.png",width = 100)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

