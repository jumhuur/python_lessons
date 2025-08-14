word = "tttaayyssirrrrr"

def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])
    
print(cleanWord(word))

def countdown(n):
    if n <= 0:  # base case
        print("Time's up!")
    else:
        print(n)
        countdown(n - 1)  # recursive call

countdown(5)



def factorial(n):
    if n == 1:  # base case
        return 1
    return n * factorial(n - 1)  # recursive call

print(factorial(4))  # 5 × 4 × 3 × 2 × 1 = 120


Weekdays = ["sabti","axad","isniin", "jimce","salaasa", "arbaca", "khamiis"]
def ex_recurtion(days,index=0):
    if days[index] != "jimce":
            days.pop(index)
            index += 1
    else:
        return f"one day is here {days[index]}"

    return ex_recurtion(days)

print(ex_recurtion(Weekdays,0))


# Example Input
nums = [1, 2, 3, 4]

def recur1(nums):
    if len(nums) == 1:
        return nums[0]
   
    else:
        return nums[0] + recur1(nums[1:])
print(recur1(nums))
# Expected Output 10


# Example Input
text = "Python"
def reversestr(text):
    if len(text) == 1:
        return text[0]
    else:
        # reversed_txt = [*text]
        # reversed_txt.reverse()
        text.reverse()
        print(text)
        return f"{text[0]}{reversestr(text[1:])}"


# Expected Output
"nPoyht"

print(reversestr([*text]))

text = "Python"
# print(len(text))
kalarog = [*text]
kalarog.sort()
print(kalarog)



def iskugayn(*listNumbers):
    result = 0
    for Number in listNumbers:
        result += Number
    return result
print(iskugayn(10,5))
    





