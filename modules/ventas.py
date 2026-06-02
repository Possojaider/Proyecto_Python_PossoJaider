import json
from datetime import datetime

ARCHIVO_VENTAS = "data/ventas.json"
ARCHIVO_MEDICAMENTOS = "data/medicamentos.json"
ARCHIVO_PACIENTES = "data/pacientes.json"
ARCHIVO_EMPLEADOS = "data/empleados.json"


def cargar_json(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_json(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def registrar_venta():

    ventas = cargar_json(ARCHIVO_VENTAS)
    medicamentos = cargar_json(ARCHIVO_MEDICAMENTOS)
    pacientes = cargar_json(ARCHIVO_PACIENTES)
    empleados = cargar_json(ARCHIVO_EMPLEADOS)

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    if not empleados:
        print("No hay empleados registrados.")
        return

    if not medicamentos:
        print("No hay medicamentos registrados.")
        return

    print("\n===== PACIENTES =====")
    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p['nombre']}")

    pos_paciente = int(input("Seleccione paciente: ")) - 1
    paciente = pacientes[pos_paciente]

    print("\n===== EMPLEADOS =====")
    for i, e in enumerate(empleados, start=1):
        print(f"{i}. {e['nombre']} - {e['cargo']}")

    pos_empleado = int(input("Seleccione empleado: ")) - 1
    empleado = empleados[pos_empleado]

    medicamentos_vendidos = []

    while True:

        print("\n===== MEDICAMENTOS =====")

        for i, m in enumerate(medicamentos, start=1):
            print(
                f"{i}. {m['nombre']} | "
                f"Precio: ${m['precio']} | "
                f"Stock: {m['stock']}"
            )

        pos_medicamento = int(input("Seleccione medicamento: ")) - 1

        medicamento = medicamentos[pos_medicamento]

        cantidad = int(input("Cantidad: "))

        if cantidad > medicamento["stock"]:
            print("Stock insuficiente.")
            continue

        medicamento["stock"] -= cantidad

        medicamentos_vendidos.append({
            "nombreMedicamento": medicamento["nombre"],
            "cantidadVendida": cantidad,
            "precio": medicamento["precio"]
        })

        continuar = input(
            "¿Agregar otro medicamento? (s/n): "
        ).lower()

        if continuar != "s":
            break

    venta = {
        "fechaVenta": datetime.now().strftime("%Y-%m-%d"),
        "paciente": paciente,
        "empleado": empleado,
        "medicamentosVendidos": medicamentos_vendidos
    }

    ventas.append(venta)

    guardar_json(ARCHIVO_VENTAS, ventas)
    guardar_json(ARCHIVO_MEDICAMENTOS, medicamentos)

    print("✅ Venta registrada correctamente.")


def listar_ventas():

    ventas = cargar_json(ARCHIVO_VENTAS)

    if not ventas:
        print("No hay ventas registradas.")
        return

    print("\n===== VENTAS =====")

    for i, venta in enumerate(ventas, start=1):

        print(f"\nVENTA #{i}")
        print("Fecha:", venta["fechaVenta"])
        print("Paciente:", venta["paciente"]["nombre"])
        print("Empleado:", venta["empleado"]["nombre"])

        print("Medicamentos:")

        for med in venta["medicamentosVendidos"]:
            print(
                f"- {med['nombreMedicamento']} "
                f"x {med['cantidadVendida']} "
                f"= ${med['precio'] * med['cantidadVendida']}"
            )


def buscar_venta():

    nombre = input(
        "Nombre del paciente: "
    ).lower()

    ventas = cargar_json(ARCHIVO_VENTAS)

    encontrado = False

    for venta in ventas:

        if venta["paciente"]["nombre"].lower() == nombre:

            encontrado = True

            print("\nFecha:", venta["fechaVenta"])
            print("Empleado:",
                  venta["empleado"]["nombre"])

            for med in venta["medicamentosVendidos"]:

                print(
                    med["nombreMedicamento"],
                    med["cantidadVendida"]
                )

    if not encontrado:
        print("No se encontraron ventas.")


def eliminar_venta():

    ventas = cargar_json(ARCHIVO_VENTAS)

    listar_ventas()

    if not ventas:
        return

    posicion = int(
        input("\nNúmero de venta a eliminar: ")
    ) - 1

    if 0 <= posicion < len(ventas):

        ventas.pop(posicion)

        guardar_json(ARCHIVO_VENTAS, ventas)

        print("✅ Venta eliminada.")

    else:
        print("Opción inválida.")


def menu_ventas():

    while True:

        print("\n===== MENÚ VENTAS =====")
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("3. Buscar venta")
        print("4. Eliminar venta")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_venta()

        elif opcion == "2":
            listar_ventas()

        elif opcion == "3":
            buscar_venta()

        elif opcion == "4":
            eliminar_venta()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")