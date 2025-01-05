qoraal1 = "waxan ahay arday";
qoraal2 = 'waxaan ahay arday'
print(qoraal1)
print(qoraal2)


# singal qout
Msg = "soomalilan waa 'Haragaysa'"
Hrg = 'Hargaysa waa "Soomaliland"'

print(Msg)
print(Hrg)

#dauble qout

# layn badan 

Qoraal_Dheer = ''' waxaan ahay arday waxaan
 dhigataa dhamaan waxii 
 casharo i 
 Khuseeya Gaar 
 Ahaan Hawlahayga 
 CAAADIGA AH 
 '''
print(Qoraal_Dheer)

Qoraal_Dheer = """ waxaan ahay arday waxaan
 dhigataa dhamaan waxii 
 casharo i 
 Khuseeya Gaar 
 Ahaan Hawlahayga 
 CAAADIGA AH 
 """

print(Qoraal_Dheer)



# indexing an slicing 

mymessage = "ilaahay ha laga baqo meel kasta iyo mar kasta"

print(mymessage[0]) # i
print(mymessage[21]) # b

# waxaad siin kartaa tiro maynis wada 
print(mymessage[-1]) # a
print(mymessage[-7])

# waxaad siin kartaa bilow iyo dhamaad
print(mymessage[0:16])

print(mymessage[10:12]) # l

# bilawga waad ka boodi kartaa

print(mymessage[:10])
# waxaad iska dayn kartaa dhamaadka 
print(mymessage[5:])

# labada qayboodba waad iska dayn kartaa 
print(mymessage[:]) # full string

# waxaad xadidi kartaa talaabooyin ka ay qaadayso 
print(mymessage[::1]) # full messgae waayo waxba maynaan badalin 1 talaabo marka hore wuu qaadayay

# laba taalbo ayaan boodnay
print(mymessage[::2]) # iahyh aabq elksaiomrksa
print(mymessage[::3]) #iayaa qmlaaym s

#----------------string Methods----
# strip() = waxay jaraysaa waxii space ah ama waxi aad siiso sidan oo kale strip("#")
# lstrip()  = dhinaca midig
# rstrip()  = dhinaca Bidix
# len(string) = waxy ku siinaysaa qoraalka inta uu yahay ee xaraf
# title() waxay kuugu badalaysaa qaab ciwaan xataa xarafka lanbar ka danbeeya way kuu waynayasaa
# upper()
# lewer()
# cap
#----------------------------------

Msg = "    Waxaan Jeclay Python  ilaa 3sano "
Msg1 = "#######waxaan jeclahay Python#######"

#strip()
print(Msg.strip())
print(Msg1.strip("#"))
#lstrip()  waxay ka jaraysaa midigta
print(Msg.lstrip())
print(Msg1.lstrip("#"))
#rstrip() waxay ka jaraysaa dhinaca bidix da 
print(Msg.rstrip())
print(Msg1.rstrip("#"))

#len(string)
print(len(Msg))

# title()
print(Msg.title())

# upper()
print(Msg.upper())


#lower()
print(Msg.lower())


#capitalize()
print("Maxamad".capitalize())

# zfill()

a,b,c,d = "1","10","100","1000"
print(a)
print(b)
print(c)
print(d)

print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))
print(d.zfill(4))






