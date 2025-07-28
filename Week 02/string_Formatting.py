#-----------------------
#-String Formatting Old way
#-----------------------

name = "jumhuur"
age = 27
rank = 10

# print("My name is" + name + "and may age is" + age) # Type Error
print("My name is " + name + " and may age is " + str(age)) # concat

## Formatting with placeholders
# waxaan adeegsan doontaa sadex qaab oo kala ah sidan hoose
# %s => string (waxii qoraal ah )
# %d => number (waxii number ah sida 10 11 63)
# %f => floting  waxii number ah laakiin wata jajab sida (1.20, 889.20 0.33)
print("My name is %s" % name)
print("may name is %s and may age is %d and may ranka is %f" % (name, age,rank))

#3 control foating point number
# hakii uu qorayay zero badan waxaad ku xukumi kartaa 
# kaliya inta aad doonayso sidan hoose oo kale 
# waxaan ku xukunay inuu adeegsado Lba Zero oo kaliya
print("My Rank is %.2f" % rank)
print("My Rank is %.1f" % rank)
# trancate stringe
msg = "soo dhawaada dhamaan walalaha"
print("My Msg is %.12s" % msg)

#-----------------------
# -- String Formatting New way
#-----------------------
## Formatting with placeholders
# markaad adeegsanayso qaabka waxaan u kala qaybin kartaa 
# data-dada noocyo kala duwan sidan hoose oo kale 
# {:s}  => string 
# {:d} => number
# {:f} => floating

print("My name is {}".format(name))
print("may name is {:s} and may age is {:d} and may ranka is {:f}".format(name, age,rank))
print("My Rank is {:.2f}".format(rank))
# trancate stringe
msg = "soo dhawaada dhamaan walalaha"
print("My Msg is {:.12s}".format(msg))

# rearange 
a = 1
b = 2
c = 3
print("welcome {:d} and {:d} and {:d}".format(a,b,c))  #welcome 1 and 2 and 3
print("welcome {2:d} and {1:d} and {0:.2f}".format(a,b,c))  #welcome 1 and 2 and 3
print(f"welcome {a}")
print(f"may name is {name} and may age is {age} and may ranka is {rank}")











