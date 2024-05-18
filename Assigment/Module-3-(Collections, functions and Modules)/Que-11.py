#Write a Python function that takes a list and returns a new list with unique elements of the first list


number=[1,1,2,3,4,5,5,5]
print("original list is : ",number)
def unique(number):
    unique_list=[]
    for item in number:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print("unique list is : ",unique(number))
    
