# append
# 👉 Waxay ku darsataa element cusub dhamaadka list-ka.
ls = ["Maxamd", "Dayib", 25, 25, 25, True, False]
print(ls)
ls.append("yuusuf")
print(ls)

# inser(index, item)
# 👉 Waxay ku darsataa item meel gaar ah oo index ah.
ls.insert(0, "ALI")
ls.insert(-1, "Taysiir online")
print(ls)


## extend(iterable)
# 👉 Waxay ku darsataa dhammaan element-yada liis kale ama iterable kale.
ls1 = [1,2,3,4,5,6]
ls.extend(ls1)
print(ls)

## remove(item)
# 👉 Waxay ka saartaa item-kii ugu horeeyay ee la helay list-ka.
ls.remove(25)
print(ls)


# # pop(,index)
# hadaad index siin waxay saaraysaa ka ugu danbeeya 
# hadii index la siiyana waxay saaraysa ka ugu 
#  horeeya
removed = ls.pop()
removed2 = ls.pop(0) # hada index-ka 0 element-ga ku jira ayay saaraysaa
print(removed)
print(removed2)
print(ls)

# index(item)
# 👉 Waxay soo celisaa index-ka item-ka ugu horeeya ee list-ka.
print(f" waa index-ka {ls.index(True)}")


## count(item)
# 👉 Waxay tirisaa inta jeer ee item-ku ku jiro list-ka.
print(ls.count(25))


## sort
# 👉 Waxay u kala hormarisaa list-ka sida la kala weyn yahay (default: Ascending).
numbers = [10,56,77,-34,00,-100,123]
numbers.sort()  
print(numbers)
# Haddii aad rabto descending:
numbers.sort(reverse=True)  
print(numbers)

## reverse
# 👉 Waxay dib u rogtaa list-ka (ma ahan kala hormarin).
numbers.reverse()
print(numbers)

# # copy()
# 👉 Waxay sameysaa nuqul cusub oo list-ka ah (copy gaar ah, maaha reference).
alllist = numbers.copy()
print(alllist)



## len
# 👉 waxa uu ku siinayaa inta items ee liiskaaga  ka kooban yahay 
print(len(ls))

## clear
# 👉 Waxay tirtirtaa dhammaan element-yada list-ka.
ls.clear()
print(ls) # []


## slicing 
#👉 Waa maxay slicing?
#Slicing waa hab aad qayb uga goyn karto list (ama string) adigoo isticmaalaya [:] syntax.
# list[start:stop:step]

numbers = [10, 20, 30, 40, 50, 60]

#🎯 1. Qayb ka bilowso index 1 ilaa 3
qaybt1 = numbers[1:3]
print(numbers)
print(qaybt1)

#🎯 2. Ka bilaab bilowga ilaa index 2
print(numbers[0:3])

#🎯 3. Ka bilaab index 2 ilaa dhammaad
print(numbers[2:])

#🎯 4. Copy liiska oo dhan
print(numbers[:])

#🎯 5. Bood 2 kasta
print(numbers[::2]) # ?


#🎯 6. Rog liiska (reverse)
print(numbers[::-1])

#🔄 QAYBTA 2: Nested Lists
#👉 Waa maxay nested list?
#Nested list waa liis ku jira liis kale. Waxaa loo isticmaalaa in lagu kaydiyo xog is dhexgal ah sida tiirar iyo safaf (rows and columns).

#✅ Tusaale guud:
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
#🎯 1. Hel row-ga labaad
print(matrix[1])  # [4, 5, 6]
#🎯 2. Hel item-ka 5
print(matrix[1][1])  # 5
#🎯 3. Hel item-ka 9
print(matrix[2][2])  # 9
#🎯 4. Dhex gal liis nested ah:
data = ["name", [1, 2, 3], True]
print(data[1][0])  # 1










