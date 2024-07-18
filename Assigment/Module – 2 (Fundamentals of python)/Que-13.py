#Write a Python program to count the number of characters (characterfrequency) in a string

def check(string):
    
    EmptyDict = {}
    
for char in string:
    if char in EmptyDict:
        EmptyDict[char] += 1
    else:
        EmptyDict[char] = 1
    return EmptyDict

input_string = input("Enter a string: ")
EmptyDict = check(input_string)
print("Character Frequency:")
for char, count in EmptyDict.items():
    print(f"'{char}': {count}")
