import oop_09

class Class01():
    def __init__(self, name, age, job):
        self._name = name # protected
        self._age = age # protected
        self.__job = job # private

class Class02(Class01):
    def __init__(self):
        super().__init__(self)
    pass

c_01 = Class01("cali", 12, "python developer")

print(c_01._age)
print(c_01._name)