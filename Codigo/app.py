import streamlit as st
import pandas as pd

st.image("Logos/Python_Logo.png", width = 100)
st.title("Especialización en Python  for Analytics ")
st.sidebar.title("Menú")
st.write("Proyecto Academico")
st.sidebar.image("Logos/DMC_logo.png",width = 200)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulos == "Home":


    st.markdown("---")

    st.header("Módulo 1 – Fundamentos de Programación")
    
    st.image("Logos/Logo_Log.png", width = 200)
    
    st.markdown("### Elaborado por: Bryan Abel Pineda Sulca")
    st.write("""
    Egresado de la Carrera de Psicología organizacional con experiencia en análisis de datos
    """)
    st.subheader("2026")
    st.write("""
    Desarrollo de una aplicación interactiva para analizar y visualizar información utilizando Python y Streamlit.
    """)
    st.markdown("### Tecnologías Utilizadas")
    st.markdown("""
    - Python
    - Streamlit
    - NumPy
    - Pandas
    - GitHub
    """)
elif modulos == "Ejercicio 1":
  st.write("1. FLUJO DE CAJA CON LISTAS")
  concepto = st.text_input("Ingrese Concepto:")
  tipo = st.selectbox("Tipo de Movimiento",["Ingreso","Gasto"])
  valor=st.number_input("Ingrese Valor (s/)")

  Movimientos= pd.DataFrame({
    "Concepto":["Lapiz","Papel"]
    ,"Tipo":["Ingreso","Ingreso"]
    ,"Valor":[20,30]
  }) 
  st.dataframe(Movimientos)
  ingresos=Movimientos[Movimientos["Tipo"]=="Ingreso"]["Valor"].sum()
  gasto   =Movimientos[Movimientos["Tipo"]=="Gasto"]["Valor"].sum()
  saldo   =ingresos-gasto
  st.write("Ingresos: ",ingresos)
  st.write("Gastos: ",gasto)
  st.write("Saldo: ",saldo)

else:

  

  st.write("No hay nada")

