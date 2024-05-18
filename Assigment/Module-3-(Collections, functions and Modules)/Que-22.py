#Write a Python program to check whether an element exists within a tuple.


number_tuple=(1,2,35,4413,48,79,7941)

tuple_input=int(input("enter the number : "))

def check_existing_element(number_tuple,tuple_input):
          return tuple_input in number_tuple

if check_existing_element(number_tuple,tuple_input):
    print(f"{tuple_input} exists in the tuple.")
else:
    print(f"{tuple_input} does not exist in the tuple.")
