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

# Interfaz principal
def interfaz_principal():
    st.title("Gestión de Correos")
    st.write("Aquí puedes gestionar y probar correos funcionales.")
    
    correos = st.text_area("Escribe los correos a probar (uno por línea):")
    lista_correos = correos.split("\n")
    
    # Contador de correos ingresados
    st.write(f"Cantidad de correos ingresados: {len([correo for correo in lista_correos if correo.strip()])}")
    
    if st.button("Probar correos"):
        resultados = {}
        for correo in lista_correos:
            if "@" in correo and "." in correo:  # Validación básica
                resultados[correo] = "Válido"
            else:
                resultados[correo] = "Inválido"
        
        st.subheader("Resultados:")
        for correo, estado in resultados.items():
            st.write(f"- {correo}: {estado}")

# Lógica de la aplicación
if st.session_state["usuario_activo"]:
    st.sidebar.write(f"Bienvenido, {st.session_state['usuario_activo']}!")
    if st.sidebar.button("Cerrar sesión"):
        cerrar_sesion()
        st.experimental_rerun()
    interfaz_principal()
else:
    st.title("Inicio de Sesión")
    usuario = st.text_input("Nombre de usuario")
    contrasena = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if iniciar_sesion(usuario, contrasena):
            st.success("¡Inicio de sesión exitoso!")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos")