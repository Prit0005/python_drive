#Write a Python program to returns sum of all divisors of a number

total=0
number = int(input("enter a number: "))
for i in range(1,number):
    if number%i==0:
        total+=i
print("sum of all divisors of a number : ",total)

