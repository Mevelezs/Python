data = {
    "name": input("\nWhat is your name?\n"),
    "Age": input("\nHow old you?\n")
    }


def age(num: str) -> str:
    num = int(num)
    if num >= 18:
        return "you are adult"
    else:
        return "you are younger"



print(f"Hello {data['name']}, your age is {data['Age']}, {age(data['Age'])}")
print(data)






