import streamlit as st
from datetime import datetime, timedelta
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("usuarios.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tabla de usuarios si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    tipo_acceso TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL,
    activo INTEGER NOT NULL DEFAULT 1
)
''')
conn.commit()

# Función para validar credenciales
def validar_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ? AND activo = 1", (username, password))
    return cursor.fetchone()

# Función para registrar usuario
def registrar_usuario(username, password, tipo_acceso):
    fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO usuarios (username, password, tipo_acceso, fecha_creacion, activo) VALUES (?, ?, ?, ?, 1)",
                   (username, password, tipo_acceso, fecha_creacion))
    conn.commit()
    st.success("¡Usuario registrado correctamente!")

# Función para gestionar correos
def gestionar_correos():
    st.subheader("Gestión de Correos")
    st.write("Aquí puedes gestionar y probar correos funcionales.")
    # Aquí puedes agregar más funcionalidades específicas para correos
    st.text_area("Escribe los correos a probar:")
    if st.button("Probar correos"):
        st.success("Correos probados exitosamente (ejemplo).")

# Interfaz de inicio de sesión
st.title("Inicio de Sesión")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if not st.session_state.logged_in:
    username = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar sesión"):
        usuario = validar_usuario(username, password)
        if usuario:
            st.session_state.logged_in = True
            st.session_state.username = usuario[1]
            st.success(f"¡Inicio de sesión exitoso!\nBienvenido {usuario[1]}")
        else:
            st.error("Usuario o contraseña incorrectos.")
else:
    st.sidebar.title("Menú")
    if st.session_state.username == "monke@47":
        # Opciones exclusivas para el administrador
        opcion = st.sidebar.selectbox("Seleccione una opción", ["Inicio", "Registrar Usuario", "Gestionar Correos", "Cerrar sesión"])
        if opcion == "Inicio":
            st.subheader("Bienvenido a MonkeyApp")
            st.write("Esta es la vista principal del administrador.")
        elif opcion == "Registrar Usuario":
            st.subheader("Registrar Usuario")
            new_username = st.text_input("Nombre de usuario (nuevo)")
            new_password = st.text_input("Contraseña (nueva)", type="password")
            tipo_acceso = st.selectbox("Tipo de acceso", ["temporal", "permanente"])
            if st.button("Registrar"):
                registrar_usuario(new_username, new_password, tipo_acceso)
        elif opcion == "Gestionar Correos":
            gestionar_correos()
        elif opcion == "Cerrar sesión":
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.experimental_set_query_params()  # Para limpiar los parámetros de sesión
            st.stop()
    else:
        # Opciones para usuarios normales
        st.sidebar.selectbox("Seleccione una opción", ["Gestionar Correos", "Cerrar sesión"])
        st.subheader("Gestión de Correos")
        gestionar_correos()

# Cerrar conexión con la base de datos
conn.close()