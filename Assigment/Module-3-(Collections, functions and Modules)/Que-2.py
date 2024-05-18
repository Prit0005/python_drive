#How will you remove last object from a list?
#Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]
'''
you can use pop() method to remove last object.
list1[-1] is a show only number 25 because index of 25 is -1
'''

list1=[2, 33, 222, 14, 25]
print("current list : ",list1)
print("-1 index number is ",list1[-1])
list1.pop()
print("update list is after remove last object : ",list1)

