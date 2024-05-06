import random

num=random.randint(1,20)

while True:
    guess=int(input("Enter the number between 1 to 20"))
    if guess==num:
        print("guess correct number")
        break
    elif guess>num:
        print("guess a higher number")
    elif guess<num:
        print("guess a smaller number")
