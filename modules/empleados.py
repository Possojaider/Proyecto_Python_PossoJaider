import json

ARCHIVO = "data/empleados.json"


def cargar_empleados():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_empleados(empleados):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(empleados, archivo, indent=4, ensure_ascii=False)


def agregar_empleado():
    empleados = cargar_empleados()

    nombre = input("Nombre del empleado: ")
    cargo = input("Cargo: ")
    fecha_contratacion = input("Fecha de contratación (AAAA-MM-DD): ")

    nuevo_empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "fechaContratacion": fecha_contratacion
    }

    empleados.append(nuevo_empleado)
    guardar_empleados(empleados)

    print("Empleado agregado correctamente.")


def listar_empleados():
    empleados = cargar_empleados()

    if not empleados:
        print("No hay empleados registrados.")
        return

    print("\n===== LISTA DE EMPLEADOS =====")

    for i, empleado in enumerate(empleados, start=1):
        print(f"\nEmpleado #{i}")
        print(f"Nombre: {empleado['nombre']}")
        print(f"Cargo: {empleado['cargo']}")
        print(f"Fecha de contratación: {empleado['fechaContratacion']}")


def buscar_empleado():
    nombre_buscar = input("Ingrese el nombre del empleado: ").lower()

    empleados = cargar_empleados()

    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_buscar:

            print("\nEmpleado encontrado:")
            print(f"Nombre: {empleado['nombre']}")
            print(f"Cargo: {empleado['cargo']}")
            print(f"Fecha de contratación: {empleado['fechaContratacion']}")
            return

    print("Empleado no encontrado.")


def actualizar_empleado():
    nombre_buscar = input("Nombre del empleado a actualizar: ").lower()

    empleados = cargar_empleados()

    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_buscar:

            print("\nDatos actuales:")
            print(empleado)

            empleado["cargo"] = input("Nuevo cargo: ")
            empleado["fechaContratacion"] = input(
                "Nueva fecha de contratación (AAAA-MM-DD): "
            )

            guardar_empleados(empleados)

            print("Empleado actualizado correctamente.")
            return

    print("Empleado no encontrado.")


def eliminar_empleado():
    nombre_buscar = input("Nombre del empleado a eliminar: ").lower()

    empleados = cargar_empleados()

    for empleado in empleados:
        if empleado["nombre"].lower() == nombre_buscar:

            empleados.remove(empleado)

            guardar_empleados(empleados)

            print("Empleado eliminado correctamente.")
            return

    print("Empleado no encontrado.")


def menu_empleados():

    while True:

        print("\n===== MENÚ EMPLEADOS =====")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Actualizar empleado")
        print("5. Eliminar empleado")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_empleado()

        elif opcion == "2":
            listar_empleados()

        elif opcion == "3":
            buscar_empleado()

        elif opcion == "4":
            actualizar_empleado()

        elif opcion == "5":
            eliminar_empleado()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")