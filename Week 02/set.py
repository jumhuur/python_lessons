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

