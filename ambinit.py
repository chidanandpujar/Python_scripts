class X:
    def __init__(self,x):
        print("Inside X ", x)
class Y:
    def __init__(self):
        print("Inside Y")
class Z(X,Y):
    def __init__(self):
        super().__init__(10)
        print("Inside Z")

obj = Z()
