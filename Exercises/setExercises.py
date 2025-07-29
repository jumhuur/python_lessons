# Exercise 01
names = {"Ali", "Ayan"}
names.add("Maxamad")
print(names)
# Ku dar "Maxamad" set-ka
# Output: {'Ali', 'Ayan', 'Maxamad'}

# Exercise 02
colors = {"red", "green", "blue"}
colors.remove("green")
print(colors)
# Ka saar "green" adoo isticmaalaya remove()
# Output: {'red', 'blue'}


# Exercise 03
days = {"Monday", "Tuesday", "Wednesday"}
days.discard("Sunday")
print(days)
# Tijaabi discard() adoo ka saaraya "Sunday"
# Output: {"Monday", "Tuesday", "Wednesday"} (no error)


# Exercise 04
a = {1, 2}
b = {3, 4}
a.update(b)
print(a)
# Ku dar dhammaan b → a adoo adeegsanaya update()
# Output: {1, 2, 3, 4}


# Exercise 05
c = {1, 2}
d = {2, 3}
cd = c.union(d)
print(cd)
# Samee set cusub oo ah midda isku darkooda (union)
# Output: {1, 2, 3}


# Exercise 06
x = {"apple", "banana", "cherry"}
y = {"banana", "kiwi", "cherry"}

same = x.intersection(y)
print(same)
# Waxyaabaha ay wadaagaan labadan set
# Output: {'banana', 'cherry'}



# Exercise 07
d = {1, 2, 3}
f = {2, 3, 4}
df = d.difference(f)
print(df)
# Ka saar kuwa b ku jira a → difference
# Output: {1}



# Exercise 08
s = {1, 2, 3}
s.clear()
print(s)
# Tirtir dhammaan items-ka
# Output: set()


# Exercise 09
S = {"one", "two", "three"}
print(len(S))
# Soo saar tirada elements ee ku jira
# Output: 3


# Exercise 10
items = {100, 200, 300}
print(items.pop())
# Isticmaal pop() si aad u saarto mid random ah
# Output: wax random ah oo la saaray
