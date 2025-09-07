# xisaabta bishii
import termcolor
kiro = [{"Account": [2307.50], "8":[100,150,200,50,150,150,135,50,165,150], "9": [300]}]
baxay = [{"8":[183.50,105,200,20,100,25,15,150],"9":[130] }]
amaah = [{"Hinda": [10,15,5,3.50,40],"Maxamad": [46], "Maxamad_Yuusuf": [50], "Naasir": [50], "c/shakuur": [200]}]
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
def ChooseMonth():
    bilo = []
    print(termcolor.colored("Fadlan Dooro Bisha".title(), "blue".title()))
    for number in range(8,10):
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
    elif Bisha.strip().upper() == "A":
        for Account in kiro:
             Total_Account = sum(Account.get("Account"))
             print(Total_Account)
            # print(Account = sum(k_bil["Account"]))
    else :
        print(termcolor.colored("Si sax waxba umaad dooran".title(), "red"))
ChooseMonth()







