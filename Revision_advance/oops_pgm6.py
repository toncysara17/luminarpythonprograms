#using oops
class Bank:
    def acCreate(self,acno,acname,bname):
        self.acno=acno
        self.acname=acname
        self.bname=bname
        self.minibal=5000
        self.currentbal=self.minibal
    def deposit(self,amt):
        self.minibal+=amt
        print("your account has been credited with amount",amt)
        print("your current balance",self.currentbal)
    def withdraw(self,amt):
        if amt>self.currentbal:
            print("insufficient balance")
        else:
            print("account debited with",amt)
            self.currentbal-=amt
            print("available balance",self.currentbal)
obj=Bank()
obj.acCreate(123,"tom","sbi")
obj.deposit(2500)
obj.withdraw(1500)

