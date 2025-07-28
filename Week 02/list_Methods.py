# List Methods
list = [10,90,34,77,10,-34]
alph_list = [""]
newlist = [12,99]
print(list)
## append
# waxa uu ku  shayga xaga ugu danbeeya 
# hadaad u adeegsato list kalana waxa uu ka dhigaya 
# one element
list.append(150)
# list.append(newlist)
print(list)

#extend
listOne = ["a", "b", "c", "c", "c"]
listTwo = ["e", "f"]
listOne.extend(listTwo)
print(listOne)


# reverse
list.reverse()
print("reversed List", list)


#sort()
list.sort()
print(list)

# Sort With reverse
list.sort(reverse=True)
# hadii reverse ay tahay True 
# waxa u kala horaysiinaysaa siday  u kala badan yihiin 
# tusaale ahaan 120 waxaa ka soo horaynaya 121
print(list)
list.sort(reverse=False)
# hadii reverse ay tahay Flase 
# waxa u kala horaysiinaysaa siday  u kala Yar yihiin 
# tusaale ahaan 121 waxaa ka soo horaynaya 120
print(list)


## reverse()
# waxa uu kaga duwan yahay tii hore waxa uu kuu 
# kala tartiibin karaa 
# waxii xarfo ah sida names-ka oo kale iyo sidoo kale 
# waxii numbers ah 

TestReverse = [120,121,"A", "C", "B"]
TestReverse.reverse()
print(TestReverse) # ['B', 'C', 'A', 121, 120]







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







