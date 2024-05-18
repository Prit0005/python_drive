
#multiple inheritance
class a:
    def geta(self,a):
        self.a=a
    def puta(self):
        print("A : ",self.a)
class b:
    def getb(self,b):
        self.b=b
    def putb(self):
        print("B : ",self.b)

class c(a,b):
    def getc(self,c):
        self.c=c
    def putc(self):
        print("C : ",self.c)

b1=c()
b1.geta(10)
b1.getb(20)
b1.getc(30)
b1.puta()
b1.putb()
b1.putc()
