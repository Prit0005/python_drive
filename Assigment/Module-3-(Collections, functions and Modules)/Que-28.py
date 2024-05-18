#Write a Python program to remove an empty tuple(s) from a list of tuples.


tuple_list=[(210,11),(),(41,5441,1),()]

def empty(tuple):
    return [ item for item in tuple_list if item]

remove_empty=empty(tuple_list)
print(remove_empty)
