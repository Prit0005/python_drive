# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1=int(input("enter a number 1 : "))
num2=int(input("enter a number 2 : "))
num3=int(input("enter a number 3 : "))

if num1==num2 or num1==num3 or num2==num3:
    print("sum is zero")
else:
    print("sum is : ",num1+num2+num3)
