man = {"name": "Bernard", "email": "kibuddessali@gmail.com", "number": "0704045674"}

all_contact = []
all_contact.append(man)
print(all_contact)

name = input("Enter name: ")
while len(name) > 15 or len(name) < 3:
    name = input("invalid name.  Re-enter name")
email = input("Enter email: ")
while "@" not in (email) and "." is not (email):
    email = input("invalid. Re-enter email: ")
number = input("Enter mobile number: ")
while len(number) > 10:
    number = input("invalid. Re-enter number: ")

new_contact = {"name": name, "email": email, "number": number}

all_contact.append(new_contact)

print(all_contact)