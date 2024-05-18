'''Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.'''


name="pritesh"
counter={}
for char in name:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1
print(counter)
