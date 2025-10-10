class Students :
    # class attribute
    students = [
        {
            "f_name": "Maxamad",
            "l_name": "Dayib",
            "age": 22,
            "school": "Taysiir Online",
            "semester": 2,
            "course": "Python Programming",
            "Id": "STU001"
        },
        {
            "f_name": "Nimco",
            "l_name": "Ali",
            "age": 20,
            "school": "Taysiir Online",
            "semester": 1,
            "course": "Web Development",
            "Id": "STU002"
        },
        {
            "f_name": "Hodan",
            "l_name": "Isse",
            "age": 23,
            "school": "Taysiir Academy",
            "semester": 3,
            "course": "Full Stack Development",
            "Id": "STU003"
        },
        {
            "f_name": "Mukhtaar",
            "l_name": "Ahmed",
            "age": 24,
            "school": "Taysiir Academy",
            "semester": 4,
            "course": "Data Science",
            "Id": "STU004"
        },
        {
            "f_name": "Cismaan",
            "l_name": "Nur",
            "age": 21,
            "school": "Taysiir Online",
            "semester": 2,
            "course": "ReactJS & NextJS",
            "Id": "STU005"
        }
    ]

    def __len__(cls):
        return f"Students Count {len(cls.students)}"
    @staticmethod
    def Welcome(name):
        return f"Welcome {name}"

    @classmethod
    def Allstudents(cls):
        return cls.students
    @classmethod
    def remove_student(cls,Id):
        cls.student_obj = next((student for student in Students.students  if student["Id"] == Id))
        Students.students.remove(cls.student_obj)
        return f"removed this student {cls.student_obj}"
    @classmethod
    def update_student(cls,Id,f_name,l_name,age,school,semester,course):
        student_obj = next((std for std in cls.students  if std["Id"] == Id), None)
        if not student_obj:
            raise ValueError(f"No student found with ID {Id}")
        else:
            new_obj = {
                "f_name":f_name,
                "l_name":l_name,
                "age":age,
                "school":school,
                "semester":semester,
                "course":course,
                "Id": Id
            }
            index = Students.students.index(student_obj)
            Students.students[index] = new_obj
            print("Updated")
            print("old info", student_obj)
            return f"new info {new_obj}"
    @classmethod
    def add_student(cls,Id,f_name,l_name,age,school,semester,course):
        student_obj = next((std for std in cls.students  if std["Id"] == Id), None)
        if student_obj:
            raise ValueError(f"this id {Id} already Token")
        else:
            new_obj = {
                "f_name":f_name,
                "l_name":l_name,
                "age":age,
                "school":school,
                "semester":semester,
                "course":course,
                "Id": Id
            }
            Students.students.append(new_obj)
            return f"new Student Added"
    def __init__(self,Id):
        # Student = filter(lambda student : student.get("Id") == Id, Students.students)
        self.Info = next((std for std in Students.students if std["Id"] == Id), None)  #[std  for std in Student][0]
        if not self.Info:
            raise ValueError(f"No student found with ID {Id}")
    def student_full_name(self):
        return f"{self.Info.get("f_name")} {self.Info.get("l_name")}"
    def get_school(self):
        return f"{self.Info.get("school")}"
    def get_age(self):
        return f"{self.Info.get("age")}"
    def get_semester(self):
        return f"{self.Info.get("semester")}"
    def get_course(self):
        return f"{self.Info.get("course")}"
    def greating(self):
        return Students.Welcome(self.student_full_name())
    

        

User = Students("STU002")
# print(Students.Allstudents())
print(User.Info)
print("*" * 45)
print(User.student_full_name())
print("*" * 45)
print(User.get_school())
print("*" * 45)
print(User.get_age())
print("*" * 45)
print(User.get_semester())
print("*" * 45)
print(User.get_course())
print("*" * 45)
print(User.greating())
print(len(Students.Allstudents()))
print("*" * 45)
print(User.remove_student("STU005"))
print("*" * 45)
print(len(Students.Allstudents()))
print(Students.Allstudents())
print("*" * 45)
updated = Students.update_student("STU001", "Asma", "Maxamad", 25, "Ibnu Baaz", 3, "caqiido")
print(updated)
print("*" * 45)
print(len(Students.students))
print("*" * 45)
add = Students.add_student("STU0078", "xamda", "Maxamad", 25, "Ibnu Baaz", 3, "caqiido")
print(add)
addstudents = Students.add_student("STU0079", "Muuna", "cimaraan", 28, "Ibnu Baaz", 3, "Maths")
print(len(Students.students))






