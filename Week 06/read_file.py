import os

print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# file info 
file = open("jumhuur.txt", "r")
print(file) # info object
print(file.name)
print(file.mode)
print(file.encoding)


#read file 
print(file.read())  # read all file
print(file.read(10)) # toban xaraf ugu horeeya file-ka

#line line ayay u akriyayaa
print(file.readline())
print(file.readline())


#hadaad tiro ku qorto waxa uu akhriyaay inta xaraf ee tirada ah 
print(file.readline(10))
print("*" * 30)

print(file.readlines())  # lines-kii oo array ah 
print("*" * 30)
# print(file.readlines(6)) # maan fahmin

for line in file:
    print(line)

    if(line.startswith("4-")):
        break


file.close()

