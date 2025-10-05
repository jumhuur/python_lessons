# Xisaabta Lacagaha Guryaha Kirada ah 
import termcolor
from datetime import datetime
kiro = [{"Account": [2307.50], "8":[100,150,200,50,150,150,135,50,165,150], "9": [150,200,154,150,150,100,162], "10": [150,150]}]
baxay = [{"8":[183.50,105,200,20,100,25,15,150],"9":[130,100],"10":[130] }]
amaah = [{"Hinda": [10,15,5,3.50,40],"Maxamad": [37],  "Naasir": [50], "c/shakuur": [200],"cabdicasiis": [55]}]
account_out = {"laptops": [650,20,5,8]}
Numbers = [{"name":"Hodan", "number": 1234567890}, {"name":"Maxamad", "number": 1234567890}, {"name":"Naasir", "number": 1234567890}, {"name":"c/shakuur", "number": 1234567890}, {"name":"cabdicasiis", "number": 1234567890}]
def Amaah_le():
    for Amaah in amaah:
        Hinda = sum(Amaah.get("Hinda"))
        Maxamad = sum(Amaah.get("Maxamad".title()))
        Tota_Amaah = Hinda + Maxamad;
        print(f"Total Amaah: {Tota_Amaah}".title())
        return Tota_Amaah
def Baxay(bil):
     for OneBaxay in baxay:
        #   print(OneBaxay.get(bil))
          return OneBaxay.get(bil)
def Account_out_bill():
     print(termcolor.colored("Xisaabta Akoonka-ka".title(), "blue"))
     Total = 0
     for cash_key, cash_value in account_out.items():
          print(f"#-{cash_key} : {sum(cash_value)}$")
          Total += sum(cash_value)
     print(f"Total Baxay: {termcolor.colored(Total, "red")}$".capitalize())
     return Total
def ShowNumbers():
    for number in Numbers:
          print(f"{number['name']} : {number['number']}".title())
    print("Time: ", datetime.now().strftime("%H:%M:%p"))


def ChooseMonth():
    bilo = []
    print(termcolor.colored("Fadlan Dooro Bisha".title(), "blue"))
    for number in range(8,11):
        bilo.append(str(number))
        print(f"{str(number).zfill(2)} - bisha {number}aad".title())
    Bisha = input("Qor bisha ")
    def Kiro_calc():
        for k_bil in kiro:
                Bishii_08 = sum(k_bil[Bisha])
                # Account = sum(k_bil["Account"])
                return Bishii_08
    if Bisha.strip() in bilo:
            Total_Kiro = Kiro_calc()
            Total_baxay = sum(Baxay(Bisha))
            print(termcolor.colored(f"Wxaad dooratay bisha {Bisha.zfill(2)}", "red"))
            print(f'Total Kirada bisha {Bisha.zfill(2)} aad :  {Total_Kiro}$'.title())
            print(f"Total Baxay bisha {Bisha.zfill(2)} aad :  {Total_baxay}$".title())
            Total_Guud = Total_Kiro - Total_baxay
            print(f"Waxaa la doonayay inuu soo hadho:{Total_Guud}$".title())
            print(f"Total Dhaba {termcolor.colored(Total_Guud, "blue")}$")
            print(f"Taariikhda Maanta:" , datetime.now().strftime("%d-%b-%y"), "Time:" , datetime.now().strftime("%H:%M:%p"))
    elif Bisha.strip().upper() == "A":
        for Account in kiro:
             Total_Account = sum(Account.get("Account"))
             print(f"Total Akoon-ka : {termcolor.colored(Total_Account - Account_out_bill(), "magenta")}$")
             print(f"Taariikhda Maanta:" , datetime.now().strftime("%d-%b-%y"), "Time:" , datetime.now().strftime("%H:%M:%p"))
    elif Bisha.strip().upper() == "N":
        print(termcolor.colored("Lanbarada dhamaan Macaamiisha".title(), "blue"))
        ShowNumbers()
    else :
        #print(termcolor.colored("Si sax waxba umaad dooran".title(), "red"))
        raise ValueError(termcolor.colored("Si sax waxba umaad dooran".title(), "red"))
ChooseMonth()







