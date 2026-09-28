# # Parte 1 - Cadenas
# Las cadenas (str) son secuencias inmutables de caracteres: podés leerlas con índices y slices,
# pero no modificarlas "en el lugar" — los métodos como upper() siempre devuelven una cadena nueva.

# Ejercicio 1.1: Pedí una palabra y mostrala en mayúsculas, en minúsculas y con la primera letra en mayúscula.
# palabra = input("Ingrese una palabra: ")
# print(f"Mayúsculas: {palabra.upper()}")
# print(f"Minúsculas: {palabra.lower()}")
# print(f"Primera letra en mayúscula: {palabra.capitalize()}")

# Ejercicio 1.2:  Ingresá una frase y mostrá la cantidad de palabras que contiene.
# frase = input("Ingrese una frase: ")
# print(f"La cantidad de palabras en la frase es: {len(frase.split())}")

# Ejercicio 1.3: Escribí un programa que reemplace todas las vocales de una palabra por *.
# palabra = input("Ingrese una palabra: ")
# for letra in palabra:
#     if letra.lower() in "aeiou":
#         palabra = palabra.replace(letra, "*")
# print(f"Palabra con vocales reemplazadas: {palabra}")

# Ejercicio 1.4:  Pedí una palabra y mostrá, usando segmentos (slices): los primeros 3 caracteres, los últimos 3 y la palabra invertida.
# palabra = input("Ingrese una palabra: ")
# print(f"Primeros 3 caracteres: {palabra[:3]}")
# print(f"Últimos 3 caracteres: {palabra[-3:]}")
# print(f"Palabra invertida: {palabra[::-1]}")

# # Parte 2 - Listas
# Las listas son secuencias mutables: se pueden agregar, quitar y reemplazar elementos después de creadas. Es la gran diferencia con cadenas y tuplas.

# Ejercicio 2.1: Creá una lista vacía y pedile al usuario que ingrese 5 números. Luego mostrá: la lista completa, el mayor y el menor número.
# lista= []
# for i in range(5):
#     numero = int(input(f"Ingrese el número {i + 1}: "))
#     lista.append(numero)
# print(f"Lista completa: {lista}")
# print(f"Númeor mayor: {max(lista)}")
# print(f"Número menor: {min(lista)}")

# Ejercicio 2.2: A partir de la lista ["pera", "banana", "manzana"], agregá "uva" al final, eliminá "banana" e imprimí la lista resultante.
# frutas = ["pera", "banana", "manzana"]
# frutas.append("uva")
# frutas.remove("banana")
# print(frutas)

# Ejercicio 2.3. Escribí un programa que invierta una lista sin usar el método reverse().
# lista = []
# nueva_lista = []
# for i in range(int(input("Ingrese la cantidad de elementos: "))):
#     lista.append(input(f"Ingrese el elemento N° {i+1}: "))
#     nueva_lista.insert(0,lista[i])
# print(f"Lista resultante: {lista}")
# print(f"Lista invertida: {nueva_lista}")


# # Parte 3 — Listas anidadas (matrices)
# Una lista dentro de otra lista está anidada. Si cada elemento es una fila, tenés una matriz: 
# matriz[fila][columna] accede a un valor puntual (primer índice = fila, segundo = columna).

# Ejercicio 3.1. Creá una matriz de 2x2 con números ingresados por el usuario y mostrala en forma de tabla.
# matris = []
# for i in range(2):
#     fila = []
#     for j in range(2):
#         fila.append(input(f"Ingrese el elemento {i, j}: "))
#     matris.append(fila)
# for i in range(len(matris)):
#     for j in range(len(matris[i])):
#         print(matris[i][j], end=" ")
#     print()

# Ejercicio 3.2 ★. Calculá la suma de todos los elementos de una matriz de 3x3 definida en el código.
# matriz = []
# suma = 0
# for i in range(3):
#     fila = []
#     for j in range(3):
#         fila.append(int(input(f"Ingrese el elemento {i+1, j+1}: ")))
#         suma += fila[j]
#     matriz.append(fila)
# print(f"Matriz = {matriz}")
# print(f"La suma de todos los elementos es: {suma}")

# # Parte 4 — Tuplas
# Las tuplas son como listas pero inmutables: una vez creadas no se pueden modificar 
# (no tienen append ni remove). Se usan para datos que no deberían cambiar, y permiten "desempaquetar" varios valores de una vez.

# Ejercicio 4.1 ★. Creá una tupla con 5 números y mostrá el primero y el último.
# tupla = (1,2,3,4,5)
# print("Tupla: ",tupla)
# print(f"Primer número: {tupla[0]}")
# print(f"Último número: {tupla[-1]}")

# Ejercicio 4.2 ★. A partir de la lista de notas [8, 6, 9, 7], generá una tupla y calculá el promedio.
# notas = [8, 6, 9, 7]
# notas = tuple(notas)
# promedio = sum(notas)/len(notas)
# print(f"Las notas fueron: {notas}")
# print(f"El promedio es: {promedio}")

# Ejercicio 4.3. Creá una tupla con tres colores y mostrala desempaquetándola en variables individuales.