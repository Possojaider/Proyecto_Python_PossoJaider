import json

ARCHIVO = "data/pacientes.json"


def cargar_pacientes():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_pacientes(pacientes):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(pacientes, archivo, indent=4, ensure_ascii=False)


def agregar_paciente():
    pacientes = cargar_pacientes()

    nombre = input("Nombre del paciente: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")

    nuevo_paciente = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono
    }

    pacientes.append(nuevo_paciente)
    guardar_pacientes(pacientes)

    print("Paciente agregado correctamente.")


def listar_pacientes():
    pacientes = cargar_pacientes()

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    print("\n===== LISTA DE PACIENTES =====")

    for i, paciente in enumerate(pacientes, start=1):
        print(f"\nPaciente #{i}")
        print(f"Nombre: {paciente['nombre']}")
        print(f"Dirección: {paciente['direccion']}")
        print(f"Teléfono: {paciente['telefono']}")


def buscar_paciente():
    nombre_buscar = input("Ingrese el nombre del paciente: ").lower()

    pacientes = cargar_pacientes()

    for paciente in pacientes:
        if paciente["nombre"].lower() == nombre_buscar:
            print("\nPaciente encontrado:")
            print(f"Nombre: {paciente['nombre']}")
            print(f"Dirección: {paciente['direccion']}")
            print(f"Teléfono: {paciente['telefono']}")
            return

    print("Paciente no encontrado.")


def actualizar_paciente():
    nombre_buscar = input("Paciente a actualizar: ").lower()

    pacientes = cargar_pacientes()

    for paciente in pacientes:
        if paciente["nombre"].lower() == nombre_buscar:

            print("\nDatos actuales:")
            print(paciente)

            paciente["direccion"] = input("Nueva dirección: ")
            paciente["telefono"] = input("Nuevo teléfono: ")

            guardar_pacientes(pacientes)

            print("Paciente actualizado correctamente.")
            return

    print(" Paciente no encontrado.")


def eliminar_paciente():
    nombre_buscar = input("Paciente a eliminar: ").lower()

    pacientes = cargar_pacientes()

    for paciente in pacientes:
        if paciente["nombre"].lower() == nombre_buscar:

            pacientes.remove(paciente)

            guardar_pacientes(pacientes)

            print("Paciente eliminado correctamente.")
            return

    print("Paciente no encontrado.")


def menu_pacientes():

    while True:

        print("\n===== MENÚ PACIENTES =====")
        print("1. Agregar paciente")
        print("2. Listar pacientes")
        print("3. Buscar paciente")
        print("4. Actualizar paciente")
        print("5. Eliminar paciente")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_paciente()

        elif opcion == "2":
            listar_pacientes()

        elif opcion == "3":
            buscar_paciente()

        elif opcion == "4":
            actualizar_paciente()

        elif opcion == "5":
            eliminar_paciente()

        elif opcion == "0":
            break

        else:
            print(" Opción inválida.")