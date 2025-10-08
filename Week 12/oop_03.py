# class attributes
import termcolor, requests
class Xisaab:
    print("Fadlan Dooro Bisha")
    for number in range(8,11):
        print(number)
    UserInput = input("").strip()
    Bilo = ["08", "09", "10"]
    def __init__(self):
        self.Bil = Xisaab.UserInput

    def One_Month(self):
        if self.Bil in Xisaab.Bilo:
            return f"Xisaabta Bisah {self.Bil}"
        else:
            raise ValueError("Bisha aad dooratay waa qalad !")


one = Xisaab()
print(one.One_Month())
