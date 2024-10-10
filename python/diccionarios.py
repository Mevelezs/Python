avengersColors = {
  "Hulk": "Green",
  "Capitan America" : ["blue", "red"],
  "Iron man" : "red",
  "Black widow": "black",
  "Scarlet witch" : "Scarlet"
}

print(avengersColors)
print("\n --> Obteniendo keys")
print(avengersColors.keys())

print("\n --> Obtenienvdo values")
print(avengersColors.values())

print("\n --> Obtenienvdo el tamaño")
print(len(avengersColors))

print("\n --> Accediendo al valor")
print(avengersColors["Hulk"])

print("\n --> Agregando")
avengersColors["Thor"] = "Metalic";
print(avengersColors)

print("\n --> reemplazando")
avengersColors["Thor"] = ["rojo", "uru color"]
print(avengersColors)

print("\n --> Eliminando")
del avengersColors["Thor"]
print(avengersColors)

print("\n --> Accediendo a un valor con get y retornando valor personalizado si no está")
print(avengersColors.get("Thor", "El vengador mas fuerte no está"))
print(avengersColors.get("Iron man"))

print("\n --> Iterando")
for llave, valor in avengersColors.items():
  print(f"vengador => {llave} :: color => {valor}")

print("\n --> Uniendo dos diccionarios")
dic1 = {"uno": 1, "dos": 2}
dic2 = {"tres":3, "cuatro":4}

dic3 = dic1 | (dic2)
print(dic3)

print("\n --> Desestructurando para obtener los valores")
dic4= {**dic1, **dic2}
print(dic4)

print("\n --> Actualizando el valor de uno con el otro")
dic1.update(dic2)
print(dic1) # si las clave son iguales el valos se reemplaza
