div = int(input("Enter a number of your choice: "))

if div % 3 == 0 and div % 5 == 0:
    print("fizzbuzz")
elif div % 3 == 0:
    print("fizz")
elif div % 5 == 0:
    print("buzz")
else:
    print(div)
