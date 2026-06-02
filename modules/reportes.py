import json


ARCHIVO_MEDICAMENTOS = "data/medicamentos.json"
ARCHIVO_VENTAS = "data/ventas.json"
ARCHIVO_COMPRAS = "data/compras.json"
ARCHIVO_PROVEEDORES = "data/proveedores.json"
ARCHIVO_EMPLEADOS = "data/empleados.json"


def cargar_json(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


# =====================================
# REPORTE 1
# Medicamentos con stock menor a 50
# =====================================

def stock_bajo():

    medicamentos = cargar_json(ARCHIVO_MEDICAMENTOS)

    print("\nMEDICAMENTOS CON STOCK MENOR A 50\n")

    for medicamento in medicamentos:

        if medicamento["stock"] < 50:

            print(
                medicamento["nombre"],
                "Stock:",
                medicamento["stock"]
            )


# =====================================
# REPORTE 2
# Proveedores y contacto
# =====================================

def proveedores_contacto():

    proveedores = cargar_json(ARCHIVO_PROVEEDORES)

    print("\nLISTA DE PROVEEDORES\n")

    for proveedor in proveedores:

        print(
            proveedor["nombre"],
            "-",
            proveedor["contacto"]
        )


# =====================================
# REPORTE 3
# Medicamentos comprados a ProveedorA
# =====================================

def compras_proveedor_a():

    compras = cargar_json(ARCHIVO_COMPRAS)

    print("\nMEDICAMENTOS DE PROVEEDOR A\n")

    for compra in compras:

        if compra["proveedor"]["nombre"] == "ProveedorA":

            for medicamento in compra["medicamentosComprados"]:

                print(
                    medicamento["nombreMedicamento"]
                )


# =====================================
# REPORTE 4
# Total ventas Paracetamol
# =====================================

def total_ventas_paracetamol():

    ventas = cargar_json(ARCHIVO_VENTAS)

    total = 0

    for venta in ventas:

        for medicamento in venta["medicamentosVendidos"]:

            if medicamento["nombreMedicamento"] == "Paracetamol":

                total += (
                    medicamento["cantidadVendida"]
                    * medicamento["precio"]
                )

    print("\nTOTAL PARACETAMOL: $", total)


# =====================================
# REPORTE 5
# Medicamento más caro
# =====================================

def medicamento_mas_caro():

    medicamentos = cargar_json(ARCHIVO_MEDICAMENTOS)

    mayor = medicamentos[0]

    for medicamento in medicamentos:

        if medicamento["precio"] > mayor["precio"]:
            mayor = medicamento

    print("\nMEDICAMENTO MÁS CARO")

    print(
        mayor["nombre"],
        "$",
        mayor["precio"]
    )


# =====================================
# REPORTE 6
# Ingresos totales
# =====================================

def ingresos_totales():

    ventas = cargar_json(ARCHIVO_VENTAS)

    total = 0

    for venta in ventas:

        for medicamento in venta["medicamentosVendidos"]:

            total += (
                medicamento["cantidadVendida"]
                * medicamento["precio"]
            )

    print("\nINGRESOS TOTALES")

    print("$", total)


# =====================================
# REPORTE 7
# Medicamentos no vendidos
# =====================================

def medicamentos_no_vendidos():

    medicamentos = cargar_json(ARCHIVO_MEDICAMENTOS)
    ventas = cargar_json(ARCHIVO_VENTAS)

    vendidos = []

    for venta in ventas:

        for medicamento in venta["medicamentosVendidos"]:

            vendidos.append(
                medicamento["nombreMedicamento"]
            )

    print("\nMEDICAMENTOS NO VENDIDOS\n")

    for medicamento in medicamentos:

        if medicamento["nombre"] not in vendidos:

            print(medicamento["nombre"])


# =====================================
# REPORTE 8
# Cantidad ventas por empleado
# =====================================

def ventas_por_empleado():

    ventas = cargar_json(ARCHIVO_VENTAS)

    empleados = {}

    for venta in ventas:

        nombre = venta["empleado"]["nombre"]

        empleados[nombre] = (
            empleados.get(nombre, 0) + 1
        )

    print("\nVENTAS POR EMPLEADO\n")

    for nombre, cantidad in empleados.items():

        print(nombre, ":", cantidad)


# =====================================
# REPORTE 9
# Empleados con más de 5 ventas
# =====================================

def empleados_mas_5_ventas():

    ventas = cargar_json(ARCHIVO_VENTAS)

    empleados = {}

    for venta in ventas:

        nombre = venta["empleado"]["nombre"]

        empleados[nombre] = (
            empleados.get(nombre, 0) + 1
        )

    print("\nEMPLEADOS CON MÁS DE 5 VENTAS\n")

    for nombre, cantidad in empleados.items():

        if cantidad > 5:

            print(nombre)


# =====================================
# REPORTE 10
# Pacientes que compraron Paracetamol
# =====================================

def pacientes_paracetamol():

    ventas = cargar_json(ARCHIVO_VENTAS)

    pacientes = set()

    for venta in ventas:

        for medicamento in venta["medicamentosVendidos"]:

            if medicamento["nombreMedicamento"] == "Paracetamol":

                pacientes.add(
                    venta["paciente"]["nombre"]
                )

    print("\nPACIENTES QUE COMPRARON PARACETAMOL\n")

    for paciente in pacientes:

        print(paciente)


# =====================================
# MENÚ
# =====================================

def menu_reportes():

    while True:

        print("\n===== REPORTES =====")
        print("1. Stock menor a 50")
        print("2. Proveedores")
        print("3. Compras ProveedorA")
        print("4. Total ventas Paracetamol")
        print("5. Medicamento más caro")
        print("6. Ingresos totales")
        print("7. Medicamentos no vendidos")
        print("8. Ventas por empleado")
        print("9. Empleados con más de 5 ventas")
        print("10. Pacientes que compraron Paracetamol")
        print("0. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            stock_bajo()

        elif opcion == "2":
            proveedores_contacto()

        elif opcion == "3":
            compras_proveedor_a()

        elif opcion == "4":
            total_ventas_paracetamol()

        elif opcion == "5":
            medicamento_mas_caro()

        elif opcion == "6":
            ingresos_totales()

        elif opcion == "7":
            medicamentos_no_vendidos()

        elif opcion == "8":
            ventas_por_empleado()

        elif opcion == "9":
            empleados_mas_5_ventas()

        elif opcion == "10":
            pacientes_paracetamol()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")