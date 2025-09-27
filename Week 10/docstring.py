# doc string 
# commenting vs Documenting 



# doc one line
def welcoming(name):
    '''waxaad function-kan loo sameeyay waa inu soo dhaweeyo'''
    msg = "welcome"
    print(f"${msg} {name}")



    # doc multible lines
def sayhello(name):
    """
    hadii aad doonayso ilaa dhaw layn waxaad samayn kartaa sidan 
    hada aan samayno oo kale waxaanad qori karaa doc_dhamays tiran 
    """
    print(f"Hello {name}")



sayhello("maxamad")
# print(dir(sayhello))
# print(sayhello.__doc__)
print(help(sayhello))
print(help(welcoming))