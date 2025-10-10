# Every thin in python is an Object


from doctest import SkipDocTestCase


name  = "Maxamad"  
age = 45
print(age.__class__) # <class 'int'>
print(int.to_bytes(age, 3))
print(name.__class__) # <class 'str'>
print(str.upper(name))
# print(dir(int))


# __class__ = waxa uu kuu sheegayaa instance walba calss-ka uu ka tirsan yahay
#__str__ = wax la akhriyayo ayay kuu soo daabacaysaa 
#__len__ = len() ayay la shaqayanaysaa hadii la adeeegsado

class Sako_Api:
    
    def __init__(self):
        self.sakwaat = ["lacag", "Dahab", "Fido", "Geel", "Adhi", "lo'a"]
    def __str__(self):
        return f"{self.sakwaat}"
    def __len__(self):
        return len(self.sakwaat)

sako = Sako_Api()
print(sako)
print(sako)
print(len(sako))
sako.sakwaat.append("alaab")
sako1 = Sako_Api()
print(len(sako))