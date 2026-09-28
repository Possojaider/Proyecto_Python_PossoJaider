# 💊 Sistema de Gestión de Farmacia

Sistema de gestión desarrollado en **Python** para administrar las principales operaciones de una farmacia mediante una aplicación de consola. El proyecto permite gestionar medicamentos, proveedores, pacientes, empleados, compras y ventas utilizando archivos **JSON** como sistema de almacenamiento.

## 📌 Descripción

El sistema fue desarrollado con el objetivo de facilitar la administración de una farmacia, permitiendo registrar, consultar, actualizar y eliminar información, además de generar diferentes reportes relacionados con el inventario y las operaciones realizadas.

El proyecto aplica conceptos fundamentales de programación como:

- Funciones
- Condicionales
- Ciclos
- Listas y diccionarios
- Manejo de archivos
- Archivos JSON
- CRUD
- Manejo de excepciones
- Modularización
- Menús interactivos
- Generación de reportes

## 🚀 Funcionalidades

### 💊 Gestión de medicamentos

Permite:

- Registrar medicamentos.
- Listar medicamentos.
- Buscar medicamentos.
- Actualizar información.
- Eliminar medicamentos.
- Consultar precios y stock.
- Controlar fechas de vencimiento.

### 🏢 Gestión de proveedores

Permite administrar la información de los proveedores:

- Registrar proveedores.
- Consultar proveedores.
- Actualizar información.
- Eliminar proveedores.
- Consultar datos de contacto.

### 👥 Gestión de pacientes

Permite:

- Registrar pacientes.
- Consultar pacientes.
- Actualizar información.
- Eliminar pacientes.

### 👨‍💼 Gestión de empleados

Permite administrar:

- Nombre del empleado.
- Cargo.
- Fecha de ingreso.
- Información relacionada con sus ventas.

### 🛒 Gestión de compras

Permite registrar las compras realizadas a los proveedores y relacionarlas con los medicamentos correspondientes.

### 💰 Gestión de ventas

Permite:

- Registrar ventas.
- Consultar ventas.
- Relacionar medicamentos con pacientes.
- Registrar cantidades y precios.
- Consultar ventas realizadas por empleados.

### 📊 Reportes

El sistema genera información para analizar las operaciones de la farmacia, incluyendo:

- Medicamentos con bajo stock.
- Medicamentos próximos a vencer.
- Medicamentos más y menos vendidos.
- Total de ventas.
- Ventas por empleado.
- Ventas por medicamento.
- Compras por proveedor.
- Pacientes con mayor consumo.
- Proveedores con mayor cantidad de medicamentos suministrados.
- Medicamentos que nunca han sido vendidos.

## 📁 Estructura del proyecto

```text
Farmacia/
│
├── main.py
│
├── modules/
│   ├── medicamentos.py
│   ├── proveedores.py
│   ├── pacientes.py
│   ├── empleados.py
│   ├── compras.py
│   ├── ventas.py
│   └── reportes.py
│
└── data/
    ├── Medicamentos.json
    ├── Proveedores.json
    ├── Pacientes.json
    ├── Empleados.json
    ├── Compras.json
    └── Ventas.json
```

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **JSON**
- Programación modular
- Consola/Terminal
- Git
- GitHub

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Possojaider/nombre-del-repositorio.git
```

### 2. Entrar al proyecto

```bash
cd Farmacia
```

### 3. Ejecutar el sistema

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## 🖥️ Uso

Al ejecutar el programa se mostrará un menú principal:

```text
========================================
       SISTEMA DE GESTIÓN FARMACIA
========================================
1. Gestión de Medicamentos
2. Gestión de Proveedores
3. Gestión de Pacientes
4. Gestión de Empleados
5. Gestión de Compras
6. Gestión de Ventas
7. Reportes
8. Salir
========================================
Seleccione una opción:
```

El usuario puede seleccionar una opción y acceder al módulo correspondiente.

## 💾 Almacenamiento

La información del sistema se almacena mediante archivos **JSON**, separados según el tipo de información:

```text
Medicamentos.json
Proveedores.json
Pacientes.json
Empleados.json
Compras.json
Ventas.json
```

Esto permite conservar los datos aunque el programa se cierre.

## 🔄 Operaciones CRUD

Los módulos principales utilizan operaciones CRUD:

| Operación | Descripción |
|---|---|
| **Create** | Crear nuevos registros |
| **Read** | Consultar registros |
| **Update** | Modificar registros |
| **Delete** | Eliminar registros |

## 🎯 Objetivos del proyecto

- Aplicar fundamentos de programación en Python.
- Trabajar con estructuras de datos.
- Aprender a manipular archivos JSON.
- Implementar operaciones CRUD.
- Aplicar programación modular.
- Desarrollar menús interactivos.
- Generar reportes a partir de información almacenada.
- Simular un sistema de gestión para un negocio real.

## 📚 Conceptos aprendidos

Durante el desarrollo del proyecto se trabajaron conceptos como:

```text
Python
 ├── Variables
 ├── Condicionales
 ├── Ciclos
 ├── Funciones
 ├── Listas
 ├── Diccionarios
 ├── Módulos
 ├── try / except
 ├── Archivos
 ├── JSON
 ├── CRUD
 └── Reportes
```

## 👨‍💻 Autor

**Jaider Santiago Posso Mosquera**

Proyecto académico desarrollado como práctica de programación en Python y gestión de información mediante archivos JSON.
