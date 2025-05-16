#Actividad 1:  Ejercicio 1 - Factorial recursivo hasta número dado.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar factoriales desde 1 hasta n
limite = int(input("Ingresá un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")


#Actividad 2:  Ejercicio 2 - Serie de Fibonacci hasta posición dada.
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Mostrar serie completa hasta la posición indicada
n = int(input("Ingresá la cantidad de términos de la serie Fibonacci: "))
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")


#Actividad 3:  Ejercicio 3 - Potencia de forma recursiva.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Prueba
base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")


#Actividad 4:  Ejercicio 4 - Conversión de decimal a binario (en texto).
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Número decimal a convertir: "))
# Caso especial si el número es 0
print("Binario:", decimal_a_binario(numero) if numero > 0 else "0")


#Actividad 5:  Ejercicio 5 - Verificar si una palabra es palíndromo.
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Prueba
texto = input("Ingresá una palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))


#Actividad 6:  Ejercicio 6 - Suma de los dígitos de un número (sin convertir a string).
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

# Prueba
numero = int(input("Número para sumar sus dígitos: "))
print("Suma de dígitos:", suma_digitos(numero))


#Actividad 7:  Ejercicio 7 - Cantidad total de bloques en pirámide.
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Prueba
niveles = int(input("Cantidad de bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(niveles))


#Actividad 8:  Ejercicio 8 - Contar cuántas veces aparece un dígito.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Prueba
numero = int(input("Número: "))
digito = int(input("Dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
