name = str(input("Enter any word: "))
answer = [name]
index = len(str)
while index > 0:
    answer += str(index - 1)
    index = index - 1
print(answer.reverse)