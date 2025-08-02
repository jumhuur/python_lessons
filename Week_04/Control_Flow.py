# if elif else
# name = "maxamad"
# country = "Etho"
# Price = 100
# isstudent = False

# if country == "so" or country == "som":
#     print(f"soo dhawaaw {name}")
#     print(f"waxaad joogtaa {country}")
#     if isstudent == False:
#         print("Madaama aad tahay arday")
#         print(f"Qiimaha waa {Price - 20}")
#         print()
#     else :
#         print(f"Qiimaha waa {Price - 25}")

# elif country == "Etho"  or country == "djiboutii":
#     print(f"soo dhawaaw {name}")
#     print(f"waxaad joogtaa {country}")
#     if isstudent == False:
#         print("Madaama aad tahay arday")
#         print(f"Qiimaha waa {Price - 15}")
#         print()
#     else :
#         print(f"Qiimaha waa {Price - 10}")

# else :
#     print(f"soo dhawaaw {name}")
#     print(f"waxaad joogtaa {country}")
#     if isstudent == False:
#         print("Madaama aad tahay arday")
#         print(f"Qiimaha waa {Price - 0}")
#         print()
#     else :
#         print(f"Qiimaha waa {Price - 5}")


rate = 18
age = 22
print("This video is not suitable for you." if age < 18 else "This video is suitable for you.")




# ## membership
# # in 
# # not in 


# # str
# qoraal = "salaan"
# print("m"  in qoraal)
# print("m"  not in qoraal)

# # list
# saaxiibo = ["muuse", 'jimcaale', "daahir", "ciise", "xusen"]
# print("maxamad"  in saaxiibo)
# print("muuse"  in saaxiibo)
# print("daahir" not in saaxiibo)


admins = ["Mukhtaar", "Ismaaciil", "Ilhaan", "Hoodo", "Hadiya", "Nimcaan"]

# login
name = input("What is your name? ").strip().capitalize()

if name in admins:
    print("#" * 45)
    print(f"Welcome back, {name}!")
    print("Do you want to update or delete your name? [U/D]")
    
    option = input("Please type (U) to update or (D) to delete: ").strip().upper()
    
    if option == "D":
        admins.remove(name)
        print("#" * 45)
        print(f"The name '{name}' has been removed from the admin list. Thank you!")
    
    elif option == "U":
        print("#" * 45)
        newname = input("Please enter your new name: ").strip().capitalize()
        admins[admins.index(name)] = newname
        print("#" * 45)
        print("Here is the updated list of admins:")

        for index, admin in enumerate(admins, start=1):
            if admin == newname:
                print(f"{index} - {admin.rjust(len(admin) + 2, '*')}")
            else:
                print(f"{index} - {admin}")
    else:
        print("#" * 45)
        print("Invalid option. Please choose only 'U' or 'D'.")

else:
    print("#" * 45)
    print("You are not listed as an admin.")
    print("do you went to register your self ?")
    Options = input("choose yes or not [Y/N]").strip().capitalize()
    if Options == "Y":
        Newname  = input("Enter Your name ?").strip().capitalize()
        admins.append(Newname)
        print("wooow now you are admin")
        print("list of admins")

        for index,admin in enumerate(admins,start=1):
            if admin == Newname:
                print(f"{index} - {admin.rjust(len(admin) + 3, '@')}")
            else:
                print(f"{index} - {admin}")
    else:
        print("your choice is wronge")
        


