import math

#Actividad 1: Funcion imprimir_hola_mundo.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamada desde el programa principal
imprimir_hola_mundo()



#Actividad 2: Funcion saludar_usuario.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Llamada desde el programa principal
nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))



#Actividad 3: Funcion informacion_personal.
def información_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Solicitar datos al usuario
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

# Llamada a la función
información_personal(nombre, apellido, edad, residencia)



#Actividad 4: Funciones calcular_area_circulo y calcular_perimetro_circulo.
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Solicitar radio al usuario
radio = float(input("Ingrese el radio del circulo: "))

# Mostrar resultados
print(f"Area: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")



#Actividad 5: Funcion segundos_a_horas.
def segundos_a_horas(segundos):
    return segundos / 3600

# Solicitar segundos al usuario
segundos = int(input("Ingrese la cantidad de segundos: "))

# Mostrar resultado
print(f"Horas equivalentes: {segundos_a_horas(segundos):.2f}")



#Actividad 6: Funcion tabla_multiplicar.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar número al usuario
numero = int(input("Ingrese un numero para generar su tabla de multiplicar: "))

# Llamada a la función
tabla_multiplicar(numero)



#Actividad 7: Funcion operaciones_basicas.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: division por cero"
    return suma, resta, multiplicacion, division

# Solicitar números al usuario
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

# Mostrar resultados
resultados = operaciones_basicas(num1, num2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"División: {resultados[3]}")



#Actividad 8: Funcion calcular_imc.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Mostrar resultado con 2 decimales
print(f"IMC: {calcular_imc(peso, altura):.2f}")



#Actividad 9: Funcion celsius_a_fahrenheit.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Solicitar temperatura al usuario
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Mostrar resultado
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")



#Actividad 10: Funcion calcular_promedio.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Mostrar resultado
print(f"Promedio: {calcular_promedio(num1, num2, num3):.2f}")