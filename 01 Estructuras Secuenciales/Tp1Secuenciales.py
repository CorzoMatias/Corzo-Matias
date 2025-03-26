import math

#Actividad 1: Imprimir "Hola Mundo!"
print("Hola Mundo!")


#Actividad 2: Saludar al usuario por su nombre
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


#Actividad 3: Mostrar datos personales
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


#Actividad 4: Calcular área y perímetro de un círculo
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#Actividad 5: Convertir segundos a horas
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


#Actividad 6: Tabla de multiplicar
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


#Actividad 7: Operaciones con dos números enteros
num1 = int(input("Ingrese el primer número entero (distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")


#Actividad 8: Calcular el Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros (por ejemplo, 1.80): "))

imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")


#Actividad 9: Convertir Celsius a Fahrenheit
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")


#Actividad 10: Calcular el promedio de 3 números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {promedio:.2f}")