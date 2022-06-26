class A:
    def __init__(self):
        print("Base class init")
    def regmethod(self, val):
        print("Inside Base regmethod", val)

class B(A):
    def __init__(self):
        print("Derived class init")
        super().__init__()
    def regmethod(self, x):
        print("Inside Derived regmethod", x)
        super().regmethod(x+1)

b = B()
b.regmethod(10)
