monts = ["January", "February", "March", "April"];

print(monts[0], monts[2])
print(monts[:])
print(monts)
print(monts[2:])
print(monts[1:3])
print(monts[:2])
print(monts[-3])

# Agregar
monts.append("May") # Agrega al filnal
monts.insert(2, "June") # Agrega en un posicion dad
monts.extend(["July", "August", "September"]) # Concatena las listas
print(monts)

#tamaño
print(len(monts))

#Indice por nombre
print(monts.index("August"))

# Verifica la existencia del elemnto in()
print("August" in monts)

# sort
monts.sort()
print(monts)

# Eliminar
del monts[2]
print(monts, '----->')

# Eliminar último
monts.pop()
print(monts)

# Eliminar con pop una posición especifica
monts.pop(0);
print(monts)

# Eliminar por nombre
monts.remove("January")
print(monts)

# Repetidor
print(monts * 3)





 