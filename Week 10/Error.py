x = 22

if x <= 0:
    # print("waa in lanbarku ka waynaadaa 0")
    raise Exception("waa in lanbarku ka waynaadaa 0")
print("sii socodka barmaamijka")

y = 78

if type(y)  != int:
    raise ValueError(f"Waxaa La Doonayaa Number '{y}' maaha Lanbar")

print("sii wad hawsha kale")


# number = int(input(""))
# print(number)

try:
    number = int(input("Qor da'da:"))
    # print(maxamad)
    print(number)
except ValueError:
    print(f"Waxaa Lagaa Doonayaa Lanbar ")
except NameError:
    print("waxaa jira Magac aan la aqoonsan ")
except:
    print("Error Ayaa Dhacay")
# else:
#     pass
# finally:
#     print("Mar walba")



# Example 

passwords = [122454545, 96875454, 2544788, 99774411]
iskuday = 5
while iskuday > 0:
    try:
        Value = int(input("Passord:"))
    except ValueError:
        iskuday -=  1
        print("Passwor-ka aad Qoraysaa waa inuu lanbaro noqdo")
        if iskuday > 0:
            print(f"waxaa kuu Hadhay {iskuday} Jeer")
        continue

    if Value in passwords:
        print("Welcome to your Account")
        break
    else:
        iskuday -= 1
        print("PassworD-kaagu waa Qalad")
        if iskuday > 0:
            print(f"Waxaa Kuu Hadhay {iskuday} Jeer")
else:
    print("waxaad isku dayday 5 jeer Macasalaama")



