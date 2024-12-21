import streamlit as st

def verificar_correos(correos):
    resultados = {}
    for correo in correos:
        # Simulación de verificación: considera todos como válidos
        resultados[correo] = "Válido"
    return resultados

# Configuración de la página
st.set_page_config(page_title="Gestión de Correos", layout="centered")

# Título de la aplicación
st.title("Gestión de Correos")
st.write("Aquí puedes gestionar y probar correos funcionales.")

# Entrada de correos
st.subheader("Escribe los correos a probar (uno por línea):")
correos_input = st.text_area("Escribe los correos aquí:", height=200)
correos_lista = [correo.strip() for correo in correos_input.split("\n") if correo.strip()]

# Mostrar la cantidad de correos ingresados
st.write(f"*Cantidad de correos ingresados:* {len(correos_lista)}")

# Botón para probar los correos
if st.button("Probar correos"):
    if correos_lista:
        with st.spinner("Probando correos..."):
            resultados = verificar_correos(correos_lista)

        # Mostrar los resultados
        st.subheader("Resultados:")
        for correo, estado in resultados.items():
            st.write(f"- {correo}: *{estado}*")

        # Mostrar la cantidad de correos válidos
        validos = sum(1 for estado in resultados.values() if estado == "Válido")
        st.write(f"*Cantidad de correos válidos:* {validos}")
    else:
        st.warning("Por favor, ingresa al menos un correo.")