# Email_reg = \[A-z0-9\.]+@[a-z]+.\w{1,} 
# Email_reg1 = [A-z0-9\.]+@[a-z]+.(com|org|net)
# Website_reg = 

# ^(https?://)?(www\.)?(\w+\W?\w+).(net|com)$
# ^(?:https?://)?(?:www\.)?(?:\w+\W?\w+)\.(?:net|com)$


## Muhiim 
# hadii aad doonayso adoo groups adeegsanaya inaan loo cupcher garayn 
# group ahaan waxaad gruub walba hortii adeegsanaysaa ?: calamadaa


# examples

# search()  =>  waxaayna kuu soo celinaysaa match-ka ugu horeeya

import re

# Email_patt = r"[A-Za-z0-9\W?]+?[A-Za-z0-9]@[a-z]+.\w{1,}"
# mystring = re.search(Email_patt, "jumhuur123@gmail.com")
# print(mystring)

# testing


My_Testing = re.search(r"^(\d{3})(\s?|-?)(\d{2})(\s?|-?)(\d{7})$", "252-63-4114123")
print(My_Testing)
print(dir(My_Testing))
print(My_Testing.span()) # (0, 12)
print(My_Testing.string) # 252634645195
print(My_Testing.start()) # 0
print(My_Testing.end()) # 12
# print(My_Testing.regs) # ((0, 12),)
print(My_Testing.re)  # re.compile('^\\d{3}\\s?\\d{2}\\s?\\d{7}$') 
print(My_Testing.endpos) # 12
# print(My_Testing.expand("cali")) # cali
print(My_Testing.group()) #252634645195
print(My_Testing.groups()) # ('252', '', '63', '', '4645195')
print(My_Testing.lastindex)
print("*" * 45)
for index , group in enumerate(My_Testing.groups(), start=1):
    print(f"{index}) {group}")

# Example 2 check email
ValidWeb = re.findall(r"^(?:https?://)?(?:www\.)?(?:\w+\W?\w+).(?:net|com)$", "https://www.taysiir.com", re.VERBOSE)
# print(ValidWeb)

Mywbsites = []

if ValidWeb :
    for web in ValidWeb:
        print(web)
        Mywbsites.append(web)
        print(Mywbsites)

else:
    raise Exception("Fadlan Qor Website-sax!")

emails = []

def RegEmail():
    tray = 5
    while tray > 0:
        UserEmail = input("Your Email: ")
        Email_patt = r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.-]+(\.[A-Za-z]{2,})$"
        emailCheck = re.match(Email_patt, str(UserEmail.strip()))
        if emailCheck:
            emails.append(str(UserEmail).lower().strip())
            print("Your Email is valid")
            tray -= 1
            if len(emails) > 0:
                for index , email in enumerate(emails, start=1):
                    print(f"{index}: {email}")
        else :
            raise Exception("Your Email Is Not Valid")

# RegEmail()

print(dir(re.match))
Valid = re.match(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9]+(\.[A-Za-z]{2,})$", "j@gmail.com.net")
Valid2 = re.search(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9]+(\.[A-Za-z]{2,})$", "j@gmail.com.net")
print(Valid)
print(Valid2)



# split(pattern, string, maxsplit)
str_one = "Waxaan Jeclahay Luuqada Python"
searchstr = re.split(r"\s", str_one)
print(searchstr)  # meel kasta oo space ku jirto wuu ku lala jaray waxana uu ka dhigay ilaa  4 qaybood


# max split
str_two = "Waxaan Jeclahay Luuqada Python"
searchstr_1 = re.split(r"\s", str_two, maxsplit=1)
print(searchstr_1)
 

str_three = "Waxaan_Jeclahay#Luuqada-Python=Wayo"
searchstr_three = re.split(r"_|-|#|=", str_three)
print(searchstr_three)


# sub(pattern, rep, string , counreplays)
print(re.sub(r"\s", "-", str_two))
print(re.sub(r"\s", "-", str_two, 2))