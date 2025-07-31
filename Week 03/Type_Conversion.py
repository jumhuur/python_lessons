# Type Conversion
a = 10 # int
b = "10" # string
c = 10.0 # floting
d = ["maxamad", 12, False] # list
e = {"muuse", "ayaan", "cali"} # set
f = ("784",44,55,66,77,)  # tuple
j = {"name": "maxamad", "age": 45} # dict
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(j))


# convert

# tuple 
# print(tuple(a)) # TypeError: 'int' object is not iterable 
print(tuple(b)) 
# print(tuple(c))TypeError: 'float' object is not iterable 
print(tuple(d))
print(tuple(e))
print(tuple(f))
print(tuple(j))


# list
#print(list(a)) # TypeError: 'int' object is not iterable 
print(list(b)) 
#print(list(c)) #TypeError: 'float' object is not iterable 
print(list(d))
print(list(e))
print(list(f))
print(list(j))

print("*" * 30)
# set
#print(set(a)) # TypeError: 'int' object is not iterable 
print(set(b)) 
#print(set(c)) #TypeError: 'float' object is not iterable 
print(set(d))
print(set(e))
print(set(f))
print(set(j))


print("*" * 30)
# dict
#print(dict(a)) # TypeError: 'int' object is not iterable 
#print(dict(b))  # ValueError: dictionary update sequence element #0 has length 1; 2 is required
#print(dict(c)) #TypeError: 'float' object is not iterable 
# print(dict(d)) # ValueError: dictionary update sequence element #0 has length 7; 2 is required
# print(dict(e)) # ValueError: dictionary update sequence element #0 has length 7; 2 is required
# print(dict(f))
print(dict(j))

# waxaa suura galk in tuple list  uu badalo
# waa hadii key iyo value wax u dhigma la hello sidan hoose oo kale 

test1list = [["name", "maxamad"], ["age", 20]]
test1tuple = (("name", "maxamad"), ("age", 20))
print(dict(test1list))







