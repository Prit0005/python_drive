#Write a Python program to unzip a list of tuples into individual lists.


tuple_list=[("pritesh",1),("nishant",2),("raj",3)]

list1,list2=zip(*tuple_list)

print("list 1 : ",list1)
print("list 2 : ",list2)
