name = input("What is your name?: ")
color = input("What is your favorite color?: ")
age = int(input("How old are you today?: "))

print("{} is {} years old and loves the color {}.".format(name.upper(), age, color.upper()))
print(name, "is", age, "years old and loves the color", color + ".", sep=" ")