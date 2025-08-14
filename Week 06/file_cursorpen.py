# tracate  | waxaad masaxi kartaa qayb kamida file-kaaga
afile = open("Taysiir.txt", "a")
# afile.truncate(5)
# tell
# print(afile.tell())
afile2 = open("Taysiir.txt", "r")
# seek
afile2.seek(12)
print(afile2.read())

afile2.close()
afile.close()

import os

os.remove("Taysiir.txt")