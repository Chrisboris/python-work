base = int(input("Enter base : "))
power = int(input("Enter power: "))


def pow(base,power):
    result = 1
    for x in range(power):
        result = result*base
    return result

print(pow(base,power))