#How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

'''
in python,class define using class keyword and aftre write class name.
self is a parameter that is a referance to the current instance of class.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"my name is {self.name} and I am {self.age} years old."

person1 = Person("pritesh", 18)
print(person1.introduce())
