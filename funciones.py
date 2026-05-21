from clases import *
import datos
import os
import json

RUTA_BASE = os.path.dirname(__file__)
RUTA_JSON = os.path.join(RUTA_BASE, "datos_gym.json")

def guardar_datos():
    datos_gym = {
        "clientes": [],
        "entrenadores": [],
        "productos": []
    }

    # CLIENTES
    for cliente in datos.clientes:
        datos_gym["clientes"].append({
           "nombre": cliente.nombre,
            "edad": cliente.edad,
            "cedula": cliente.cedula,
            "mensualidad_pagada": cliente.mensualidad_pagada
        })

    # ENTRENADORES
    for entrenador in datos.entrenadores:
        datos_gym["entrenadores"].append({
            "nombre": entrenador.nombre,
            "edad": entrenador.edad,
            "cedula": entrenador.cedula,
            "clientes_asignados": entrenador.clientes_asignados
        })

    # PRODUCTOS
    for producto in datos.productos:
        datos_gym["productos"].append({
            "nombre": producto.nombre,
            "precio": producto.precio,
            "stock": producto.stock,
            "vendidos": producto.vendidos
        })
    with open(RUTA_JSON, "w") as archivo:
        json.dump(datos_gym, archivo, indent=4)
    print("Datos guardados correctamente")
def cargar_datos():
    try:
        with open(RUTA_JSON, "r") as archivo:
            datos_gym = json.load(archivo)
        # CLIENTES
        for c in datos_gym["clientes"]:
            cliente = Cliente(
                c["nombre"],
                c["edad"],
                c["cedula"]
            )
            cliente.mensualidad_pagada = c["mensualidad_pagada"]
            datos.clientes.append(cliente)

        # ENTRENADORES
        for e in datos_gym["entrenadores"]:
            entrenador = Entrenador(
                e["nombre"],
                e["edad"],
                e["cedula"]
            )
            entrenador.clientes_asignados = e["clientes_asignados"]
            datos.entrenadores.append(entrenador)

        # PRODUCTOS
        datos.productos.clear()
        for p in datos_gym["productos"]:
            producto = Producto(
                p["nombre"],
                p["precio"],
                p["stock"]
            )
            producto.vendidos = p["vendidos"]
            datos.productos.append(producto)
        print("Datos cargados correctamente")

    except:
        print("No existe archivo JSON todavía")


def registrar_cliente():
    print("\n--- REGISTRO CLIENTE ---")
    # VALIDAR NOMBRE
    while True:
        nombre = input("Nombre: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Nombre invalido, solo se permiten letras")

    # VALIDAR EDAD
    while True:
        edad = input("Edad: ")
        if edad.isdigit():
            edad = int(edad)
            if edad > 0 and edad <= 100:
                break
            else:
                print("Edad invalida, debe estar entre 1 y 100")
        else:
            print("La edad solo puede contener numeros")

    # VALIDAR CEDULA
    while True:
        cedula = input("Cedula: ")
        if cedula.isdigit():
            cedula_repetida = False
            for cliente in datos.clientes:
                if cliente.cedula == cedula:
                    cedula_repetida = True
                    break
            if cedula_repetida:
                print("Ya existe un cliente con esa cedula")
            else:
                break
        else:
            print("La cedula solo puede contener numeros")
    cliente = Cliente(nombre, edad, cedula)
    datos.clientes.append(cliente)
    guardar_datos()
    print(f"\nCliente {nombre} registrado correctamente")


def registrar_entrenador():
    print("\n--- REGISTRO ENTRENADOR ---")
    while True:
        nombre = input("Nombre: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Nombre invalido, solo se permiten letras")

    while True:
        edad = input("Edad: ")
        if edad.isdigit():
            edad = int(edad)
            if edad > 0 and edad <= 100:
                break
            else:
                print("Edad invalida, debe estar entre 1 y 100")
        else:
            print("La edad solo puede contener numeros")

    while True:
        cedula = input("Cedula: ")
        if cedula.isdigit():
            cedula_repetida = False
            for entrenador in datos.entrenadores:
                if entrenador.cedula == cedula:
                    cedula_repetida = True
                    break
            if cedula_repetida:
                print("Ya existe un entrenador con esa cedula")
            else:
                break
        else:
            print("La cedula solo puede contener numeros")
    entrenador = Entrenador(nombre, edad, cedula)
    datos.entrenadores.append(entrenador)
    guardar_datos()
    print(f"\nEntrenador {nombre} registrado correctamente")


