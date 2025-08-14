#----------buil in function --------------------
# all | dhamaan waxa list  ku jiraa haday yihiin True
# any | dhamaan waxa list ku jiraa haday yihiin false
# bin | binery langu
# id  | value id in momry 
# sum(iterable, start)
# round()
# range()
# print()
# abs(number)
# pawer(base, exponent , modules)
# min(items || iterebale)
# max(items || iterebale)
# slice(start, end, step)
# -----------------------------------------



# all
x = [1,2,3,4,5,6]  # true all
d= [1,2,3,4,5,False]  # true all

if all(d):
    print("dhamaan waa True")
else:
    print("waxaa ku jira shay Flase ah ")


# any
a = [0,False, []] # dhamaan false
a = [0,True, []] # dhamaan false

if any(a):
    print("waxaa ku jira ugu yaraan xabad True ah")
else:
    print("wax True ah kuma jiraan")


# bin

n = 4645195
print(bin(n))

# id 
k = 1
j = 2

print(id(k))
print(id(j))

# sum
princes = [10.23,44.12,22.3,10.99,9.33]
princes1 = [10.50,15.50]
print(sum(princes))
print(sum(princes1))

# round()

print(round(4.55))
print(round(4.49))

print(round(14.25564654545, 2))
print(round(14.25564654545, 3))


# range(start, end, step)
print(list(range(0))) # []
print(list(range(0,5))) # [0, 1, 2, 3, 4]
print(list(range(1,46, 2)))


# print(end="\n")  default
print("soo dhawaaw maxamad")
print("soo","dhawaaw", "maxamad") 
print("soo","dhawaaw", "maxamad" , sep=" % ")
print("soo","dhawaaw", "maxamad", end="\n")
print("soo","dhawaaw", "maxamad", end=" ")
print("salaan")
print("soo","dhawaaw", "maxamad", end="#")

# abs()
print(abs(100))
print(abs(-100))
print(abs(95))
print(abs(-95))

# pawer(base, exponent , modules)
print(pow(2, 5)) # 32
print(pow(2, 5, 10)) # 2 = (2*2*2*2*2) % 10

mytuble = (45,78,88,-78,-566)
# min(items || iterebale)
print(min(mytuble))
# max(items || iterebale)
print(max(mytuble))

# slice(start, end, step)

students = ("maxamad", "cigaal", "luqmaan", "yaasir")
print(students[slice(2)])
print(students[slice(1,2)])
print(students[slice(0,len(students),2)])