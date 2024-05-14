import UDF


while True:
    print("-"*50)

    print("1. oddeven")
    print("2. maxoftwo")
    print("-"*50)

    choice=int(input("enter your number"))
    print("-"*50)
    if choice==1:
        n1=int(input("enter your number"))
        UDF.oddeven(n1)
        print("-"*50)
    elif choice==2:
        n1=int(input("enter your number"))
        n2=int(input("enter your number"))
        UDF.maxoftwo(n1,n2)
        print("-"*50)
        break
     elif choice==3:
        n1=int(input("Enter Number : "))
        n2=int(input("Enter Number : "))
        n3=int(input("Enter Number : "))
        UDF.maxofthree(n1,n2,n3)
        print("*"*50)
    elif choice==4:
        n1=int(input("Enter Number : "))
        UDF.fibonacci(n1)
        print("*"*50)
    elif choice==5:
        n1=int(input("Enter Number : "))
        UDF.prime(n1)
        print("*"*50)
    elif choice==6:
        n1=int(input("Enter Number : "))
        UDF.pattern(n1)
        print("*"*50)
    elif choice==7:
        print("Thank You.")
        print("*"*50)
        break
    else :
        print("thank you,invalid input")
        
