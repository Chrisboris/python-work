x = input("enter list 1:")
y = input("enter list 2: ")

comb = len(x) + len(y)
if comb % 3 == 0 and comb % 5 == 0:
    print("fizzbuzz")
elif comb % 3 == 0:
        print("Fizz")
elif comb % 5 == 0:
        print("Buzz")
else:
    print(comb)                      




        