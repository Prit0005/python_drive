#Write a Python program to append text to a file and display the text.



file = open("Q-3.txt", "w")
file.write("this is a que three file\n")
file.close()


file = open("Q-3.txt", "a")
file.write("this is a que three file 1")
file.close() 


file = open("Q-3.txt", "r")
print(file.read())
file.close() 


