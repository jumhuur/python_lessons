# enumerate
mylist = ["html", "css", "js", "github", "tailwindcss", "reactjs", "mongodb", "nodejs", "nextjs", "TypScript"]
for index , tech,  in enumerate(mylist, 1):
    print(f"{str(index).zfill(2)}- {tech}")


# reversed
myname = "Jumhuur"
for xaraf in reversed(myname):
    print(xaraf)

# help()
print(help(print))