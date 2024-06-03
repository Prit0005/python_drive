#What is Instantiation in terms of OOP terminology?
'''
In object-oriented programming (OOP), instantiation
refers to the process of creating a new instance of a class
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("pritesh", 18)
