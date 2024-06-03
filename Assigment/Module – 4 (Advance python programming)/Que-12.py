#Write a Python program to copy the contents of a file to another file.

with open("Q-4.txt","r")as onefile:
    content=onefile.read()
with open("Q-12.txt","w")as twofile:
    twofile.write(content)
print("sucess")
