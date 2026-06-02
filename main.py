import os
from modules.medicamentos import menu_medicamentos
from modules.proveedores import menu_proveedores
from modules.pacientes import menu_pacientes
from modules.empleados import menu_empleados
from modules.compras import menu_compras
from modules.ventas import menu_ventas
from modules.reportes import menu_reportes

def menu_principal():
    while True:
     os.system("clear" if os.name == 'posix' else 'clear')

     print(""" 
----------SISTEMA DE GESTIÓN DE FARMACIA----------
           1. Gestión de Medicamentos
           2. Gestión de Proveedores
           3. Gestión de Pacientes
           4. Gestión de Empleados
           5. Gestión de Compras
           6. Gestión de Ventas
           7. Reportes
           8. Salir
""")
     
     opcion = input('Seleccione una opción: ')

     match opcion:
        case '1':
            menu_medicamentos()
        case "2":
            menu_proveedores()
        case "3":
            menu_pacientes()
        case "4":
            menu_empleados()
        case "5":
            menu_compras()
        case "6":
            menu_ventas()
        case "7":
             menu_reportes()
        case "8":
             print("\nSaliendo del sistema...")
             break
        case _:
            print("\nOpción no válida.")


    input("\nPresione Enter para continuar...")

menu_principal()




