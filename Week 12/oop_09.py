from abc import ABC , abstractmethod
class Animal(ABC):


    @abstractmethod
    def make_sound():
        pass



class Dog(Animal):
    def make_sound(self):
        return "woow"
    def make_action(self):
        return "runing ...."


class Cat(Animal):
    def make_sound(self):
        return "meaw"
    def make_action(self):
        return "jumping ...."


dog = Dog()
cat = Cat()



if __name__ == "__main__":
    print(dog.make_sound())
    print(dog.make_action())

    print(cat.make_sound())
    print(cat.make_action())
else:
    print("lama ogola")



