import json

ARCHIVO = "data/proveedores.json"


def cargar_proveedores():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_proveedores(proveedores):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(proveedores, archivo, indent=4, ensure_ascii=False)


def agregar_proveedor():
    proveedores = cargar_proveedores()

    nombre = input("Nombre del proveedor: ")
    contacto = input("Contacto: ")
    direccion = input("Dirección: ")

    nuevo_proveedor = {
        "nombre": nombre,
        "contacto": contacto,
        "direccion": direccion
    }

    proveedores.append(nuevo_proveedor)
    guardar_proveedores(proveedores)

    print("Proveedor agregado correctamente.")


def listar_proveedores():
    proveedores = cargar_proveedores()

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    print("\n===== LISTA DE PROVEEDORES =====")

    for i, proveedor in enumerate(proveedores, start=1):
        print(f"\nProveedor #{i}")
        print(f"Nombre: {proveedor['nombre']}")
        print(f"Contacto: {proveedor['contacto']}")
        print(f"Dirección: {proveedor['direccion']}")


def buscar_proveedor():
    nombre_buscar = input("Ingrese el nombre del proveedor: ").lower()

    proveedores = cargar_proveedores()

    for proveedor in proveedores:
        if proveedor["nombre"].lower() == nombre_buscar:
            print("\nProveedor encontrado:")
            print(f"Nombre: {proveedor['nombre']}")
            print(f"Contacto: {proveedor['contacto']}")
            print(f"Dirección: {proveedor['direccion']}")
            return

    print("Proveedor no encontrado.")


def actualizar_proveedor():
    nombre_buscar = input("Proveedor a actualizar: ").lower()

    proveedores = cargar_proveedores()

    for proveedor in proveedores:
        if proveedor["nombre"].lower() == nombre_buscar:

            print("\nDatos actuales:")
            print(proveedor)

            proveedor["contacto"] = input("Nuevo contacto: ")
            proveedor["direccion"] = input("Nueva dirección: ")

            guardar_proveedores(proveedores)

            print("Proveedor actualizado.")
            return

    print("Proveedor no encontrado.")


def eliminar_proveedor():
    nombre_buscar = input("Proveedor a eliminar: ").lower()

    proveedores = cargar_proveedores()

    for proveedor in proveedores:
        if proveedor["nombre"].lower() == nombre_buscar:

            proveedores.remove(proveedor)

            guardar_proveedores(proveedores)

            print("Proveedor eliminado.")
            return

    print("Proveedor no encontrado.")


def menu_proveedores():

    while True:

        print("\n===== MENÚ PROVEEDORES =====")
        print("1. Agregar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedor")
        print("4. Actualizar proveedor")
        print("5. Eliminar proveedor")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_proveedor()

        elif opcion == "2":
            listar_proveedores()

        elif opcion == "3":
            buscar_proveedor()

        elif opcion == "4":
            actualizar_proveedor()

        elif opcion == "5":
            eliminar_proveedor()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")