def asignar_entrenador():
    if not datos.clientes or not datos.entrenadores:
        print("Debe haber clientes y entrenadores registrados")
        return
    print("\n--- CLIENTES ---")
    for i in range(len(datos.clientes)):
        print(f"{i+1}. {datos.clientes[i].nombre}")
    while True:
        cliente_op = input("Seleccione cliente: ")
        if cliente_op.isdigit():
            cliente_op = int(cliente_op) - 1
            if cliente_op >= 0 and cliente_op < len(datos.clientes):
                break
            else:
                print("Ese cliente no existe")
        else:
            print("Debe ingresar solo numeros")
    print("\n--- ENTRENADORES ---")
    for i in range(len(datos.entrenadores)):
        print(f"{i+1}. {datos.entrenadores[i].nombre}")
    while True:
        entrenador_op = input("Seleccione entrenador: ")
        if entrenador_op.isdigit():
            entrenador_op = int(entrenador_op) - 1
            if entrenador_op >= 0 and entrenador_op < len(datos.entrenadores):
                break
            else:
                print("Ese entrenador no existe")
        else:
            print("Debe ingresar solo numeros")
    cliente = datos.clientes[cliente_op]
    entrenador = datos.entrenadores[entrenador_op]
    entrenador.asignar_cliente(cliente)
    guardar_datos()
    print(f"\n{cliente.nombre} ahora entrenará con {entrenador.nombre}")

def vender_productos():
    while True:
        print("\n" + "="*35)
        print("        INVENTARIO GYM")
        print("="*35)
        contador = 1
        for producto in datos.productos:
            print(f"{contador}. {producto.nombre}")
            print(f"   Precio: ${producto.precio}")
            print(f"   Stock: {producto.stock}")
            contador += 1
        print(f"{contador}. Salir")

        try:
            opcion = int(input("\nSeleccione producto: "))

        except:
            print("Ingrese un numero valido")
            continue

        if opcion == contador:
            print("\nVolviendo al menu principal")
            input("Dar enter para seguir")
            break

        if opcion < 1 or opcion > len(datos.productos):
            print("Opcion invalida")
            continue
        producto = datos.productos[opcion - 1]

        try:
            cantidad = int(input(f"Cantidad de {producto.nombre}: "))

        except:
            print("Cantidad invalida")
            continue

        if producto.vender(cantidad):
            guardar_datos()
            total = cantidad * producto.precio
            print("\nVenta registrada correctamente")
            print(f"Total vendido: ${total}")
            input("Dar enter para seguir")
        else:
            print("\nNo hay suficiente stock")


def pagar_mensualidad():
    if not datos.clientes:
        print("No hay clientes registrados")
        input("Dar enter para seguir")
        return

    print("\n--- CLIENTES ---")
    for i in range(len(datos.clientes)):
        print(f"{i+1}. {datos.clientes[i].nombre}")

    try:
        opcion = int(input("Seleccione cliente: ")) - 1
        cliente = datos.clientes[opcion]

    except:
        print("Opcion invalida")
        input("Dar enter para seguir")
        return

    if cliente.mensualidad_pagada:
        print(f"\n{cliente.nombre} ya tiene la mensualidad paga")
        input("Dar enter para seguir")
        return
    cliente.pagar_mensualidad()
    guardar_datos()
    print(f"\nMensualidad pagada correctamente por {cliente.nombre}")
    input("Dar enter para seguir")


def mostrar_personas():
    print("\n" + "="*45)
    print("        PERSONAS REGISTRADAS")
    print("="*45)
    personas = datos.clientes + datos.entrenadores
    if not personas:
        print("No hay personas registradas")
        input("Dar enter para seguir")
        return

    for persona in personas:
        print("\n------------------------------")
        print(f"Nombre : {persona.nombre}")
        print(f"Edad   : {persona.edad}")
        print(f"Cedula : {persona.cedula}")
        if isinstance(persona, Cliente):
            print("Rol     : Cliente")
            if persona.mensualidad_pagada:
                print("Mensualidad : Pagada")
            else:
                print("Mensualidad : Pendiente")
        elif isinstance(persona, Entrenador):
            print("Rol     : Entrenador")
            print(f"Clientes asignados: {len(persona.clientes_asignados)}")
    print("\n" + "="*45)
    input("Dar enter para seguir")


def cierre_dia():
    print("\n" + "=" * 35)
    print("      CIERRE DEL GIMNASIO")
    print("=" * 35)
    total_mensualidades = 0

    # MENSUALIDADES
    for cliente in datos.clientes:
        if cliente.mensualidad_pagada:
            total_mensualidades += 80000

    print(f"\nIngreso mensualidades: ${total_mensualidades}")
    # PRODUCTOS
    total_productos = 0

    print("\n--- PRODUCTOS VENDIDOS ---")
    for producto in datos.productos:
        subtotal = producto.vendidos * producto.precio
        total_productos += subtotal
        print(f"\n{producto.nombre}")
        print(f"Vendidos: {producto.vendidos}")
        print(f"Ganancia: ${subtotal}")
    print(f"\nTotal productos: ${total_productos}")
    print(f"\nTOTAL GENERAL: ${total_productos + total_mensualidades}")
    print("=" * 35)
    input("Dar enter para seguir")