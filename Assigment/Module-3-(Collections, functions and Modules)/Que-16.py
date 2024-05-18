# Write a Python program to check whether a list contains a sub list

number_list=[1,522,7941,451,741,7845,10,51]
sub_list=[1,451,0]

def check(number_list,sub_list):
    for sub in sub_list:
        if sub not in number_list:
            return False
            break
    return True

print(check(number_list,sub_list))
