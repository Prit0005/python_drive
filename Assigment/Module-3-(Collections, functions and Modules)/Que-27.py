#Write a Python program to find the repeated items of a tuple.

my_tuple = (1, 2, 3, 4, 2, 3, 5, 6, 2,"hello","hello")

def find_repeated_items(tuple):
    return {item for item in tuple if tuple.count(item) > 1}



repeated = find_repeated_items(my_tuple)
print("repeated items:",repeated)
