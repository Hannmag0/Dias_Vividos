"""
Cálculo de días vividos utilizando lambda
Hannia Macias Gómez
30 de septiembre de 2026

La función lambda se utilizó para calcular los días vividos
de cada persona de manera breve, sin necesidad de definir
una función tradicional con def.
"""

import streamlit as st
from datetime import date

# CONFIGURACIÓN DE LA PÁGINA

st.set_page_config(
    page_title="Calculadora de días vividos",
    page_icon="📅",
    layout="wide"
)

# FUNCIÓN LAMBDA

# Calcula los días transcurridos entre una fecha y el día actual
calcular_dias = lambda fecha: (date.today() - fecha).days

# TÍTULO

st.title("📅 Calculadora de días vividos con Lambda")

st.write(
    "Ingresa una o varias fechas de nacimiento para calcular "
    "cuántos días han transcurrido hasta la fecha actual."
)

st.divider()

# ESTADO DE LA APLICACIÓN

if "cantidad_fechas" not in st.session_state:
    st.session_state.cantidad_fechas = 1

if "resultados" not in st.session_state:
    st.session_state.resultados = []

# BOTONES PARA AGREGAR O ELIMINAR FECHAS

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Agregar fecha", use_container_width=True):
        st.session_state.cantidad_fechas += 1

with col2:
    if st.button(
        "➖ Eliminar fecha",
        use_container_width=True,
        disabled=st.session_state.cantidad_fechas <= 1
    ):
        # Eliminar el último campo de fecha
        st.session_state.cantidad_fechas -= 1

        # Eliminar también el último resultado
        if st.session_state.resultados:
            st.session_state.resultados.pop()

# CAPTURA DE FECHAS

st.subheader("Fechas de nacimiento")

fechas = []

for i in range(st.session_state.cantidad_fechas):

    fecha = st.date_input(
        f"Persona {i + 1}",
        value=date(2000, 1, 1),
        max_value=date.today(),
        key=f"fecha_{i}"
    )

    fechas.append(fecha)

# CÁLCULO

if st.button(
    "🧮 Calcular días vividos",
    type="primary",
    use_container_width=True
):

    # Se aplica la función lambda a todas las fechas
    dias_vividos = list(map(calcular_dias, fechas))

    # Guardar resultados
    st.session_state.resultados = list(
        zip(fechas, dias_vividos)
    )

# MOSTRAR RESULTADOS

if st.session_state.resultados:

    st.divider()
    st.subheader("📋 Lista de personas")

    for numero, (fecha, dias) in enumerate(
        st.session_state.resultados,
        start=1
    ):

        with st.container(border=True):

            st.markdown(f"### 👤 Persona {numero}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Fecha de nacimiento",
                    fecha.strftime("%d/%m/%Y")
                )

            with col2:
                st.metric(
                    "Días vividos",
                    f"{dias:,}"
                )

    st.success("✅ Cálculo realizado correctamente.")