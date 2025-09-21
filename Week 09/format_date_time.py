from datetime import datetime
# print(dir(datetime))
date = datetime.now()

# date formating  Sunday 21-September-2025
print(date.strftime("%A %d-%B-%Y"))

# date formating  Sun 21 Sep 25
print(date.strftime("%a %d %b %y"))

# date formating  Sun/21/Sep/25
print(date.strftime("%a/%d/%b/%y"))


# date formating  Sun,21,Sep,25
print(date.strftime("%a,%d,%b,%y"))



# formatting time


# 09:52:33 AM
print(date.strftime("%H:%M:%p"))
