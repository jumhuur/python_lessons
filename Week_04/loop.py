# while

# a = 1
# while a  <= 10:
#     print(a)
#     a += 1
# else:
#     print("Loop done")


c = 0
while c  < 10:
    print(c)
    c += 1
print("Loop done")

countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "soomaliland", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]
Students = ["raashid", "maxamad", "xasan", "nimcaan", "shukri", "najaax", "c/rashiid", "shucayb", "sayid cali", "taysiir"]
print(len(Students))

num = 0
while num < len(Students):
    print(f'{str(num + 1).zfill(2)}.-{Students[num]}')
    num += 1
print("all list is dispalyed")
print("*" * 30)
cont = 0
while cont < len(countries):
    print(f"{str(cont + 1).zfill(2)} - {countries[cont].rjust(int(len(countries[cont]) + 1),"@" )}" if countries[cont] == "soomaliland" else f"{str(cont + 1).zfill(2)} - {countries[cont]}")
    cont += 1
print(f"printed {len(countries)}")