### Exercise 01
# ku daabac consolkaaga 5 data-type oo  kala duwan 
# adoo mid walba marka hore ku kaydinaya variable

My_int = 12
my_str = "jumhuur"
my_list = ["jumhuur", "cimraan", "khaalid"]
my_tuple = ("hargaysa", "burco", "berbera")
my_bool = True
my_dict = {"name" : "jumhuur", "age": 27}
my_set = {1,2,3,4,5,6}
print(type(My_int))
print(type(my_str))
print(type(my_tuple))
print(type(my_list))
print(type(my_bool))
print(type(my_dict))
print(type(my_set))



### Exercise 02
# code - kasta oo ka mida codes-kan so socda waxaa ku jira Error 
# waxaa lagaa doonayaa inaad ka dhigto mid saxa oo data- sax soo 
# celinaya

#code 1 
Myname = "jumhuur";
print(Myname)

#code 2 
Price = 90;
Price = 95;
print(Price)

#code 3 
UserName = "Maxamuud";
print(UserName)


### Exercises 03
# isticmaal Calaamadaha xisaabta ee aad soo baratay 
# si aad u hesho natiijada kuu qoran 
# calaamdna laba jeer ma soo noqon karto

print(23  - 10) # 13
print(88 + 88) # 176
print(13.90 * 89.09) # 1,238.351



### Exercise 04
# isticmaal calaamadaha isbarbar  dhiga (Comparison Operators) 
# si aad u soo saarto natiijada kuu qoran 
# calaamadana laba jeer ma soo noqon karto

print(23 > 10) # True
print(88 == 88) # True
print(80 <= 80) # True 


### Exercise 05

# waxaynu haysanaa web application kaliya waxaan u ogalnahay 
# inuu adeegsado qofka wata shuruudahan 
# - inuu yahay mid ka yar 18 sano da,diisu am uu yahay 18
# - Inuu haysto id ama Ama Uu Yahay Arday
# User kasta oo marka shuruudaa aan ka eego gudba oo True noqda 
# wuu adeegsan karaa kii kalana ma adeegsan karro waxan ku siiyay 
# 3 user kala cadee yaa gudbaya yaan gudbayn adoo shuurada eegaya

User1Age = 16;
User1Id = False;
User1IsStudent = True;
XaqiijintaadaUser1 = User1Age <= 18 and User1Id or User1IsStudent ;    # halkan ku qor qaabka aad u xaqiijinayso userka 
print(XaqiijintaadaUser1); # True

User2Age = 17;
User2Id = False;
User2IsStudent = False;
XaqiijintaadaUser2 = User2Age <= 18 and User2Id or User2IsStudent; # halkan ku qor qaabka aad u xaqiijinayso userka 
print(XaqiijintaadaUser2); # False

User3Age = 18;
User3Id = True;
User3IsStudent = False;
XaqiijintaadaUser3 = User1Age <= 18 and User3Id or User3IsStudent; # halkan ku qor qaabka aad u xaqiijinayso userka 
print(XaqiijintaadaUser3); # True


## Exercise 06

# Adoo adeegsanaya **Template Literals ku 
# daabac consol-kaaga fariintan meesha kuugu qoran** 
# - lama ogola variable cusub inaad samaysato
# - lama ogola inaad meel kale wax ku kaydiso aan ahayn variable-ka MSG

Price1 = 34.12;
Price2 = 12.66;
Msg = "Totalkaagu waa : {:.2f}".format(Price1 + Price2); 
print(Msg); # Totalkaagu waa 46.78$


### Exercise 07

# Adoo Adeegsanaya number methods-kii aad soo dhigatay 
# soo saar output ka kuu qoran
# meel kalena lama ogola in wax lagu qoro aan ahayn 
# console-ka dhexdiisa


mynumb = 90;
print(type(str(mynumb))); # string

Mystr = "90";
print(type(int(mynumb))); # Number

Views = "67450 Views";
print(Views.replace("Views", "")); # 67450


### Exercise 08

# soo saar Tirooyinka 
# laguu qoray ee output ka ah adoo ku qoraya 
# code-kaaga variabl-ka laguu calaamadiyay 
# - lama ogola variable cusub inaad samaysato
# - lama ogola inaad meel kale wax ku kaydiso aan ahayn variable-ka Result
import math
Lacag = 56.87;
Result = "{:d}".format(math.ceil(Lacag)) # code-kaaga halkan ku qor
print(Result); # 57

Result1 = math.ceil(Lacag); # code-kaaga halkan ku qor
print(Result1); # 57

Result2 = math.floor(Lacag); # code-kaaga halkan ku qor
print(Result2); # 56

Lacag = 56.87;
Result3 = round(Lacag, 1); # code-kaaga halkan ku qor
print(Result3); # 56.9


### Exercises 09

# Isticmaal index number si aad u soo saarto xarfaha output ka kuugu qoran
text = "Learning JavaScript is fun!";
print(text[9]); # J
print(text[3]); # r
print(text[23]); # f


### Exercise 10

# waxaad haysataa laba user labadaa user mid walba waxa uu haystaaa 

# lanbar iyo email waxaa la doonayaa inuu isticmaalo website-keena qofkii shuruudan laga hello 

# - inuu lanbarkiisu ka bilaabmayo 63
# - inuu haysto email ku dhamaanaya @hotmail.com

# labadaas shardi hadii laga hello waa true waan fasaxaynaa 

# hadii kale waa false adeegso methods ka casharkan iyo waxyaabihii cahsaradii hore


User1Phone = "4645195";
User1Email = "jumhuur123@hotmail.com";
result = User1Phone.startswith("63") and User1Email.endswith("hotmail.com"); # halkii waxii checkgarayn ah ku qor
print(result);
User2Phone = "634818197";
User2Email = "js@hotmail.com";
result2 = User2Phone.startswith("63") and User2Email.endswith("hotmail.com"); # halkii waxii checkgarayn ah ku qor
print(result2);


