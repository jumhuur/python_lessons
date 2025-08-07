# Example 1
def first():
    print("Hello world")

first()

def func2():
    return "hello world"

print(func2())

# Example 2 
def addition(n1,n2):
    if type(n1) == int and type(n2) ==  int:
        print(n1 + n2)
    else:
        print("string not allwed")

addition(11,55)

#Example 3
def fullname(f_name, m_name, l_name):
    return f"Hello {f_name.strip().capitalize()} {m_name.strip().capitalize():.1s} {l_name.strip().capitalize()}"

print(fullname("Jumhuur    ", "dayib", "cabdi"))
# Example 4
listUsers = ["Xuseen", "muuse", "caydiid", "c/laahi", "caaqil"]
def Hello_User(Users):
    for User in Users:
        print(f"Hello {User}")

Hello_User(listUsers)




