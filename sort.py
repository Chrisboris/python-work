list1 = ([1,2,3,4,5,6,7,8,9,10,'m','e','j','k'])

def list_sort(list1):
    even = []
    odd = []
    char = []
    # mydict = dict()

    for x in list1:
        if isinstance (x, int):
            if x % 2 == 0:
               even.append(x)
               even.sort() 
            else:
                odd.append(x)
                odd.sort() 
        elif isinstance (x, str):
            char.append(x)
            char.sort()
            char.sort(reverse=True)
    return {'evens': even, 'odd': odd, 'char': char, }

print(list_sort(list1))