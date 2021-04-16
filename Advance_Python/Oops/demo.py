class M:
    def __init__(self,no):
        self.no=no
    def print(self):
        print(self.no)
class P(M):
    def __init__(self,no2,no):
        super().__init__(no)
        self.no2=no2
    def pr(self):
        print(self.no2)
        print(self.no)
p=P(1,2)
p.print()
