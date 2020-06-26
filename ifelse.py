if 'a' > 'b':
    print("A is larger")
elif 'b' > 'a':
    print("B is larger")
else:
    print("They were equal?")

name =input("What is your name?: ")
if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("Your name is 5 characters")
elif len(name) >=4:
    print("Your name is 4 characters")
else:
    print("Your name is short")
