#bank pgm
class Bank:
    def accCreate(self,acname,acno,bname):
        self.acname=acname
        self.acno=acno
        self.bname=bname
        self.minibalance=5000
        self.balance=self.minibalance

    def deposit(self,amt):
        self.balance+=amt
        print("your account has been credited with amt",amt)
        print("your current balance is",self.balance)

    def withdraw(self,amt):   #7000
        if(amt>self.balance):
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.balance-=amt
            print("available balance",self.balance)

obj=Bank()
obj.accCreate("tom",123,"sbi")
obj.deposit(2500)
obj.withdraw(1500)


#instance variable
#static variable

