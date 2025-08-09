x = 5
def numuratee () :
    global x
    x = 10
    return x

def num():
    global x
    x = 8
    return x




print(f"frome function1 {numuratee()}")
print(f"frome function2 {num(

)}")

print(f"frome global {x}")