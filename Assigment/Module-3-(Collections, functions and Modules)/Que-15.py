# Write a Python program to get unique values from a list

list=[4,545,545,8,8,5211,0,54,9,7]
unique_list=[]

for item in list:
    if item not in unique_list:
        unique_list.append(item)
print("Unique list is : ",unique_list)
