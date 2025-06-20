# Código Principal (Resumen)
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

agenda = []  # Vector de registros

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    nuevo = Contacto(nombre, telefono, email)
    agenda.append(nuevo)