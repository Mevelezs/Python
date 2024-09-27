avengersColors = {
  "Hulk": "Green",
  "Capitan America" : ["blue", "red"],
  "Iron man" : "red",
  "Black widow": "black",
  "Scarlet witch" : "Scarlet"
}

print(avengersColors)

# Accediendo al valor
print(avengersColors["Hulk"])

# Agregando
avengersColors["Thor"] = "Metalic";
print(avengersColors)

# reemplazando
avengersColors["Thor"] = ["rojo", "uru clolor"]
print(avengersColors)

# Eliminando
del avengersColors["Thor"]
print(avengersColors)

# Accediendo a un valor con get y retornando valor personalizado si no está
print(avengersColors.get("Thor", "El vengador mas fuerte no está"))
print(avengersColors.get("Iron man"))

# Iterando

for llave, valor in avengersColors.items():
  print(f"vengador => {llave} :: color => {valor}")
  