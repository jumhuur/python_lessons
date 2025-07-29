# Week 02 String Methods

# Exercises 01
# Magac user ah oo leh faaruqyo badan.
username = "   Maxamad Dayib   "
print(username.strip())
# Soo saar magac nadiif ah.
# Output-ga la sugayo: "Maxamad Dayib"


# Exercises 02
name = "maxamad dayib"
print(name.upper())
# Soo saar magaca oo xaraf kasta waaweyn yahay.
# Output: "MAXAMAD DAYIB"

# Exercises 03
full_name = "Maxamad Dayib Cabdi"
print(full_name.split(" "))
# Kala saar magaca oo ku dar liis.
# Output: ['Maxamad', 'Dayib', 'Cabdi']


# Exercises 04
text = "Magacayga waa Maxamad Dayib"
print(text.replace("Dayib", "Ali"))
# Bedel "Dayib" adigoo ku beddelaya "Ali"
# Output: "Magacayga waa Maxamad Ali"


# Exercises 05
name = "Yuusuf Maxamed Ali"
print(name.endswith("Ali"))
# Hubi haddii magacu ku dhammaado "Ali"
# Output: True


# Exercises 06
full_name = "  maxamad DAYIB  "
print(full_name.strip().lower().title())
# Nadiifi labada daraf → ka dhig "Maxamad Dayib" (midka koowaad waa weyn, midka labaadna xaraf weyn kaliya)
# Output: "Maxamad Dayib"

# Exercises 07
text = "banana mango papaya"
print(text.count("a"))
# Soo saar inta jeer ee xarafka 'a' uu ku jiro.
# Output: 7


# Exercises 08
quote = "Knowledge is power"
print(quote.split()[0])
# Kala saar kelmada ugu horreysa oo kaliya (i.e., "Knowledge")
# Output: "Knowledge"



# Exercises 09
email = "student123@gmail.com"
print(email.split("@")[0])
# Soo saar kaliya qeybta ka horreysa '@'
# Output: "student123"


# Exercises 10
text = "My name is Maxamad Maxamad"
kal_saar = text.split(" ")
kal_saar.index("Maxamad", -1)
kal_saar[4] = "Dayib"
print(kal_saar)
print(" ".join(kal_saar))
# Bedel magaca labaad "Maxamad" → "Dayib"
# Output: "My name is Maxamad Dayib"






