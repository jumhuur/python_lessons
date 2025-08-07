# Example 1: Even or Odd numbers with zfill formatting
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in nums:
    if number % 2 == 0:
        print(f"Even: {str(number).zfill(2)}")
    else:
        print(f"Odd: {str(number).zfill(2)}")

print("=" * 40)

# Example 2: Loop through characters in a name
name = "Jumhuur"
for char in name:
    print(f"[ {char} ]")

print("=" * 40)

# Example 3: Skills dictionary
skills = {
    "Html": "90%",
    "Css": "85%",
    "Js": "90%",
    "ReactJS": "66%",
    "NextJS": "75%"
}

for skill in skills:
    print(f"{skill} progress: {skills[skill]}")

print("=" * 40)

# Example 4: Nested dictionary with roles and skills
people = {
    "Jumhuur": {
        "role": "admin",
        "skills": {
            "Html": "90%",
            "Css": "85%",
            "Js": "90%",
            "ReactJS": "66%",
            "NextJS": "75%"
        }
    },
    "Cismaan": {
        "role": "student",
        "skills": {
            "Html": "40%",
            "Css": "35%",
            "Js": "20%",
            "ReactJS": "15%",
            "NextJS": "5%"
        }
    },
    "Cimaraan": {
        "role": "student",
        "skills": {
            "Html": "40%",
            "Css": "35%",
            "Js": "20%",
            "ReactJS": "15%",
            "NextJS": "5%"
        }
    },
    "Cubayd": {
        "role": "student",
        "skills": {
            "Python": "60%",
            "Go": "95%",
            "Js": "90%",
            "Ruby": "85%",
            "NextJS": "75%"
        }
    }
}

# First way: basic access
for person in people:
    print(f"-- {person} role is [{people[person].get('role')}]")
    print("Skills:")
    for skill in people[person]["skills"]:
        print(f"   - {skill}: {people[person]['skills'][skill]}")

print("=" * 40)

# Second way: using .items() for cleaner looping
for person_name, person_info in people.items():
    print(f"-- {person_name} role is [{person_info.get('role')}]")
    print("Skills:")
    for skill_name, skill_value in person_info.get("skills").items():
        print(f"   - {skill_name}: {skill_value}")
