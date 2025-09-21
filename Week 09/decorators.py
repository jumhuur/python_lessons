# Example 01
def req_admin(hawl):
    def ilaaliye(*id,**kwargs):
        User = kwargs.get("User")
        if User == "user":
            return "❌ Access denied"
        else :
            print("You are Admin Welcome")
        return hawl(*id,**kwargs)
    return ilaaliye

@req_admin
def deletePost(postid,**kwargs):
    return f"{postid} deleted"
print(deletePost(1, User="user"))


# Example 02
admins = ["cali", "Maax"]
def shaqo(salaan):
    def kalasaar(**User):
        for admin in admins:
            if User.get("Name") == admin:
                return "Woow You are admin welcome"
            else:
             return salaan(**User)
    return kalasaar
@shaqo
def salaan(**User):
    return f"{User.get("Name")} soo dhawaaw"

print(salaan(Name="MUUSE"))



    