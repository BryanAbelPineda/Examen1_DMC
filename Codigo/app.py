import streamlit as st

st.image("Logos/Python_Logo.png", width = 100)
st.title("Trabajo Práctico - Modulo Python Fundamentals")
st.sidebar.title("Menú")
st.write("Elaborado por: Bryan Abel Pineda Sulca")
st.sidebar.image("Logos/DMC_logo.png",width = 200)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

