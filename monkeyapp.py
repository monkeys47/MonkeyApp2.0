import streamlit as st

# Simulación de la función que valida correos electrónicos
def validar_correos(correos):
    resultados = {}
    for correo in correos:
        if "@" in correo and "." in correo.split("@")[-1]:
            resultados[correo] = "Válido"
        else:
            resultados[correo] = "Inválido"
    return resultados

# Configuración de la página de la aplicación
st.set_page_config(page_title="Gestión de Correos", layout="centered")

# Título principal
st.title("Gestión de Correos")
st.write("Aquí puedes gestionar y probar correos funcionales.")

# Entrada de correos electrónicos
st.text_area(
    "Escribe los correos a probar (uno por línea):",
    placeholder="correo1@example.com\ncorreo2@example.com",
    key="correos_input",
)

# Botón para probar correos
if st.button("Probar correos"):
    # Obtener los correos ingresados
    correos_texto = st.session_state.correos_input
    correos_lista = correos_texto.split("\n")

    # Validar los correos
    resultados = validar_correos(correos_lista)

    # Mostrar los resultados en la interfaz
    st.write("### Resultados:")
    for correo, estado in resultados.items():
        st.write(f"- *{correo}*: {estado}")

# Nota al final
st.write("---")
st.write("App desarrollada por MonkeyCorreosCheck.")