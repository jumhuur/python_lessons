# xisaabta bishii
import termcolor
kiro = [{"Account": [800,1154], "8":[100,150,200,50,150,150,135,50,165,150]}]
baxay = [180.50,105,200,20,100,25]
amaah = [{"Hinda": [10,15,5,3.50,40],"Maxamad": [46], "Maxamad_Yuusuf": [50], "Naasir": [50], "c/shakuur": [200]}]
def Amaah_le():
    for Amaah in amaah:
        Hinda = sum(Amaah.get("Hinda"))
        Maxamad = sum(Amaah.get("Maxamad"))
        Tota_Amaah = Hinda + Maxamad;
        print(f"Total Amaah: {Tota_Amaah}")
        return Tota_Amaah
    
def ChooseMonth():
    bilo = []
    print(termcolor.colored("Fadlan Dooro Bisha", "blue"))
    for number in range(8,9):
        bilo.append(str(number))
        print(f"{str(number).zfill(2)} - bisha {number}aad")
    Bisha = input("Qor bisha ")
    def Kiro_calc():
        for k_bil in kiro:
            Bishii_08 = sum(k_bil[Bisha])
            Account = sum(k_bil["Account"])
            return Bishii_08 + Account
    if Bisha.strip() in bilo:
            Total_Kiro = Kiro_calc()
            Total_baxay = sum(baxay)
            print(f'Total Kiro = {Total_Kiro}$')
            print(f"Total Baxay {Total_baxay}$")

            Total_Guud = Total_Kiro - Total_baxay
            LaHayo = Total_Guud - Amaah_le()
            print(f"Waxaa la doonayay inuu soo hadho :{Total_Guud}$")
            print(f"waxaa maqan {Total_Guud - LaHayo}$")
            print(f"Total Dhaba {termcolor.colored(LaHayo, "blue")}$")
    else :
        print(termcolor.colored("Bisha aad dooratay lama helin", "red"))

ChooseMonth()







