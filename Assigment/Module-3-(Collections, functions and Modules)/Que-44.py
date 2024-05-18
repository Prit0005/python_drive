'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
'''


from itertools import product

data = {'1': ['a', 'b'], '2': ['c', 'd']}

for combination in product(*data.values()):
    print("".join(combination),end=" ")
