"""
> Son listas inmutables -> no permiten añadir eliminar, mover, etc.
> Permiten extraer porciones. pero será una nueva tupla.
> No permiten busquedas (no index).
> Sí permiten comprobar si un elemento se encuentra.
>> ventajas
  -> Más rapidas.
  -> Menos espacio en memoria
  -> Formatean Strings
  -> Pueden usarse como claves en un diccionario.
  -> Si se necesita una lista de elementos que solo se va va recorrer, ésta es la mejor opción.
"""
myTuple = ("first", "second", "third", 1, 2, 3, True, False)

print(myTuple)
print(myTuple[:])

print("\nAccediendo por indice")
print(myTuple[2])

print("\nConvirtiendo tuplas en listas y viseversa")
myList = list(myTuple)
myList.extend(["new", "new"])
print(myList)

myTuple2 = tuple(myList)
print(myTuple2)

print("\nComprovando si un elemento se encuentra en la tupla")
print("new" in myTuple)
print("new" in myTuple2)

print("\nCuantas veces se encuentra el elmento en la tupla")
print(myTuple2.count("new"))

print("\nLongitud de la tupla")
print(len(myTuple2))

print("\nTupla unitaria (siempre debe llevar la coma)")
myTuple3 = ("new",)
myTuple4 = ("new")
print(myTuple3[0], " -> length ",len(myTuple3))

print(myTuple4[0] , " -> length ", len(myTuple4))

print("\nDesmpaquetado de tuplas")

myTuple5 = (2024, 10, 1)
año, mes,dia = myTuple5

print(año, mes, dia)