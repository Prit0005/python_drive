'''
Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
'''
square=[]
for i in range(1,31):
    square.append(i**2)

first_five=square[:5]
last_five=square[-5:]

print("five element is : ",first_five)
print("second element is : ",last_five)
