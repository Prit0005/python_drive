#Write a Python program to get the Fibonacci series of given range.

number=int(input("enter the number : "))
a,b=0,1;
print(a,end=' ')
while b<number:
    print(b,end=' ')
    a,b=b,a+b

