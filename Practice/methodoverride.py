#one name multiple form


class a:
    def show(self):
        print("show data a")
class b(a):
    def show(self):
        super().show()   
        print("show data b")
        
class c(a):
    def show(self):
        super().show()
        print("show data c")
class d(c,b):
    def show(self):
       super().show()
       print("show data d")
       
c1=d()
c1.show()
