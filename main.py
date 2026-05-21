from funciones import *

cargar_datos()

while True:

    print("\n===== GYM CONTROL SYSTEM =====")

    print("1. Registrar cliente")
    print("2. Registrar entrenador")
    print("3. Asignar entrenador")
    print("4. Registrar venta")
    print("5. Pagar mensualidad")
    print("6. Mostrar personas")
    print("7. Cierre del dia")
    print("8. Salir")

    opcion = input("\nSeleccione una opcion: ")

    if opcion == "1":
        registrar_cliente()

    elif opcion == "2":
        registrar_entrenador()

    elif opcion == "3":
        asignar_entrenador()

    elif opcion == "4":
        vender_productos()

    elif opcion == "5":
        pagar_mensualidad()

    elif opcion == "6":
        mostrar_personas()

    elif opcion == "7":
        cierre_dia()

    elif opcion == "8":
        print("\nSaliendo del sistema...")
        break

    else:
        print("\nOpcion invalida")