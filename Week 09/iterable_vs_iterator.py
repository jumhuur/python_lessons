# iterable waa shay kasta oo u kala qaad qaadi karto gaar gaar 
# sida (string , list , tuple dic , itc)


# ex
string = "Jumhuur"
for xaraf in string:
    print(xaraf, end=" ")


# ex
Mylist = [1,2,3,4,5,6,7,8,9]

for number in Mylist:
    print(number)

# Iterotar waa object loo adeegsado si  iterebal  iyadoo la adeegsanayo 
# method layidhaa next() kuuna soo celiya koba shay 
#  waxaad markaa adeegsan kartaa Iterator si shay shay aad ugu kala qaato
# shay iterbale ah adoo adeegsanaya iter()
# for loop hore ayay u adegsanaysaa iter() method behind the scene


# Ex
qoraal = "Muus"
# print(next(qoraal))  'str' object is not an iterator \
print("*"  * 45)
gen_iterebale = iter(qoraal)
print(next(gen_iterebale), end="\n") # M
print(next(gen_iterebale), end="\n") # u
print(next(gen_iterebale), end="\n") # u
print(next(gen_iterebale), end="\n") # s
print("*"  * 45)
# qaabka loop-ka 
for letter in iter(qoraal):
    print(letter)

print("*"  * 45)

i = 0 
gen_myiterable = iter(qoraal)
while i < len(qoraal):
    print(next(gen_myiterable))
    i+= 1



