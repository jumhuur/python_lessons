# polymorphism
# waxa  laga wadaa in one method uu yeesho shaqooyin kala duwan sidan hoose oo kale 


# example
a = 2
b = 3
print(a + b) # 5  (+) => add

c = "o"
d = "k"
print(c+d) # ok (+) => concatinate


# example 2

items = ["a", "a", "b", "b"]
print(len(items)) # 4
name = "maxamad"
print(len(name)) # 7


# example 3

class Teacher:
    teachers = []
    def __init__(self, name, class_teacher):
        self.name = name
        self.class_teacher = class_teacher
    def new(self):
        new_teacher = {
            "name": self.name,
            "class_teacher" :self.class_teacher
        }

        Teacher.teachers.append(new_teacher)
        return f"new teacher is added"
    
    def do_more(self):
        print("do_more ...")
        raise NotImplementedError("waa in laga helaa dhamaan")


    @classmethod
    def __len__(cls):
        return f"Teachers count i {len(cls.teachers)}"


class Admin(Teacher):
    # admins = []
    def __init__(self, name, admin_title):
        self.name = name
        self.admin_title = admin_title
    def new(self):
        new_admin = {
            "name": self.name,
            "class_admin" :self.admin_title
        }

        Teacher.teachers.append(new_admin)
        return f"new admin is added"
        
    @classmethod
    def __len__(cls):
        return f"Teachers count i {len(cls.admins)}"

t = Teacher("maxamad", "4",)
a = Admin("jimcaale", "IT Team Manager")
print(Teacher("maxamad", "4",))
# print(t.new())
# print(a.new())
# print(len(Teacher.teachers))