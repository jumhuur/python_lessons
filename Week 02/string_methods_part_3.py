# istitle()
title_1 = "This Game Is 3D Game"
title_2 = "THI IS MY 3D GAME"
name = "jumhuur"
print(title_1.istitle()) # True
print(title_2.istitle()) # False
space = " "
space_1 = ""
print(space.isspace())
print(space_1.isspace())

#isupper()
print(title_1.isupper())
print(title_2.isupper())
#islower()
print(name.islower())
print(title_2.islower())
##isidenfire
# waxyaabaha aad ku hubin karto waxaa kamid
# inuu kuu hubiyo in variable sax ah uu yahay 

print("dsadsa".isidentifier())
print("223name".isidentifier())
##isalpha
# waxay  hubinaysaa in qoraalku yahay xuruuf kaliya 
# oo tusaale ahaan ka bilaab maysa A-Z
print(name.isalpha())
print(title_1.isalpha())
## isalnum
# Waxay hubinaysaa inay ka kooban yahay xaraf iyo lanbar
# sidan tusaale ahaan A-z and 1-9 oo kale
print(name.isalnum())
print(title_1.isalnum())
#replace(old value , new value , count)
name = "Jumhuur and taysiis online and online"
print(name.replace("online", "Website",1))
print(name.replace("and", "&", 2))
#join
list = ["maxamad", "dayib", "cabdi"]
print("-".join(list))
print("|".join(list))
print(",".join(list))



