import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.image("Logos/Python_Logo.png", width = 100)
st.title("Especialización en Python  for Analytics ")
st.sidebar.title("Menú")
st.write("Proyecto Academico")
st.sidebar.image("Logos/DMC_logo.png",width = 200)
modulos = st.sidebar.selectbox ("Secciones", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])
#################################################################################    1 HOME   #################################################################################   
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
    #################################################################################    EJERCICIO 1   #################################################################################   
elif modulos == "Ejercicio 1":
      st.write("1. FLUJO DE CAJA CON LISTAS")
    

      if "list_conceptos" not in st.session_state:
        st.session_state.list_conceptos = []

      if "list_tipos" not in st.session_state:
        st.session_state.list_tipos = []
        
      if "list_valores" not in st.session_state:
            st.session_state.list_valores = []

    
      concepto = st.text_input("Ingrese Concepto:")
      tipo = st.selectbox("Tipo de Movimiento",["Ingreso","Gasto"])
      valor=st.number_input("Ingrese Valor (s/)")

      if st.button("Agregar"):
            
        st.session_state.list_conceptos.append(concepto)
        st.session_state.list_tipos.append(tipo)
        st.session_state.list_valores.append(valor)
    
      Movimientos= pd.DataFrame({
        "Concepto":st.session_state.list_conceptos
        ,"Tipo":st.session_state.list_tipos
        ,"Valor":st.session_state.list_valores
      }) 
      st.dataframe(Movimientos)
      ingresos=Movimientos[Movimientos["Tipo"]=="Ingreso"]["Valor"].sum()
      gasto   =Movimientos[Movimientos["Tipo"]=="Gasto"]["Valor"].sum()
      saldo   =ingresos-gasto
    
        
      st.write("Ingresos: ",ingresos)
      st.write("Gastos: ",gasto)
      st.write("Saldo: ",saldo)
      
      if saldo > 0 : 
          st.write("Caja a favor") 
      else: 
          st.write("Caja en contra") 
#################################################################################    EJERCICIO 2   #################################################################################          
elif modulos == "Ejercicio 2":
      st.write("2. REGISTRO CON NUMPY, ARRAYS Y DATAFRAME. ")
      st.header("Piloto Registro de Productos")

      if "list_prod" not in st.session_state:
          st.session_state.list_prod=np.array([]) 
      if "list_cat" not in st.session_state:
          st.session_state.list_cat=np.array([])
      if "list_can" not in st.session_state:
          st.session_state.list_can=np.array([])
      if "list_pre" not in st.session_state:
         st.session_state.list_pre=np.array([])
      if "list_tot" not in st.session_state:
          st.session_state.list_tot=np.array([])
          
      producto=st.text_input("Producto: ")
      categoria=st.selectbox("Categoria de Producto:",["Abarrotes","Bebidas","Limpieza","Electronica","Otros"])
      precio=st.number_input("Precio Unitario (S/.)")
      cantidad=st.number_input("Cantidad")

      if st.button("Añadir Registro"):

          st.session_state.list_prod=np.append(st.session_state.list_prod,producto)
          st.session_state.list_cat=np.append(st.session_state.list_cat,categoria)
          st.session_state.list_can=np.append(st.session_state.list_can,cantidad)
          st.session_state.list_pre=np.append(st.session_state.list_pre,precio)
          st.session_state.list_tot=np.append(st.session_state.list_tot,precio*cantidad)
     
      if st.button("Limpiar Registros"):
          st.session_state.list_prod=np.array([])
          st.session_state.list_can=np.array([])
          st.session_state.list_cat=np.array([])
          st.session_state.list_pre=np.array([])
          st.session_state.list_tot=np.array([])
  
      Consolidado= pd.DataFrame({
        "Producto":st.session_state.list_prod
        ,"Categoria":st.session_state.list_cat
        ,"Cantidad":st.session_state.list_can
        ,"Precio":st.session_state.list_pre
        ,"Total":st.session_state.list_tot
      })
    
      st.dataframe(Consolidado)
#################################################################################    EJERCICIO 3   #################################################################################  
elif modulos == "Ejercicio 3":
     
      st.write("3. CALCULADORA DE PRODUCTIVDAD LABORAL")
      ## DEFINICIO DE PRIMERA FUNCION
      def validar_positivo(valor: float, nombre: str, permitir_cero: bool = False) -> None:
        if permitir_cero:
            if valor < 0:
                raise ValueError(f"{nombre} no puede ser negativo.")
        else:
            if valor <= 0:
                raise ValueError(f"{nombre} debe ser mayor que cero.")
   ############################################################################   

      up=st.number_input("Unidades Producidas:")
      ht=st.number_input("Horas Trabajadas: ")
      nt=st.number_input("Numero de Trabajadores: ")
     ## DEFINICIO DE SEGUNDA FUNCION
      def calcular_productividad_laboral(unidades_producidas: float, horas_trabajadas: float, numero_trabajadores: int) -> dict:
            """
            Calcula productividad por hora y por trabajador.
            """
            validar_positivo(unidades_producidas, "unidades_producidas")
            validar_positivo(horas_trabajadas, "horas_trabajadas")
            validar_positivo(numero_trabajadores, "numero_trabajadores")
    
            productividad_hora = unidades_producidas / horas_trabajadas
            productividad_trabajador = unidades_producidas / numero_trabajadores
    
            return {
            "productividad_por_hora": round(productividad_hora, 2),
            "productividad_por_trabajador": round(productividad_trabajador, 2)
             }
#################################################################################

      if st.button("Calcular Productividad"):
           calcular_productividad_laboral(up,ht,nt)
      
      ahora=datetime.now()
      st.metric(label="Productividad por hora",value=productividad_hora)
      st.metric(label="Productividad por Trabajador",value=productividad_trabajador)
      st.write("Hora Actual",ahora)

else:

  

  st.write("No hay nada")

