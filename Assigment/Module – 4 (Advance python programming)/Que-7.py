#Write a Python program to read a file line by line store it into a variable.


file=open("Q-4.txt","r")
content=""
for var in file:
    content+=var
print(content)
