# dict Exercises

# Exercise 01
student = {"name": "Ali", "age": 20}
print(student.get("age"))
# Isticmaal get() si aad u hesho da'da (age)
# Output: 20

# Exercise 02
student2 = {"name": "Ali", "age": 20}
print(student2.get("email"))
# Isticmaal get() si aad u hesho email, haddii uusan jirinna waa in uu noqdaa None
# Output: None



# Exercise 03
student3 = {"name": "Ali", "age": 20, "country": "Somalia"}
print(student3.keys())
# Soo saar furayaasha (keys)
# Output: dict_keys(['name', 'age', 'country'])


# Exercise 04
student4 = {"name": "Ali", "age": 20}
print(student4.values())
# Soo saar qiimaha (values)
# Output: dict_values(['Ali', 20])


# Exercise 05
a = {"name": "Ali"}
b = {"age": 21, "city": "Mogadishu"}
a.update(b)
print(a)
# Ku dar b → a adigoo isticmaalaya update()
# Output: {'name': 'Ali', 'age': 21, 'city': 'Mogadishu'}



# Exercise 06
info = {"name": "Ali", "age": 22, "city": "Hargeisa"}
info.pop("age")
print(info)
# Ka saar "age" adigoo isticmaalaya pop()
# Output: {'name': 'Ali', 'city': 'Hargeisa'}



# Exercise 07
data = {"a": 1, "b": 2, "c": 3}
data.popitem()
print(data)
# Isticmaal popitem() si aad u saarto item random ah
# Output: mid random ah wuu baxayaa



# Exercise 08
user8 = {"username": "admin"}
user8.setdefault("email", "None")
print(user8)
# Isticmaal setdefault() si aad ugu darto "email" haddii uusan jirin
# Output: {'username': 'admin', 'email': None}



# Exercise 09
user9 = {"name": "Maxamad", "role": "admin"}
print(user9.items())
# Soo saar dhammaan items-ka (key-value pairs)
# Output: dict_items([('name', 'Maxamad'), ('role', 'admin')])



# Exercise  10
settings = {"theme": "dark", "volume": 80}
settings.clear()
print(settings)
# Isticmaal clear() si aad u nadiifiso dictionary-ga
# Output: {}
