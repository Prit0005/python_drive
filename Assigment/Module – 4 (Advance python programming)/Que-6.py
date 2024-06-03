#Write a Python program to read a file line by line and store it into a list


file=open("Q-4.txt","r")
linelist=[]
for line in file:
    linelist.append(line.strip())
print(linelist)
file.close()
