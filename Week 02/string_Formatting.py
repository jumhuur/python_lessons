#-----------------------
#-String Formatting Old way
#-----------------------

name = "jumhuur"
age = 27
rank = 10

# print("My name is" + name + "and may age is" + age) # Type Error
print("My name is " + name + " and may age is " + str(age)) # concat

# Formatting with placeholders
print("My name is %s" % name)
print("may name is %s and may age is %d and may ranka is %f" % (name, age,rank))
print("My Rank is %.2f" % rank)
# trancate stringe
msg = "soo dhawaada dhamaan walalaha"
print("My Msg is %.12s" % msg)

#-----------------------
# -- String Formatting New way
#-----------------------
# Formatting with placeholders
print("My name is {}".format(name))
print("may name is {:s} and may age is {:d} and may ranka is {:f}".format(name, age,rank))
print("My Rank is {:.2f}".format(rank))
# trancate stringe
msg = "soo dhawaada dhamaan walalaha"
print("My Msg is {:.12s}".format(msg))

# rerange 
a = 1
b = 2
c = 3
print("welcome {:d} and {:d} and {:d}".format(a,b,c))  #welcome 1 and 2 and 3
print("welcome {2:d} and {1:d} and {0:.2f}".format(a,b,c))  #welcome 1 and 2 and 3
print(f"welcome {a}")
print(f"may name is {name} and may age is {age} and may ranka is {rank}")











