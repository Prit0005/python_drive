#Write a Python program to read an entire text file

file=open("Q-2.txt","w+")
file.write("this is que two file")
file.seek(0)
print(file.read())
file.close()
