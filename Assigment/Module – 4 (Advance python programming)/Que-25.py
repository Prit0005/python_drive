#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?


'''
In Python, __init__ is a special method  that is automatically called
when a new instance of a class is created.
that is also known as a constructor.

in python you can inherite one class to anothe class it is called is inheritance.

'''

class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal): 
    def bark(self):
        return "Dog barks"

dog = Dog()
print(dog.speak()) 
print(dog.bark())
