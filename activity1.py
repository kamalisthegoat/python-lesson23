number1 = [1, 2, 3]
number2 = [4, 5, 6]
result = map(lambda x, y: x + y, number1, number2)
print("addition of 2 list")
print(list(result))

nums = [1, 2, 3, 4, 5]
def sq(n):
    return n*n

sqaure = list(map(sq, nums))
print("sqaure of numbers in list")
print(sqaure)