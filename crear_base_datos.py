import sqlite3

# Conectar o crear base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Crear tabla de usuarios
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

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos y tabla de usuarios creadas correctamente.")