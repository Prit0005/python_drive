#Write a Python function to calculate the factorial of a number (a nonnegative integer)


number=int(input("enter the number : "))
if number<=0:
    print("number is zero")
else:
    result=1
    for i in range(1,number+1):
        result*=i
    print(result)
