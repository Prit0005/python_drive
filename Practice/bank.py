
class bank:
    def openaccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("hello ",cname,", your account number ",str(acno),"is opned account with ",balance,"rs")
    def deposite(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
    def checkbalance(self):
        print("your current balance is : ",self.balance)

b1=bank()
b1.openaccount("pritesh",101,1000000)

while True:
    print("*"*60)
    print("1.deposite")
    print("2.withdraw")
    print("3.checkbalance")
    print("4.exit")
    print("*"*60)

    choice=int(input("enter your choice : "))
    if choice==1:
        amount=int(input("enter deposite amount : "))
        b1.deposite(amount)
        print("*"*60)
    elif choice==2:
       amount=int(input("enter withdraw amount : "))
       b1.withdraw(amount)
       print("*"*60)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        print("exit")
        break
    elif choice==5:
        print("thank you")
    else:
        print("invalid number")

    







    
