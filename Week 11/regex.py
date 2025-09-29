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

# Email_patt = r"[A-z0-9\.]+@[a-z]+.\w{1,}"
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
ValidWeb = re.findall(r"^(?:https?://)?(?:www\.)?(?:\w+\W?\w+).(?:net|com)$", "https://www.taysiir.com")
# print(ValidWeb)

Mywbsites = []

if ValidWeb :
    print(ValidWeb)
    for web in ValidWeb:
        print(web)
        Mywbsites.append(web)

else:
    raise Exception("Fadlan Qor Website-sax!")


