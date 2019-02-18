def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        print("OLI MUSIRU NNYO ")
    else:
        return number *  factorial(number - 1) 
print(factorial(3))


