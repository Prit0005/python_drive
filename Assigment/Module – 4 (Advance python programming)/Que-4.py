
#Write a Python program to read first n lines of a file.

file=open("Q-4.txt","r")
number=int(input("enter the number betwwen 1 to 7 : "))
for i in range(number):
    line=file.readline()
    if not line:
        break
    print(line,end="")
file.close()
