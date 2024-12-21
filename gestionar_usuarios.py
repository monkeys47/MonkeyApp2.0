import sqlite3
from datetime import datetime, timedelta

# Conectar a la base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Función para agregar un usuario
def agregar_usuario(username, password, tipo_acceso):
    fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if tipo_acceso == "temporal":
        # Si el usuario es temporal, caducará en una semana
        fecha_caducidad = datetime.now() + timedelta(days=7)
        print(f"El usuario temporal expirará el {fecha_caducidad}")
    else:
        print("El usuario es permanente y no caduca.")
    cursor.execute("""
        INSERT INTO usuarios (username, password, tipo_acceso, fecha_creacion, activo)
        VALUES (?, ?, ?, ?, 1)
    """, (username, password, tipo_acceso, fecha_creacion))
    conn.commit()
    print("Usuario agregado correctamente.")

# Función para listar todos los usuarios
def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(usuario)

# Función para actualizar el estado del usuario
def cambiar_estado_usuario(username, activo):
    cursor.execute("UPDATE usuarios SET activo = ? WHERE username = ?", (activo, username))
    conn.commit()
    estado = "activado" if activo == 1 else "desactivado"
    print(f"El usuario '{username}' ha sido {estado}.")

# Función para eliminar un usuario
def eliminar_usuario(username):
    cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
    conn.commit()
    print(f"El usuario '{username}' ha sido eliminado.")

# Ejemplos de uso
if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Cambiar estado de usuario (activar/desactivar)")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            username = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            tipo_acceso = input("Tipo de acceso (temporal/permanente): ").lower()
            agregar_usuario(username, password, tipo_acceso)
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            username = input("Nombre de usuario: ")
            estado = int(input("Estado (1 para activar, 0 para desactivar): "))
            cambiar_estado_usuario(username, estado)
        elif opcion == "4":
            username = input("Nombre de usuario: ")
            eliminar_usuario(username)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Programa iniciado correctamente...")