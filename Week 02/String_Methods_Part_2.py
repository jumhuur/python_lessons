# split 
My_name = "maxamad dayib cabdi"
My_name_2 = "maxamad_dayib_cabdi"
My_name_3 = "maxamad-dayib-cabdi"
splited = My_name.split()
print(splited)
print(My_name_2.split("_")) 

# max split in py 
print(My_name_3.split("-", 3))

# center(width, fillchar)
text = "I love Python An Js"
text_2 = "I love Python aND jS"
print(text.center(25, "#"))

#swaopecase()
print(text.swapcase())
print(text_2.swapcase())

#startswidth(string, start, end)
print(text.startswith("s"))
print(text.startswith("I", 16))
print(text.startswith("I", 15, 20))
#endsWith(string, start, end)
print(text.endswith("s"))
print(text.endswith("s", 15))
print(text.endswith("s", 15, 17))

# index("string", start, end)
# --- HADII INDEX UU WAAYO QORAALKA AAD U DIRTAY WAXA UU SOO SARAYAA QALAD

print(text.index("love"))
print(text.index("Js", 7))
print(text.index("Js", 14, 20))
# find
print(text.find("love"))
print(text.find("Js", 7))
print(text.find("Js", 14, 20))
print(text.find("Js", 4, 4)) # if text is not found result is -1

# rjust(width, fill char)
name = "jumhuur"
print(name.rjust(10,"$"))
#ljust (width, fill char)
print(name.ljust(10,"@"))


##splitlines 
# waxay ku sinaysaa lines-kaagii oo ah array line walba element ayay kaaga dhigaysaa
lines = '''waxaan ahay 
maxamad
waxaan dhigtaa luuqada 
python iyo js
'''
print(lines.splitlines())

## expendtaps (dib ayaa fahankeeda loo eegayaa taas)
# waxay samaynaysaa tabs - taas o aad xukumi karto inta tab ee aad rabto sidan hooose 
tap_text = "jumhuur\ttaysiir\tonline"
print(tap_text.expandtabs(20)) # laba tab 


## count
# waxa uu kuu sheegay inta jeer ee kalmadan ku jirto hadalka
Mystr = "ilove python and js"
print(Mystr.count("js", 0, 16))
print(Mystr.count("js", 10, 20))

# mynameTest = "maxamad dayib cabdi"
# print(mynameTest.split(" "))




