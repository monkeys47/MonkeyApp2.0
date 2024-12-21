import streamlit as st

# Simulación de base de datos
usuarios = {
    "monke@47": "07052004er"
}

# Variables de sesión
if "usuario_activo" not in st.session_state:
    st.session_state["usuario_activo"] = None

# Función para manejar el inicio de sesión
def iniciar_sesion(usuario, contrasena):
    if usuario in usuarios and usuarios[usuario] == contrasena:
        st.session_state["usuario_activo"] = usuario
        return True
    return False

# Función para cerrar sesión
def cerrar_sesion():
    st.session_state["usuario_activo"] = None
    st.session_state["trigger_rerun"] = True  # Activar recarga

# Manejo de recarga de la aplicación
if "trigger_rerun" in st.session_state and st.session_state["trigger_rerun"]:
    st.session_state["trigger_rerun"] = False
    st.experimental_rerun()

# Interfaz principal
if st.session_state["usuario_activo"]:
    st.success(f"¡Bienvenido {st.session_state['usuario_activo']}!")
    if st.session_state["usuario_activo"] == "monke@47":
        # Menú exclusivo para administrador
        with st.sidebar:
            st.header("Menú de Administrador")
            opcion = st.selectbox("Seleccione una opción:", ["Gestión de Correos", "Gestión de Usuarios"])
        
        if opcion == "Gestión de Usuarios":
            st.header("Gestión de Usuarios")
            nuevo_usuario = st.text_input("Nuevo usuario (correo):")
            nueva_contrasena = st.text_input("Nueva contraseña:", type="password")

            if st.button("Agregar usuario"):
                if nuevo_usuario and nueva_contrasena:
                    usuarios[nuevo_usuario] = nueva_contrasena
                    st.success(f"Usuario {nuevo_usuario} agregado correctamente.")
                else:
                    st.error("Por favor, complete ambos campos.")

    # Página principal: Gestión de correos
    if opcion == "Gestión de Correos" or st.session_state["usuario_activo"] != "monke@47":
        st.header("Gestión de Correos")
        st.write("Aquí puedes gestionar y probar correos funcionales.")

        correos = st.text_area("Escribe los correos a probar (uno por línea):")
        correos_lista = correos.split("\n") if correos else []

        st.write(f"Cantidad de correos ingresados: {len(correos_lista)}")

        if st.button("Probar correos"):
            resultados = []
            cantidad_validos = 0

            for correo in correos_lista:
                if "@" in correo:  # Simulación de validación básica
                    resultados.append((correo, "Válido"))
                    cantidad_validos += 1
                else:
                    resultados.append((correo, "Inválido"))

            st.subheader("Resultados:")
            for correo, estado in resultados:
                st.write(f"- {correo}: {estado}")

            st.write(f"Cantidad de correos válidos: {cantidad_validos}")

else:
    st.header("Inicio de Sesión")

    usuario = st.text_input("Nombre de usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if iniciar_sesion(usuario, contrasena):
            st.success("¡Inicio de sesión exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos")