'''
If condtion

1. Simple If
        if condtion:
            statement

2. If/Else
        if condtion:
            statement
        else:
            statement
3. Lader If
    if contdition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:
    statemnt

4. Nested If
    if condition:
        if condition:
            statement
        else:
            statement
    else:
        statement


'''

a=int(input("Enter A:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if a>b:
    if a>c:
        print("A is max")
    else:
        print("c is max")
elif b>c:
    print("b is max")
else:
    print("c is max")
    
