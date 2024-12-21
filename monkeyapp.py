import streamlit as st
import json

# Cargar datos de usuarios desde un archivo JSON
try:
    with open("usuarios.json", "r") as archivo:
        usuarios = json.load(archivo)
except FileNotFoundError:
    usuarios = {
        "admin": {"contraseña": "admin123", "tipo": "permanente"}
    }
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)

# Variables de sesión
if "usuario_activo" not in st.session_state:
    st.session_state["usuario_activo"] = None

# Función para manejar el inicio de sesión
def iniciar_sesion(usuario, contraseña):
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        st.session_state["usuario_activo"] = usuario
        return True
    return False

# Función para cerrar sesión
def cerrar_sesion():
    st.session_state["usuario_activo"] = None

# Función para agregar un nuevo usuario
def agregar_usuario(usuario, contraseña, tipo):
    if usuario in usuarios:
        return "El usuario ya existe."
    usuarios[usuario] = {"contraseña": contraseña, "tipo": tipo}
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)
    return "Usuario agregado exitosamente."

# Menú de la aplicación
if st.session_state["usuario_activo"] is None:
    # Pantalla de inicio de sesión
    st.title("Inicio de sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        if iniciar_sesion(usuario, contraseña):
            st.success("¡Inicio de sesión exitoso!")
            st.session_state["usuario_activo"] = usuario
        else:
            st.error("Usuario o contraseña incorrectos")
else:
    # Pantalla de gestión para usuarios autenticados
    st.sidebar.title("Menú")
    st.sidebar.write(f"Bienvenido, {st.session_state['usuario_activo']}!")
    if st.sidebar.button("Cerrar sesión"):
        cerrar_sesion()

    # Funcionalidad de gestión de correos (accesible para todos los usuarios)
    st.title("Gestión de correos")
    st.write("Aquí puedes gestionar y probar correos funcionales.")
    correos = st.text_area("Escribe los correos a probar (uno por línea):")
    if st.button("Probar correos"):
        st.write("Procesando correos...")
        # Aquí puedes agregar lógica para verificar los correos

    # Agregar usuarios (solo visible para administradores)
    if st.session_state["usuario_activo"] == "admin":
        st.subheader("Agregar nuevo usuario")
        nuevo_usuario = st.text_input("Nuevo usuario")
        nueva_contraseña = st.text_input("Contraseña del nuevo usuario", type="password")
        tipo_usuario = st.selectbox("Tipo de usuario", ["permanente", "temporal"])
        if st.button("Agregar usuario"):
            mensaje = agregar_usuario(nuevo_usuario, nueva_contraseña, tipo_usuario)
            st.success(mensaje)