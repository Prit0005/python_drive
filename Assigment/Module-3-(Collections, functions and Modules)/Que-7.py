#Write a Python program to remove duplicates from a list

element=["hello","hello","good morning","night","afternoon","noon","noon"]
print("current string is : ",element)

empty=[]
for string in element:
    if string not in empty:
        empty.append(string)
print("remove duplicate string is : ",empty)
