VOWELS = ("a", "e", "i", "o", "u") 
message = input("enter your message :")

new_message = ""
counter = 0

for letter in message:
    if letter not in VOWELS:
        new_message += letter 
    if letter in VOWELS:
        print(letter)
    counter +=1
    print (counter)
 
print(new_message)  