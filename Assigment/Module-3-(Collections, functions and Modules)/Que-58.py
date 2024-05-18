#Write a Python program to read a random line from a file.

import random

file=open("Que-58.txt","w")
file.write("\n this file is open\n this file is close\n this file is in read mode")
file.close()

with open("Que-58.txt","r")as file:
    line=file.readlines()

if not line:
    print("The file is empty.")
else:
    random_line=random.choice(line)
    print(random_line.strip())


