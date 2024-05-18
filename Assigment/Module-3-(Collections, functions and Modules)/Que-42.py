#Write a Python program to print all unique values in a dictionary

dictonary = {"a": 1, "b": 2, "c": 3, "d": 2,}

unique=set(dictonary.values())
print(unique)
