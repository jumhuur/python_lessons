# dict
my_dict = {
    "name": "Jumhuur", 
    "age":27, 
    "Skills": ["Html", "Css", "Js", "Python"]
}
print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())

# print values
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["Skills"])

# neted dict
Luuqado = {
    "One": {
        "name": "Html",
        "Progress": "87%"
    },
    "two": {
        "name": "Css",
        "Progress": "97%"
    },
    "three": {
        "name": "js",
        "Progress": "76%"
    }
}

print(Luuqado)
print(Luuqado["One"])
print(Luuqado["One"]["name"])
print(Luuqado["One"]["Progress"])


# anthar way 

Html = {
    "name": "Html",
    "Prog": "90%",
    "Pro": "3"
}

Css = {
    "name": "Css",
    "Prog": "87%",
    "Pro": "3"
}

Js = {
    "name": "js",
    "Prog": "80%",
    "Pro": "2"
}


skills = {
    "One": Html,
    "Two": Css,
    "Three": Js
}

print("My Skills",skills)
print(skills["One"]["name"])
print(skills["Three"]["name"])

# --------- dict methods ------

# leng
print(len(skills))
print(len(skills["Three"]))

# update
skills.update({"four": "footboll"})
print(skills)

# you can update with out update method
skills["five"] =  "cooking";
print(skills["five"])

# copy
thebest = Luuqado.copy()
print("thebest",thebest)


# setdefault
skills.setdefault("five", "internet") # waxba ma soo kordhin laakiin hadii wax key-gaas wata la waayo isagaa meesha soo galayaa
skills.setdefault("six", "documentry") # maadaama aanu jirin mid cusub ayuu soo kordhiyay
print("*" * 25)
print(skills)


#popitem
print(skills.popitem()) # shaygii ugu danbeeyay ee lagu daray

# items
print("*" * 25)
print(skills.items())


# fromkeys
keys = ("A", "B", "C")
values = "taysiir"
print("*" * 25)
user = {

}.fromkeys(keys,values)
print(user)
print(dict.fromkeys(keys,values))

# clear
skills.clear()
print(f"clear Skills Dict {skills}")