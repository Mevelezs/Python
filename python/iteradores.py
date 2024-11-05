fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
  print(f"this name is {fruit}")
  

print(len(fruits))

# range(init, length, increment)
for x in range(0, len(fruits), 1):
  print(f"0.{x + 1} fruit")


# recorriendo string
for i in "caracter":
  print(i, end="")