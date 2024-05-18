'''Write a Python function that takes two lists and returns true if they have
at least one common member.'''


first=["one","two","three"]
second=["four","five","six"]
def twolist(first,second):
    for item in first:
        if item in second:
            return True
    return False

result=twolist(first,second)
print(result)
