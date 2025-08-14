import os

print("shaqo",os.getcwd())
print(os.path.abspath(__file__)) # file-ka aan ku shaqaynayaa halka uu ku jiro

print(os.path.dirname(os.path.abspath(__file__)))

# you can change dir using 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("shaqo",os.getcwd())
# os.chdir("C:\Users\Hp\Desktop\React js\Python")
file = open("jumhuur.txt")