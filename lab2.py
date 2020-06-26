user_input=input("Enter a random string: ")

print("The first character is: {}".format(user_input[0]))
print("The last character is: {}".format(user_input[len(user_input)-1]))
print("The middle character is: {}".format(user_input[int(len(user_input)/2)]))

print("The even characters are: {}".format(user_input[0::2]))
print("The odd characters are: {}".format(user_input[1::2]))

print("The reverse string is: {}".format(user_input[::-1]))