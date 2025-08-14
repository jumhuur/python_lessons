def say_hello(name, age):
    return f"soo dhawaaw {name} your age is {age}"

# lamda function basic
hello = lambda name,age: f"soo dhawaaw {name} your age is {age}"
# lamda function with prams  has default value

mylamda = lambda name1="null", name2="null": f"soo dhawaw {name1} and {name2}"


print(say_hello("maxamad", 27))
print(hello("taysiir", 6))
print(mylamda("laki", "farax"))