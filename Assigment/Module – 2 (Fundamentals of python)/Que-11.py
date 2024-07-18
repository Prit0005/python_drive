#Write a python program to sum of the first n positive integers.

number=int(input("enter the number  : "))
sum=0
if number<0:
    print("enter positive number")
else:
    sum=number*(number+1)//2
print("sum of n number is ",sum)
