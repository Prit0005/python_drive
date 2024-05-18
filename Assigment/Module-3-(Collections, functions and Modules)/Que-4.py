'''Write a Python function to get the largest number, smallest num and sum
of all from a list'''


number=[10,20,50,7,90,5]
print("number list is : ",number)

def alloperation(number):
    number.sort()
    print("largest numebr is : ",number[-1])
    print("small numebr is : ",number[0])

    total=0
    for i in number:
        total+=i
    print("sum of all number is : ",total)
    #also we can use sum function
    
alloperation(number)
