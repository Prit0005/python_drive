#block of code that will perform specific task


#function with no argument & no return value

def printline():
    print("-"*70)

printline()
print("i am pritesh")
printline()


#function with argument but no return value

def sum(a,b):
    print("addition :",a+b)

printline()
x=int(input("enter the number : "))
y=int(input("enter the number : "))
sum(x,y)
printline()



#function with argument &  return value

def sub(a,b):
    return a-b

printline()
x=int(input("enter the number : "))
y=int(input("enter the number : "))

print("substration :",sub(x,y))
printline()
