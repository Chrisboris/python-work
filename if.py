person = {"name": "Eli", "email": "a@ja.com", "number": 1234567}

all_contacts =[]
all_contacts.append(person)
print(all_contacts)


name = input("Enter name:")
while len(name) > 15:
     print("Long name")
     input("Re-enter name:")
email = input("Enter email:")
while "@" not in (email) and "." is not(email):
     email = input("Enter valid email:")
number = int(input("Enter number:"))
while len(str(number)) > 10:
  number = int(input("Invalid number. Re-enter phonenumber(10 digits):"))
while len(str(number)) > 10:
  number = int(input("Invalid number. Re-enter phonenumber(10 digits):"))




new_person = {"name": name, "email": email, "number": number}


all_contacts.append(new_person)


for x in all_contacts:
    print(x)