a = 0 
while a < 15:
    print(a)
    a+= 1
print("loop is done")  # mar walba wuu daabac mayaa 


# waxba ma daabacayao waayo code0ka hoose waayo false waa false 
while False:
    print("daabac")
print("done")

fr = ["ma", "xu", "ci", "mu", "ni"]
print(len(fr)) # list length [5]

# loop list 
index = 0
while index  < len(fr):
    print(f"{str(index + 1).zfill(2)}-{fr[index]}")
    index += 1
else:
    print("All Fr is Printed")