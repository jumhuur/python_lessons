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

## clear
# 👉 Waxay tirtirtaa dhammaan element-yada list-ka.
ls.clear()
print(ls) # []






