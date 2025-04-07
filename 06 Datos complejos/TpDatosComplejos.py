import math

#Actividad 1: Añadir frutas al diccionario.
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas
precios_frutas.update({
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
})

print("Diccionario actualizado:", precios_frutas)



#Actividad 2: Actualizar precios de frutas.
# Actualizar precios
precios_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})

print("Precios actualizados:", precios_frutas)



#Actividad 3: Lista de frutas (solo nombres).
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)



#Actividad 4: Clase Persona.
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Ejemplo de uso
persona = Persona("Carlos", "México", 28)
persona.saludar()



#Actividad 5: Clase Circulo.
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplo de uso
circulo = Circulo(5)
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Perímetro: {circulo.calcular_perimetro():.2f}")



#Actividad 6: Verificar parentesis balanceados (Utilizando Pila).
def balanceado(s):
    pila = []
    parejas = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in parejas.values():
            pila.append(char)
        elif char in parejas.keys():
            if not pila or pila.pop() != parejas[char]:
                return False
    return len(pila) == 0

# Ejemplos
print(balanceado("([[]])"))  # True
print(balanceado("([[]]"))   # False



#Actividad 7: Sistema de turnos en banco (utilizando Cola).
from collections import deque

class Banco:
    def __init__(self):
        self.cola = deque()

    def encolar(self, cliente):
        self.cola.append(cliente)
        print(f"Cliente '{cliente}' agregado. Turnos en espera: {len(self.cola)}")

    def desencolar(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo a '{cliente}'. Turnos restantes: {len(self.cola)}")
        else:
            print("No hay clientes en espera.")

    def siguiente(self):
        if self.cola:
            print(f"Próximo cliente: '{self.cola[0]}'")
        else:
            print("No hay clientes en espera.")

# Ejemplo de uso
banco = Banco()
banco.encolar("Juan")
banco.encolar("María")
banco.siguiente()  # Próximo cliente: 'Juan'
banco.desencolar() # Atendiendo a 'Juan'



#Actividad 8: Lista enlazada (Inserción al inicio).
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" → ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_inicio(3)
lista.insertar_inicio(2)
lista.insertar_inicio(1)
lista.mostrar()  # 1 → 2 → 3 → None



#Actividad 9:  Invertir lista enlazada.
def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza
    while actual:
        siguiente_temp = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente_temp
    lista.cabeza = anterior

# Continuación del ejemplo anterior
print("Lista original:")
lista.mostrar()  # 1 → 2 → 3 → None

invertir_lista(lista)
print("Lista invertida:")
lista.mostrar()  # 3 → 2 → 1 → None