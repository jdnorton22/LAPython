message = input("Enter a message: ")

print("Lowercase: ", message.lower())
print("Uppercase: ", message.upper())
print("Capitalized: ", message.capitalize())
print("Title Case: ", message.title())

words = message.lower().split()
print("Words: ", words)

sorted_words = sorted(words)
print("Sorted words: ", sorted_words)
print("Alphabetic last word: ", sorted_words[-1])