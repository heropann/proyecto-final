# ===== CLASE PADRE =====

class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula

    def mostrar_rol(self):
        print(f"{self.nombre} pertenece al gimnasio")

# ===== CLIENTE =====

class Cliente(Persona):
    def __init__(self, nombre, edad, cedula):
        super().__init__(nombre, edad, cedula)
        self.mensualidad_pagada = False

    def pagar_mensualidad(self):
        self.mensualidad_pagada = True

    def mostrar_rol(self):
       print(f"{self.nombre} es cliente del gimnasio")


# ===== ENTRENADOR =====

class Entrenador(Persona):
    def __init__(self, nombre, edad, cedula):
        super().__init__(nombre, edad, cedula)
        self.clientes_asignados = []

    def asignar_cliente(self, cliente):
        self.clientes_asignados.append(cliente.nombre)

    def mostrar_rol(self):
        print(f"{self.nombre} es entrenador del gimnasio")

# ===== PRODUCTO =====

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.vendidos = 0

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            self.vendidos += cantidad
            return True
        return False