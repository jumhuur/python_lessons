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
    def __init__(self, name, class_):
        self.name = name
        self.class_ = class_

    @property   
    def new(self):
        new_teacher = {
            "name": self.name,
            "class_" :self.class_
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
    def __init__(self, name, admin_title,school, class_):
        super().__init__(self, class_)
        self.name = name
        self.admin_title = admin_title
        self.school = school
 

    @property
    def new(self):
        new_admin = {
            "name": self.name,
            "admin_title" :self.admin_title,
            "class_": self.class_
        }

        Teacher.teachers.append(new_admin)
        return f"new admin is added"
        
    @classmethod
    def __len__(cls):
        return f"Teachers count i {len(cls.admins)}"

t = Teacher("maxamad", "4",)
a = Admin("jimcaale", "IT Team Manager", "tog", "tt")
print(a)
print(t.new)
print(a.new)
print(len(Teacher.teachers))
print(a.class_)