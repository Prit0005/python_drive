#Write a Python program to write a list to a file.

fruit=["apple","mango","kiwi","guava","grape"]
file=open("Q-11.txt","w")
for i in fruit:
    file.write(i+"\n")

file.close()
