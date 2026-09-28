# El programa pide notas al usuario hasta que ingrese un número menor o igual a 0 
# (como el registro de legajos de la teoría). Al terminar muestra: la lista de notas, cuántas son, la mayor, la menor, el promedio 
# (con f-string y 2 decimales) y la lista invertida sin usar reverse(). Como broche, convertí la lista final en una tupla "de cierre" que ya nadie pueda modificar.
notas = []
while True:
    nota = int(input(f"Ingrese una nota (<=0 para terminar): "))
    if nota <= 0:
        break
    notas.append(nota)
print(f"Notas cargadas: {notas}")
print(f"Cantidad: {len(notas)} | Mayor: {max(notas)}| Menor: {min(notas)}")
print(f"Promedio: {sum(notas)/len(notas):.2f}")
print(f"De la última a la primera: {notas[::-1]}")
print(f"Registro cerrado: {tuple(notas)}")
