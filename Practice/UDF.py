def oddeven(a):
    if a%2==0:
        print(a,"is even number")
    else:
        print(a,"is not even number")


def maxoftwo(a,b):
    if a>b:
        print(a,"is big")
    else:
        print(b,"is big")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a," Is Max")
        else:
            print(c," Is Max")
    elif b>c:
        print(b," Is Max")
    else:
        print(c," Is Max")
def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n," Is Not Prime")
                break
        else:
            print(n," Is Prime")
    else:
       print(n," Is Not Prime") 
def pattern(n):
    for i in range(1,n):
        print("*"*i)
