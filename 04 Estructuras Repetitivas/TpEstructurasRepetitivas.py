#Actividad 1: Imprimir numeros del 0 al 100 (uno por linea).
for i in range(101):  # range(101) incluye desde 0 hasta 100
    print(i)

#Actividad 2: Contar digitos de un numero entero.
numero = int(input("Ingrese un numero entero: "))
cantidad_digitos = len(str(abs(numero)))  # abs() maneja numeros negativos
print("El numero tiene", cantidad_digitos, "digitos.")

#Actividad 3: Sumar numeros entre dos valores (excluyendolos).
inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))
suma = 0

for i in range(min(inicio, fin) + 1, max(inicio, fin)):
    suma += i

print("La suma es:", suma)

#Actividad 4: Sumar numeros hasta ingresar 0.
total = 0
while True:
    numero = int(input("Ingrese un numero (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print("Total acumulado:", total)

#Actividad 5: Juego de adivinar un numero aleatorio.
import random
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el numero (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Intentos:", intentos)
        break
    print("Intenta de nuevo.")

#Actividad 6: Numeros pares del 100 al 0 (decreciente).
for i in range(100, -1, -2):  # De 100 a 0, paso -2 (solo pares)
    print(i)

#Actividad 7: Suma desde 0 hasta un numero positivo.
n = int(input("Ingrese un numero entero positivo: "))
suma = sum(range(n + 1))  # range(n+1) incluye 0 hasta n
print("La suma es:", suma)

#Actividad 8: Estadisticas de 100 numeros.
pares = impares = positivos = negativos = 0

for _ in range(100):  # Cambiar a 5 para pruebas
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares, "| Impares:", impares)
print("Positivos:", positivos, "| Negativos:", negativos)

#Actividad 9: Media de 100 numeros.
suma = 0
for _ in range(100):  # Cambiar a 10 para pruebas
    suma += int(input("Ingrese un número: "))

media = suma / 100  # Ajustar denominador si se prueba con menos numeros
print("Media:", media)

#Actividad 10: Invertir digitos de un numero.
numero = input("Ingrese un número: ")  # Se recibe como cadena
numero_invertido = numero[::-1]  # Inversion con slicing
print("Número invertido:", numero_invertido)