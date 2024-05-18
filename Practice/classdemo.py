'''
python oop concept

1.class
    -it is a group of different type of data and functions
    
2.object
    -it is a instance of class
    
3.nheritance
    -the object of one class can aquire the properties of object another class
    is called 3nheritance.
    -creating a new class from an existing class is called inheritance
    1.single
    2.multiple
    3.multilevel
    4.hierarchical
    5.hybrid

4.polymorphisam
    1.compile time polymorphism (method overloading): when there is a more than
    one method in a single class having the same name but with different number
    of arguments then it is called method overloading.
    
    2.run time polymorphisam(method overriding): when there is a same method
    protoype in your both base classs & derived class & if you call that method
    using the object of derived class ,then only derived class method will be
    called.so you can say that method of derived class override the method of
    base class.

5.abstraction- data hiding

6.encapsulation- to bind a data and code in to a single unit is called.

'''


class student:
    def getdata(self,fname,lname):
        self.f=fname
        self.l=lname
    def putdata(self):
        print("first name : ",self.f)
        print("last name : ",self.l)

s1=student()
s1.getdata("pritesh","senjaliya")
s1.putdata()
        















    
