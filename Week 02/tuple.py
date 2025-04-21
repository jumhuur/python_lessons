# tuple Methods
my_tuple = ("maxamad", "jumhuur", 123,12.33, False)
print(my_tuple)

# tuple indexing 
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-4])

# anther way to white tuple in py 
new_tuple = "muuse", 123, False , True, 11.22
print(type(new_tuple))
print(type(my_tuple))

# you cant update
# new_tuple[0] = "python"
# print(new_tuple)  #'tuple' object does not support item assignment


# use tuple list methods
numbers = (1,2,3,4,5,6,7,8,9,9)

#tuple with one  element
oneElment1 = "mukhtaar"
oneElment2 = ("maxaamad")
print(type(oneElment1)) # <class 'str'>
print(type(oneElment2)) # <class 'str'>

#change to tuple 
oneElment1_1 = "mukhtaar",
oneElment2_2 = ("maxaamad",)
print(type(oneElment1_1)) # <class 'tuple'>
print(type(oneElment2_2)) # <class 'tuple'>

# len
print(len(oneElment1_1)) # 1
print(len(numbers)) # 9

# tuple concat

numbers_1 = 10,11,12,13

allnumb = numbers + (99,) + numbers_1
print(len(allnumb))
print(allnumb)

# tuple repeat as list and string
newlist = [12,13]
newstr = "22"
print(numbers_1 * 2)  # (10, 11, 12, 13, 10, 11, 12, 13)
print(newlist * 2) # [12, 13, 12, 13]
print(newstr * 2) # 2222

# count 
print(numbers.count(9))
print("number 9 in this list {1:d} and {0:d} pos".format(numbers.count(9), 10))

# index
print(newlist.index(13))
print(f"index is : {newlist.index(13)}")

# tuple descturc
a = ("100", "200", "300", 400)

one,two, three, _ = a
print(one)
print(two)
print(three)

