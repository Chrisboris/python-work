VOWELS = ("a", "e", "i", "o", "u") 
message = input("enter your message :")

new_message = ""
counter = 0

for letter in message: 
    if letter in VOWELS:
        if letter in new_message:
                counter = counter+1
        else: new_message += letter        
result =(new_message, counter)
print(result)
#         counter +=1
# print (counter)

    
 
# print(new_message)  
# coordinates = (4,5,4)
# coordinates[2] =
# print(coordinates)