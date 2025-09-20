# user input

fname = input("magacaa 1aad")
mname = input ("magac labaad")
lname = input("magaca 3aad")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()
print(f"soo dhawaaw {fname} {mname:.1s} {lname}")



# slice Email
thename = input("Your name ? ").strip().capitalize()
theemail = input("Your Email ?").strip()

theusername = theemail[:theemail.index("@")]
thewebsite = theemail[theemail.index("@") + 1:]

print(f"soo dhawaaw {thename} \nyour email is {theemail} \nyour username is {theusername} \nand your website is {thewebsite} ")


# Practical Your age
age = int(input("Whats Your age ? "))
# age = int(age)
# print(age)
# print(type(age))

bilo = age * 12
wiig = bilo * 4
maalmo = age * 365
saacado = maalmo * 24
daqiiqado = saacado * 60
sikino = daqiiqado * 60

print("Waxaad Noolayd :")
print(f"{bilo} Bil")
print(f"{wiig:,} wiig")
print(f"{maalmo:,} maalmo")
print(f"{saacado:,} saacado")
print(f"{daqiiqado:,} daqiiqado")
print(f"{sikino:,} sikino")




