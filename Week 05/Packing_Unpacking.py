#example 1
def hello(*dad):
    print(type(dad))
    for qof in dad:
        print(f"soo dhawaaw {qof}")

hello("maxamad","cismaan")


# example 2
def hello_2(**Dad):
    # print(type(Dad))
    # print(Dad)
    for key,value in Dad.items():
        print(f"{key} = {value}")

hello_2(maxamad="12", xasan="45")


# example 3

with_outProg = ("html", "css", "js")

with_Prog = {
    "html": "98%",
    "css": "88%",
    "python": "66%"
}

def show_skills(name="null",*OutProg, **with_Prog):
    print(f"soo dhawaaw {name}")
    print("skills with out Prog")
    skillindex = 0
    for skill in OutProg:
        print(f"{skillindex + 1}- {skill}")
        skillindex += 1
    print("skills with Prog")
    skill2index = 0
    for skill_key, skill_value in with_Prog.items():
        print(f"{skill2index + 1}- {skill_key} = {skill_value}")
        skill2index += 1


show_skills("Jumhuur", *with_outProg, **with_Prog)

def showskill(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"--- {skill} - {value}")

showskill(html = "80", css="50%")






