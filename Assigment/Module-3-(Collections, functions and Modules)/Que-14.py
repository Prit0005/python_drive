#Write a Python program to find the second smallest number in a list

number=[10,20,50,7,90,5]
print("number list is : ",number)

def alloperation(number):
    number.sort()
    print("second small numebr is : ",number[1])
    
alloperation(number)
