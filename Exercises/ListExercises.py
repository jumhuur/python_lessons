# ----------------------------------
# list Exercises (Methods)
# -----------------------------------

# Exercise 01
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
# Ku dar "mango" dhamaadka list-ka
# Output: ['apple', 'banana', 'mango']

# Exercise 02
students = ["Ahmed", "Fatima", "Ali"]
students.insert(1, "Maxamad")
print(students)
# Ku dar "Maxamad" booska labaad (index 1)
# Output: ['Ahmed', 'Maxamad', 'Fatima', 'Ali']


# Exercise 03
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)
# Ku dar dhammaan item-yada liiska b list a
# Output: [1, 2, 3, 4]



# Exercise 04
colors = ["red", "blue", "green", "blue"]
colors.pop(1)
print(colors)
# Ka saar "blue" ugu horeeya
# Output: ['red', 'green', 'blue']



# Exercise 05
nums = [5, 10, 15, 20]
nums.pop()
print(nums)
# Ka saar item-ka ugu dambeeya
# Output: [5, 10, 15]



# Exercise 06
items = [1, 2, 3, 4]
items.clear()
print(items)
# Tirtir dhammaan items-ka
# Output: []



# Exercise 07
letters = ['a', 'b', 'c', 'd', 'b']
print(letters.index("b"))
# Soo hel index-ka "b" ugu horeeya
# Output: 1


# Exercise 08
nums1 = [2, 3, 2, 5, 2, 7]
print(nums1.count(2))
# Tiriso inta jeer ee 2 ku jiro
# Output: 3



# Exercise 09
scores = [45, 10, 30, 90]
scores.sort()
print(scores)

# Kala hormari scores-ka si ay u noqdaan yaryar ilaa weyn
# Output: [10, 30, 45, 90]


# Exercise 10
names = ["Ayan", "Hodan", "Maxamad"]
names.reverse()
print(names)
# Rog liiska si uu u noqdo: ['Maxamad', 'Hodan', 'Ayan']
