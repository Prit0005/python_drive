#Write a Python function to check whether a number is in a given range

number=int(input("enter the number between 1 to 100 : "))
if number in range(1,101):
    print("number in range")
else:
    print("number in not in range")
