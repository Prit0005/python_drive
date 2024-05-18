#Write a Python program to find the highest 3 values in a dictionary



dictonary={"a":65,"b":45,"c":25,"d":78,"e":95}

a=list(dictonary.values())
a.sort(reverse=True)
a=a[:3]
print(a)
