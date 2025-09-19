# map

# Example 01
from functools import reduce


def formater(text):
    return f"--{text.strip().capitalize()}--"
texts = ["cimraan  " , "cabdilaahi" , "  ciise"]
formated = map(formater, texts)

for text in formated:
    print(text)



# Example 02
items = [["ss", "aa", 2020], {"name": "maxamad"}, 45, 77, 1.22,25.22, "nimcaan", (1,2,3)]
check = map(lambda item : f"{item} type is {type(item)}",items)
for ck in check:
    print(ck)



# filter


# Example 1
numbers = [41,11,2,45,78,96,63,100,451,1]
def filterNum(number):
    return number + number >= 100

data = filter(filterNum, numbers)
for result in  data:
    print(result)

# Example 2
small = [41,11,2,45,78,96,63,100,451,1]
print("*" * 30)
data = filter(lambda num : num + num <= 100, small)
for result in  data:
    print(result)

print("*" * 35)
listall = ["a", "12", "wew", 45,77,10,3.23]
for one in list(filter(lambda item : type(item) == int or  type(item) == float, listall)):
    print(one)


print("*" * 35)
# reduce

# Example 01

allnums = [44,2.50,44.23,25.12,2.02,45.55,14.78,45.98]

def sumall(num1, num2):
    return num1 + num2

reduced = reduce(sumall, allnums)
print(round(reduced,5))
print(reduced)