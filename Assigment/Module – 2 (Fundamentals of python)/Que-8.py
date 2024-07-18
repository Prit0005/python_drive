#Write a Python program to test whether a passed letter is a vowel or not.


input1=["a","e","i","o","u"]
char=input("enter a alphabate : ")
lowercase=char.lower()
if lowercase in input1:
    print(char,"is vowel")
else:
    print(char,"is not vowel")
    
