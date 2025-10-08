class Member:
    def __init__(self, f_name, l_name, age, gen, job):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gen = gen
        self.job = job

    def Fullname(self):
        return f'{self.f_name} {self.l_name}'
    def Getage(self):
        return self.age
    def Name_With_Title(self):
        if self.gen == "male":
            return f"Hello mr {self.f_name}"
        elif self.gen == "female":
            return f"Hello miss {self.f_name}"
        else:
           return f"Hello {self.f_name}"
    def Getjob(self):
        return self.job 
    def full_info(self):
        return f"{self.Name_With_Title()} Your Full name in {self.Fullname()}"
    
    


user_one = Member("Jumhuur", "dayib", 28, "male", "full stack web developer")
user_2 = Member("Taysiir", "dayib", 6, "male", "UI/UX Designer")
user_3 = Member("Laki", "dayib", 41, "female", "Mobile app dev")
print(user_one.f_name)
print(user_one.l_name)
print(user_one.age)
# use methods
print(user_one.Fullname())
print(user_one.Getage())
print(user_one.Getjob())
print(user_one.Name_With_Title())
print(user_one.full_info())
print("*" * 45)

print(user_2.Fullname())
print(user_2.Getage())
print(user_2.Getjob())
print(user_2.Name_With_Title())
print(user_2.full_info())
print("*" * 45)

print(user_3.Fullname())
print(user_3.Getage())
print(user_3.Getjob())
print(user_3.Name_With_Title())
print(user_3.full_info())
print("*" * 45)


# print(user_3.f_name)
# print(user_3.l_name)
# print(user_3.age)

# print(dir(user_one))

