# List Methods
list = [10,90,34,77,10,-34]
alph_list = [""]
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
listOne = ["a", "b", "c", "c", "c"]
listTwo = ["e", "f"]
listOne.extend(listTwo)
print(listOne)

# remove
listOne.remove("a")
print(listOne)

# copy
coped_list = listOne.copy()
listOne.append("cali")
print(coped_list)
print(listOne)

# count 
print(listOne.count("c"))
print(coped_list.count("a"))

# index
print(listOne.index("c"))
print(listOne.index("cali"))

#insert
listOne.insert(0, "online")
listOne.insert(-1, "dugsiiye")
print(listOne)

#pop
removed = listOne.pop(1)
print("Waxaa la saaray",removed)


# clear
listOne.clear()
print(listOne)



list = [1,2,3,4]
list[len(list) - 1] = 10;
print(len(list)) # ?







