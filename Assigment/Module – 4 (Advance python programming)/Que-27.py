#What is used to check whether an object o is an instance of class A?

class A:
    pass

class B(A):
    pass


a = A()
b = B()

print(isinstance(a, A))  
print(isinstance(b, A))  
