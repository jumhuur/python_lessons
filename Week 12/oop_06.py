# inheritance
class Food:
    def __init__(self, name,price, cat):
        self.name = name
        self.price = price
        self.cat = cat
    def Eat(self):
        print(f"Eat From Food class an food is {self.name}")
    

class Apple(Food):
    def __init__(self,name,price, cat):
        super().__init__(name, price, cat)
        print(f"Eat From Apple class an food is {self.name}")
    def geed(self):
        print(f"Geedka waxaan ka helay {self.name} and Price is {self.price}")


# instance
Food_1 = Food("canbe", "254", "Food")
Food_2 = Apple("apple", 110, "Food")

# usage
Food_1.Eat()
Food_2.Eat()
Food_2.geed()



# multiple inheritence

from random import random, randint
class Baseone():
    def __init__(self):
        pass
    def random_int(self):
        print(randint(1,23))



class Basetwo():
    def __init__(self):
        pass
    def random_floot(self):
        print(random())

class Farac(Basetwo, Baseone):

    pass


print("*" * 40)
intance = Farac()

intance.random_floot()
intance.random_int()

# print(dir(Farac))
print(Farac.mro())
