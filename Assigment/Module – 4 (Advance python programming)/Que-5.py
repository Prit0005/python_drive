#Write a Python program to read last n lines of a file.



file = open("Q-4.txt", "r")
lines = file.readlines()
number = int(input("Enter the number between 1 to 7: "))
last_n_lines = lines[-number:]
for line in last_n_lines:
    print(line, end="")
file.close()
