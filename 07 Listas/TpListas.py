#Actividad 1: Lista de múltiplos de 4 del 1 al 100:
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


#Actividad 2: Mostrar el penúltimo elemento de una lista:
lista = ["manzana", "banana", "naranja", "uva", "pera"]
print(lista[-2])  # Usando índice negativo para contar desde el final


#Actividad 3: Lista vacía con palabras agregadas:
lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("Java")
lista_vacia.append("C++")
print(lista_vacia)


#Actividad 4: Reemplazar segundo y último valor en lista "animales":
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"    # Segundo elemento (índice 1)
animales[-1] = "oso"    # Último elemento (índice -1)
print(animales)


#Actividad 5: Análisis del programa dado:
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)


#Actividad 6: Lista del 10 al 30 con saltos de 5:
numeros = list(range(10, 31, 5))
print(numeros[:2])  # Mostrar los dos primeros elementos


#Actividad 7: Reemplazar valores centrales en lista "autos":
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "pickup"]  # Reemplaza índices 1 y 2
print(autos)


#Actividad 8: Lista "dobles" con valores calculados:
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)


#Actividad 9: Manipulación de lista anidada "compras":
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"
# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")
# d) Imprimir lista resultante
print(compras)


#Actividad 10: Creación de lista anidada "lista_anidada":
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)