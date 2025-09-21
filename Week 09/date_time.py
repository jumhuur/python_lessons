import datetime
# print(dir(datetime))
# print(dir(datetime.datetime))

# date now
print(datetime.datetime.now())
print("*" * 45)

# year
print(datetime.datetime.now().year)

# month
print(datetime.datetime.now().month)

# day
print(datetime.datetime.now().day)

print("*" * 45)

# star and End date 
print(datetime.datetime.min)
print(datetime.datetime.max)

print("*" * 45)

# print current Time
print(datetime.datetime.now().time())


# print current Time hour
print(datetime.datetime.now().time().hour)

# print current Time minute
print(datetime.datetime.now().time().minute)


# print current Time second
print(datetime.datetime.now().time().second)

print("*" * 45)

# start time and end time 
print(datetime.time.min)
print(datetime.time.max)

print("*" * 45)

# date gaara 
print(datetime.datetime(1998, 1,25))
print(datetime.datetime(2025,9,21,9,30,45,150364))
print("*" * 45)
dhalasho = datetime.datetime(1998, 1,25)
hada = datetime.datetime.now()
print(hada - dhalasho)

# Maalmaha kaliya
print((hada - dhalasho).days, end=" ")
print("days.")