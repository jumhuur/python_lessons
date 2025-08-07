# while

# a = 1
# while a  <= 10:
#     print(a)
#     a += 1
# else:
#     print("Loop done")


# c = 0
# while c  < 10:
#     print(c)
#     c += 1
# print("Loop done")

# countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "soomaliland", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
# Students = ["raashid", "maxamad", "xasan", "nimcaan", "shukri", "najaax", "c/rashiid", "shucayb", "sayid cali", "taysiir"]
# print(len(Students))

# num = 0
# while num < len(Students):
#     print(f'{str(num + 1).zfill(2)}.-{Students[num]}')
#     num += 1
# print("all list is dispalyed")
# print("*" * 30)
# cont = 0
# while cont < len(countries):
#     print(f"{str(cont + 1).zfill(2)} - {countries[cont].rjust(int(len(countries[cont]) + 1),"@" )}" if countries[cont] == "soomaliland" else f"{str(cont + 1).zfill(2)} - {countries[cont]}")
#     cont += 1
# print(f"printed {len(countries)}")


# # book mark websites 
# websites = []
# countBook = 5
# DomainExtensions = [".com", ".net", ".dev", ".org", ".info", ".so", ".sa", ".ae"]
# while countBook > 0:
#     print("*" * 30)
#     web = input("whrite website name with out htpps:// ")
#     Extenstion = web.split(".")[1]
#     if str(f".{Extenstion}") in DomainExtensions:
#         print("sax")
#         fullweb = f"https://{web.strip().lower()}"
#         if fullweb in websites:
#             print("------ deplicate website not allowed sorry --------")
#             print(f" ❌ {fullweb} in list")
#         else:
#             websites.append(fullweb)
#             countBook -= 1
#             print("*" * 30)
#             print(f" ✔️   { fullweb} added thanks")
#             print(f"now you can added {countBook}")
#             if countBook < 1:
#                 print(f"your bookmark is full")
#     else :
#         print("you use wrong Extantion pleace use these extentions in blow")
#         index = 0
#         while index < len(DomainExtensions):
#             print(f"🔹 {DomainExtensions[index]}")
#             index += 1
# else:
#     index = 0
#     print("------ website list you added--------")
#     while index < len(websites):
#         print(f" {index + 1} -  ✔️  {websites[index]}")
#         index += 1



# passwor tries
tries = 4
password_user = '1234'
pass_tries = []

while tries > 0:
    print(f"waa markii ugu danbaysay" if tries == 1 else f"waxaa kuu hadhay {tries} isku day")
    password = input("whirte your password ").strip()
    if password != password_user:
        print(f"isku day mar kale!")
        tries -= 1

        if tries == 0:
            print("loop push list ")

    else:
        print("Password is correct ")
        break
    

else:
    print("loop is end")



