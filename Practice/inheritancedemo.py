
#single level
#multiple level
#hybrid level
class a:
    def geta(self,a):
        self.a=a
    def puta(self):
        print("A : ",self.a)
class b(a):
    def getb(self,b):
        self.b=b
    def putb(self):
        print("B : ",self.b)

class c(a):
    def getc(self,c):
        self.c=c
    def putc(self):
        print("C : ",self.c)
class d(b,c):
    def getd(self,d):
        self.d=d
    def putd(self):
        print("D : ",self.d)
    
b1=d()
b1.geta(10)
b1.getb(20)
b1.getc(30)
b1.getd(40)
b1.puta()
b1.putb()
b1.putc()
b1.putd()
