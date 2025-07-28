# lists
mylist = ["a", "b", "c", 12.00, False]
print(mylist)
# index accessing 
print(mylist[0])
print(mylist[-1])
print(mylist[-3])

# slice lists
print(mylist[1:4])
print(mylist[:2])
print(mylist[3:])

## slice lists with steps
# kani waxa uu ka boodayaa mid
print(mylist[0::1])
# kana waxa uu ka boodayaa 2 element
print(mylist[0::2])
# kana waxa uu ka boodayaa 3 element
print(mylist[0::3])

# update lists
mylist[0] = "jumhuur"
print(mylist)
mylist[-1] = True
print(mylist)

# multible updates
mylist[0:3] = []
print(mylist)
mylist[0:2] = ["taysiir", "online"]
print(mylist)
