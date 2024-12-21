import streamlit as st
import json
import os

# Archivo para guardar usuarios permanentes
ARCHIVO_USUARIOS = "usuarios.json"

# Cargar usuarios desde el archivo, si existe
if os.path.exists(ARCHIVO_USUARIOS):
    with open(ARCHIVO_USUARIOS, "r") as file:
        usuarios_permanentes = json.load(file)
else:
    usuarios_permanentes = {}

# Usuarios temporales (estos no se guardan en disco)
usuarios_temporales = {}

# Unir usuarios permanentes y temporales
def obtener_usuarios():
    return {**usuarios_permanentes, **usuarios_temporales}

# Variables de sesión
if "usuario_activo" not in st.session_state:
    st.session_state["usuario_activo"] = None

# Función para manejar el inicio de sesión
def iniciar_sesion(usuario, contraseña):
    usuarios = obtener_usuarios()
    if usuario in usuarios and usuarios[usuario] == contraseña:
        st.session_state["usuario_activo"] = usuario
        return True
    return False

# Función para cerrar sesión
def cerrar_sesion():
    st.session_state["usuario_activo"] = None

# Función para agregar un nuevo usuario
def agregar_usuario(usuario, contraseña, permanente=False):
    if usuario in obtener_usuarios():
        return "El usuario ya existe."
    if permanente:
        usuarios_permanentes[usuario] = contraseña
        with open(ARCHIVO_USUARIOS, "w") as file:
            json.dump(usuarios_permanentes, file)
    else:
        usuarios_temporales[usuario] = contraseña
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

    # Funcionalidad de gestión de correos
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
        permanente = st.checkbox("¿Hacer el usuario permanente?")
        if st.button("Agregar usuario"):
            mensaje = agregar_usuario(nuevo_usuario, nueva_contraseña, permanente)
            st.success(mensaje)