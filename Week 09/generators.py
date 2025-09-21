def generator():
    yield 1
    yield 2
    yield 3
    yield 4

print(generator())

gen = generator()
print(next(gen))  # 1
# waxaan halkan ku qaban karaa hawl kale kadib 
# waxaan halii kasii wadayaa waxa function-ka ka soo noqonaya 
# anoon dib u soo bilaabin waayo waxaan soo adeegsaday yield badalka return
print(next(gen)) # 2
print(next(gen)) # 3
# print(next(gen)) # 4 kan waxaan u joojiyay si xabad loop looga soo saaro  

print("*" * 44)
# waxaan u adeegsan karaa loop
# laakiin hadaa data-da aad hore ula soo baxday waxba kuuma soo baxayaan
for num in gen:
    print(num)
