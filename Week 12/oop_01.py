# syntext
class Users:
    def __init__(self) -> str:
        print("New user is added")

Users()
Users()
Users()

# class info
print(dir(Users))
# example
# print(dir(int))
# print(dir(str))

# class-ka ay ka tirsantahay | ku kaydin var
user_one = Users()
print(user_one.__class__)