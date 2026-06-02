import json
from datetime import datetime

ARCHIVO_COMPRAS = "data/compras.json"
ARCHIVO_MEDICAMENTOS = "data/medicamentos.json"
ARCHIVO_PROVEEDORES = "data/proveedores.json"


def cargar_json(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def guardar_json(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def registrar_compra():

    compras = cargar_json(ARCHIVO_COMPRAS)
    medicamentos = cargar_json(ARCHIVO_MEDICAMENTOS)
    proveedores = cargar_json(ARCHIVO_PROVEEDORES)

    if not proveedores:
        print("No hay proveedores registrados.")
        return

    if not medicamentos:
        print("No hay medicamentos registrados.")
        return

    print("\n===== PROVEEDORES =====")

    for i, proveedor in enumerate(proveedores, start=1):
        print(f"{i}. {proveedor['nombre']}")

    pos_proveedor = int(input("Seleccione proveedor: ")) - 1

    if pos_proveedor < 0 or pos_proveedor >= len(proveedores):
        print("Proveedor inválido.")
        return

    proveedor = proveedores[pos_proveedor]

    medicamentos_comprados = []

    while True:

        print("\n===== MEDICAMENTOS =====")

        for i, medicamento in enumerate(medicamentos, start=1):
            print(
                f"{i}. {medicamento['nombre']} | "
                f"Stock actual: {medicamento['stock']}"
            )

        pos_medicamento = int(
            input("Seleccione medicamento: ")
        ) - 1

        if pos_medicamento < 0 or pos_medicamento >= len(medicamentos):
            print("Medicamento inválido.")
            continue

        medicamento = medicamentos[pos_medicamento]

        cantidad = int(
            input("Cantidad comprada: ")
        )

        precio_compra = float(
            input("Precio de compra: ")
        )

        medicamento["stock"] += cantidad

        medicamentos_comprados.append({
            "nombreMedicamento": medicamento["nombre"],
            "cantidadComprada": cantidad,
            "precioCompra": precio_compra
        })

        continuar = input(
            "¿Agregar otro medicamento? (s/n): "
        ).lower()

        if continuar != "s":
            break

    compra = {
        "fechaCompra": datetime.now().strftime("%Y-%m-%d"),
        "proveedor": proveedor,
        "medicamentosComprados": medicamentos_comprados
    }

    compras.append(compra)

    guardar_json(ARCHIVO_COMPRAS, compras)
    guardar_json(ARCHIVO_MEDICAMENTOS, medicamentos)

    print("Compra registrada correctamente.")


def listar_compras():

    compras = cargar_json(ARCHIVO_COMPRAS)

    if not compras:
        print("No hay compras registradas.")
        return

    print("\n===== COMPRAS =====")

    for i, compra in enumerate(compras, start=1):

        print(f"\nCOMPRA #{i}")
        print("Fecha:", compra["fechaCompra"])
        print("Proveedor:",
              compra["proveedor"]["nombre"])

        print("Medicamentos:")

        for medicamento in compra["medicamentosComprados"]:

            print(
                f"- {medicamento['nombreMedicamento']} | "
                f"Cantidad: {medicamento['cantidadComprada']} | "
                f"Precio Compra: ${medicamento['precioCompra']}"
            )


def buscar_compra():

    nombre = input(
        "Nombre del proveedor: "
    ).lower()

    compras = cargar_json(ARCHIVO_COMPRAS)

    encontrado = False

    for compra in compras:

        if compra["proveedor"]["nombre"].lower() == nombre:

            encontrado = True

            print("\nFecha:",
                  compra["fechaCompra"])

            for medicamento in compra["medicamentosComprados"]:

                print(
                    medicamento["nombreMedicamento"],
                    medicamento["cantidadComprada"]
                )

    if not encontrado:
        print("No se encontraron compras.")


def eliminar_compra():

    compras = cargar_json(ARCHIVO_COMPRAS)

    listar_compras()

    if not compras:
        return

    posicion = int(
        input("\nNúmero de compra a eliminar: ")
    ) - 1

    if 0 <= posicion < len(compras):

        compras.pop(posicion)

        guardar_json(ARCHIVO_COMPRAS, compras)

        print("Compra eliminada.")

    else:
        print("Opción inválida.")


def menu_compras():

    while True:

        print("\n===== MENÚ COMPRAS =====")
        print("1. Registrar compra")
        print("2. Listar compras")
        print("3. Buscar compra")
        print("4. Eliminar compra")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_compra()

        elif opcion == "2":
            listar_compras()

        elif opcion == "3":
            buscar_compra()

        elif opcion == "4":
            eliminar_compra()

        elif opcion == "0":
            break

        else:
            print("Opción inválida.")