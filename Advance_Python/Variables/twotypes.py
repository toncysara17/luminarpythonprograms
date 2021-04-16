#variables
#2 types
    #instance variables........related to object can access creating self
    #static variables..........related to class can access creating class name


class Bank:
    bname="sbi"
    def accCreate(self,acno,name):
        self.acno=acno
        self.name=name
        self.minbal=5000
        self.balance=self.minbal

    def Deposit(self,amt):
        self.balance+=amt
        print("your ",Bank.bname ," account has been credited with amt",amt)
        print("your current balance is",self.balance)

    def Withdraw(self,amt):
        if amt>self.balance:
            print("insufficient balance")
        else:
            print("account has been debited with amt",amt)
            self.balance-=amt
            print("available balance",self.balance)
obj=Bank()
obj.accCreate(123,"abc")
obj.Deposit(2500)
obj.Withdraw(1500)


