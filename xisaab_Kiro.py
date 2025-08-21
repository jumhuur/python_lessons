# xisaabta bishii
import termcolor, pyfiglet
kiro = [{"Hore": [800,1154], "08/2025":[100,150,200,50,150,150,135,50]}]
baxay = [170,105,200,20,100]
amaah = [{"Hinda": [10,15,5,3.50],"Maxamad": [46], "Maxamad_Yuusuf": [50], "Naasir": [50], "c/shakuur": [200]}]
def Amaah_le():
    for Amaah in amaah:
        Hinda = sum(Amaah.get("Hinda"))
        Maxamad = sum(Amaah.get("Maxamad"))
        Tota_Amaah = Hinda + Maxamad;
        print(f"Total Amaah: {Tota_Amaah}")
        return Tota_Amaah
def Kiro_calc():
    for k_bil in kiro:
        Bishii_08 = sum(k_bil["08/2025"])
        Hore = sum(k_bil["Hore"])
        return Bishii_08 + Hore
Total_Kiro = Kiro_calc()
Total_baxay = sum(baxay)
print(f'Total Kiro = {Total_Kiro}$')
print(f"Total Baxay {Total_baxay}$")

Total_Guud = Total_Kiro - Total_baxay
LaHayo = Total_Guud - Amaah_le()
print(f"Waxaa la doonayay inuu soo hadho :{Total_Guud}$")
print(f"waxaa maqan {Total_Guud - LaHayo}$")
print(f"Waxaa la Hayaa {LaHayo}$")
# print(f"Main Total: {termcolor.colored(Account_Total + LaHayo, "blue")}$")

