#Write a Python function that checks whether a passed string is palindrome or not


def check(string):
    return string==string[::-1]
name=input("enter the string : ")

result=check(name)
if result:
    print(f"{name} is palindrome ")
else:
    print(f"{name} is not palindrome ")

    
