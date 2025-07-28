# ---- set ------------
# -- set items are in close curly barces
# --- not indexing and not ordered
# --- set has ammutuble data types (number string,boolean, tuble)
# --- set items is unique

# set items are in close curly barces
new_set = {"maxamad", 12, 12.44, False, True, ("jumhuur", "name")}
print(type(new_set)) # <class 'set'>
print(new_set) # {False, True, ('jumhuur', 'name'), 'maxamad', 12, 12.44}

# not indexing 
# print(new_set[0]) # TypeError: 'set' object is not subscriptable

# not ordered
print(new_set)  # {False, True, 'maxamad', 12, 12.44, ('jumhuur', 'name')}
print(new_set) # {False, True, ('jumhuur', 'name'), 'maxamad', 12, 12.44}

# set can has only ammutuble data types (number string,boolean, tuble)

# Myset = {["jumhuur", "dayib"]} 
# Myset2 = {{"name": "maxamad"}} # TypeError: unhashable type: 'list' 
# print(type(Myset))
# print(Myset2) # unhashable type: 'dict



# set items is unique
setitems = {"jumhuur", "online", "jumhuur", "online", 1,1}
print(setitems) # {'jumhuur', 'online', 1}



#---------- set methods --------

# union
a = {1,2,3,4,5,6}
b = {7,8}
print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}

# add
b.add(9) # {8, 9, 7}
b.add(10) # {8, 9, 10, 7}
print(b)

# copy shalow copy 

c = a.copy()
print(c)  # {1, 2, 3, 4, 5, 6}


# remove
a.remove(1)
# a.remove(88) # KeyError: 88
print(a)

# discard
a.discard(2)
print("here",a)
a.discard(88) # not print Error

removed_element = a.pop()
print(removed_element)

# update
a.update(b)
print(a)

# clear()
a.clear()
print("set cleared",a)


# diffrance (set - set)
d = {1,2,3,4,5,6,"e","x"}
f = {1,2,3,"r","x"}

print("-------difference--------")
diff = d.difference(f)
print(d)
print(f)
print(diff)

# diffrance update

print("-------difference update--------")
# waxa u samaynayaa set-ka loo adeegsaday method-ka
# Original set ayuu ku ridayaa waxii farqi ah 
# isagoo ka saaraya waxii hore ugu jiray 
d.difference_update(f)
print(d)
print(f)


## intersection  (m & f)
# hadaad soo daabacdo waxa uu kuu siinayaa 
# elements-ku ay iskaga mid yiihiin sets-yadu

print("-------intersection--------")
m = {1,2,3,"f", "x"}
n = {2, 9,8,7, "o", "x"} 

inter = m.intersection(n)
print(m)
print(n)
print(inter)


# intersection_update
print("-------intersection_update--------")
# waxa u samaynayaa set-ka loo adeegsaday method-ka
# Original set ayuu ku ridayaa waxii iska mid yihiin 
# isagoo ka saaraya waxii hore ugu jiray 
w = {1,2,3,"f", "x"}
v = {2, 9,8,7, "o", "x"}
w.intersection_update(v)
print(w) # waxii asalka ahaa wu ka saaray kaliya waxa uu galiyay waxii ay iskaga mid ahaayeen
print(v)


# symmetric_difference
print("-------symmetric_difference--------")
T = {1,2,3,"f", "x"}
Q = {2, 9,8,7, "o", "x"}
sem = T.symmetric_difference(Q)
print(T) # waxii asalka ahaa wu ka saaray kaliya waxa uu galiyay waxii ay iskaga mid ahaayeen
print(Q)
print(sem)

# symmetric_difference_update
print("-------symmetric_difference_update--------")
T = {1,2,3,"f", "x"}
Q = {2, 9,8,7, "o", "x"}
T.symmetric_difference_update(Q)
print(T) # waxii asalka ahaa wu ka saaray kaliya waxa uu galiyay waxii ay iskaga mid ahaayeen
# print(Q)
# print(sem)

# issuperset
print("-------issuperset--------")
ee = {1,6,7,8}
rr = {4,3,1,6,7,8}
print(rr.issuperset(ee)) # True


# issubset
print("-------issubset--------")
ee = {1,6,7,8}
rr = {4,3,1,6,7,8}
print(ee.issubset(rr)) # True

# isdisjoin
print("-------isdisjoin--------")
ee = {1,6,7,8}
rr = {4,3,90,}
print(ee.isdisjoint(rr)) # True






