import json

ARCHIVO = "data/medicamentos.json"

def cargar():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def guardar(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

def agregar():
    medicamentos = cargar()

    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    fecha = input("Fecha expiración: ")
    proveedor = input("Proveedor: ")

    medicamentos.append({
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "fechaExpiracion": fecha,
        "proveedor": proveedor
    })

    guardar(medicamentos)
    print("Medicamento agregado")

def listar():
    medicamentos = cargar()

    for m in medicamentos:
        print(m)

def buscar():
    nombre = input("Nombre: ")

    medicamentos = cargar()

    for m in medicamentos:
        if m["nombre"].lower() == nombre.lower():
            print(m)
            return

    print("No encontrado")

def actualizar():
    nombre = input("Nombre: ")

    medicamentos = cargar()

    for m in medicamentos:

        if m["nombre"].lower() == nombre.lower():

            m["precio"] = float(input("Nuevo precio: "))
            m["stock"] = int(input("Nuevo stock: "))

            guardar(medicamentos)

            print("Actualizado")
            return

    print("No encontrado")

def eliminar():
    nombre = input("Nombre: ")

    medicamentos = cargar()

    medicamentos = [
        m for m in medicamentos
        if m["nombre"].lower() != nombre.lower()
    ]

    guardar(medicamentos)

    print("Eliminado")

def menu_medicamentos():

    while True:

        print("\n=== MEDICAMENTOS ===")
        print("1. Agregar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("0. Volver")

        op = input("Seleccione: ")

        if op == "1":
            agregar()

        elif op == "2":
            listar()

        elif op == "3":
            buscar()

        elif op == "4":
            actualizar()

        elif op == "5":
            eliminar()

        elif op == "0":
            break