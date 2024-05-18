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
class d(a):
    def getd(self,d):
        self.d=d
    def putd(self):
        print("D : ",self.d)
b1=b()
b1.geta(10)
c1=c()
c1.geta(20)
d1.d()
d1.geta(30)
b1.puta()
c1.puta()
d1.puta()
