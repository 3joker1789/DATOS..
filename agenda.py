class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

agenda = []  # Vector de registros (estructura de datos)

def agregar_contacto():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    nuevo = Contacto(nombre, telefono, email)
    agenda.append(nuevo)
    print(f"✅ Contacto '{nombre}' agregado!")

def buscar_contacto():
    nombre = input("Buscar contacto: ")
    for contacto in agenda:
        if contacto.nombre.lower() == nombre.lower():
            print(f"📞 {contacto.nombre}: {contacto.telefono} | ✉️ {contacto.email}")
            return
    print("❌ Contacto no encontrado")

def mostrar_todos():
    print("\n--- AGENDA COMPLETA ---")
    for i, contacto in enumerate(agenda, 1):
        print(f"{i}. {contacto.nombre} | {contacto.telefono} | {contacto.email}")

def menu():
    while True:
        print("\n*** AGENDA TELEFÓNICA ***")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos")
        print("4. Salir")
        opcion = input("Seleccione: ")
        
        if opcion == "1": agregar_contacto()
        elif opcion == "2": buscar_contacto()
        elif opcion == "3": mostrar_todos()
        elif opcion == "4": break
        else: print("⚠️ Opción inválida")

if __name__ == "__main__":
    menu()