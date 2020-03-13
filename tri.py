vowels = ("a","b","c","d","e")
message = input("enter anyword: ")

new_message = ("")

for letter in message:
    if letter not in vowels:
        new_message += letter
    if letter in vowels:
        print(letter, "is a vowel,")

print(new_message)