websites = []
countBook = 5
DomainExtensions = [".com", ".net", ".dev", ".org", ".info", ".so", ".sa", ".ae"]
while countBook > 0:
    print("*" * 30)
    web = input("Enter website (without https://): ")
    Extenstion = web.split(".")[1]
    if str(f".{Extenstion}") in DomainExtensions:
        fullweb = f"https://{web.strip().lower()}"

        if fullweb in websites:
            print("❌ Duplicate website not allowed.")
            print(f"⚠️ {fullweb} is already in your list.")
        else:
            websites.append(fullweb)
            countBook -= 1
            print("*" * 30)
            print(f"✔️ {fullweb} added.")
            print(f"{countBook} more can be added.")

            if countBook < 1:
                print("✅ Bookmark list is full.")
    else:
        print("❌ Invalid extension. Use one of these:")
        index = 0
        while index < len(DomainExtensions):
            print(f"🔹 {DomainExtensions[index]}")
            index += 1
else:
    index = 0
    print("📄 Your bookmarked websites:")
    while index < len(websites):
        print(f"{index + 1} - ✔️ {websites[index]}")
        index += 1
