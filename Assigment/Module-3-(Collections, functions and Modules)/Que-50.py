#Write a Python function to check whether a number is perfect or not.


number=int(input("enter the number : "))
sum1=0

for i in range(1,number):
    if number%i==0:
        sum1+=i
if sum1==number:
    print("number is perfect")
else:
    print("number is not perfect")
