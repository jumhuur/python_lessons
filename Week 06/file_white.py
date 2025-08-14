myfile = open("Taysiir.txt", "w")
#---- write => w  ------
# ku qorid  hadii aad adeegsan /n wuu isku daba qabanayaa 
myfile.write("soo dhawaaw walaal")
myfile.write("waxaan kugu soo dhawaynayaa qaybtan")

# hada magac walba waxa uu ku qoray line
myfile.write("cali\n")
myfile.write("yuusuf\n")
myfile.write("saleebaan\n")
myfile.write("cimaraan\n")

# hal mar data badan oo isku wada daba xidhan

list_s = ["maxamad", 'nimcaan', "raashid", "shukri"] 
myfile.writelines(list_s)

list_s_t = ["maxamad\n", 'nimcaan\n', "raashid\n", "shukri\n"] 
myfile.writelines(list_s_t)

myfile.close()


#---- append => a ------

newfile = open("Laki.txt", "a")

# waxaan ku bilaabayaa qoraalkan 
walaalo = ["maxamad\n", "mukhtaar\n", "taysir\n", "farax\n"]
newfile.write("Magacagu waa laki\n")
newfile.write("waxaan dhigtaa dugsiga hoose dhex ee cigaal \n")
newfile.write("da,daydu waa 14 jir\n")
newfile.write("waxaa ila dhashay oon walaalo nahay \n")
newfile.writelines(walaalo)
