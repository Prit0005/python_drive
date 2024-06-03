#Write a Python program to count the number of lines in a text file

file=open("Q-4.txt","r")
count=0

for line in file:
    count+=1
print(count)
