vowels=("a","e","i","o","u")
message = input("ANY WORD:")

New_message = ""

for letter in message:
    if letter not in vowels:
        New_message += letter
    if letter in vowels:
        print(letter, "is a vowel,")

print(New_message)            