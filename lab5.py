# take a single number in fizzbuzz
# divisible by 5 or 3, or both

value = int(input("Enter an integer value: "))

if value % 5 ==0 and value % 3 ==0:
    print("Fizz buzz")
elif value % 5 ==0:
    print("Buzz")
elif value % 3 ==0:
    print("Fizz")
else:
    print(value)