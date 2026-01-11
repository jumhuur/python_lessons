from re import split


def word_count(word):
    spilit_word = word.split(" ")
    print(len(spilit_word))


word_count("soo dhawaaw waxaad tahay arday ")

# hadaad doonayso inaad meelo badan ku kala jarto waxaad
# adeegsan kartaa module re gaar ahaan split
kalmado = "cunto,cabitaan;qado macmacaan"
result = split(r'[,; ]', kalmado)
print(result)