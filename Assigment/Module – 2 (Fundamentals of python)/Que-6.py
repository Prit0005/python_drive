#Write python program that swap two number with temp variable and without temp variable


a,b=5,10
# with temp veriable
print("a : ",a)
print("b : ",b)
temp=a
a=b
b=temp
print("after swaping value a is : ",a)
print("after swaping value b is : ",b)


#without temp
a,b=5,10
a,b=b,a
print("after swaping value a is : ",a)
print("after swaping value b is : ",b)
