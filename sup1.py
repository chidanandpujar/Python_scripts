class A:
    def __init__(self):
        print("Base class init")
    def regmethod(self,val):
        print("Inside Base reg method",val)

class B(A):
    def __init__(self):
        print("Derived init")
        super().__init__()
    def regmethod(self,x):
        print("Derived regmethod")
        super().regmethod(x+1)

b= B()
b.regmethod(10)
