def is_adult(age: int) -> None:
    if 0 < age < 18:
        print(f"The person with {age} years is younger")
    elif age >= 18:
        print(f"The person with {age} years is adult")
    else:
        print(f"The person with {age} year don't exist")


number = 20
is_adult(number)

print("a" == "b")
print(not "a" == "b")
print("a" != "b")

fruits = ['apple', 'banana', 'cherry']

if "cherry" in fruits:
    print("Yes, it is")
else:
    print("No, it doesn't")
