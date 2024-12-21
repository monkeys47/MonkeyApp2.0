import streamlit as st

# Simulación de base de datos
usuarios = {
    "admin": "admin123"
}

# Variables de sesión
if "usuario_activo" not in st.session_state:
    st.session_state["usuario_activo"] = None

# Función para manejar el inicio de sesión
def iniciar_sesion(usuario, contraseña):
    if usuario in usuarios and usuarios[usuario] == contraseña:
        st.session_state["usuario_activo"] = usuario
        return True
    return False

# Función para cerrar sesión
def cerrar_sesion():
    st.session_state["usuario_activo"] = None

# Función para agregar un nuevo usuario
def agregar_usuario(usuario, contraseña):
    if usuario in usuarios:
        return "El usuario ya existe."
    usuarios[usuario] = contraseña
    return "Usuario agregado exitosamente."

# Botón temporal para limpiar sesión (solo para depuración)
if st.sidebar.button("Limpiar sesión"):
    st.session_state.clear()
    st.success("Sesión limpiada, recarga la página e intenta nuevamente.")

# Menú de la aplicación
if st.session_state["usuario_activo"] is None:
    # Pantalla de inicio de sesión
    st.title("Inicio de sesión")
    usuario = st.text_input("Usuario")
    contraseña = st.text_input("Contraseña", type="password")
    
    # Prueba de impresión para depuración (temporal)
    st.write(f"Usuario ingresado: {usuario}")
    st.write(f"Contraseña ingresada: {contraseña}")
    st.write(f"Credenciales almacenadas: {usuarios}")
    
    if st.button("Iniciar sesión"):
        if iniciar_sesion(usuario, contraseña):
            st.success("¡Inicio de sesión exitoso!")
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
        if st.button("Agregar usuario"):
            mensaje = agregar_usuario(nuevo_usuario, nueva_contraseña)
            st.success(mensaje)