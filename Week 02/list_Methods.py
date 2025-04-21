# List Methods
list = [10,90,34,77,10,-34]
newlist = [12,99]
print(list)

# append
list.append(150)
# list.append(newlist)
print(list)
#sort()
list.sort()
print(list)

# Sort With reverse
list.sort(reverse=True)
print(list)
list.sort(reverse=False)
print(list)

# reverse
list.reverse()
print("reversed List", list)

#extend
listOne = ["a", "b", "c"]
listTwo = ["e", "f"]
listOne.extend(listTwo)
print(listOne)

# remove
listOne.remove("a")
print(listOne)

