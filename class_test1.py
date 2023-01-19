import os
class Myclass:
    """This is doc string"""
    def __init__(self):
        self.a=10
        self.b=11
        self.c=12

MyClassObj1 = Myclass()
print(dir(MyClassObj1))
print(MyClassObj1.__dict__)
print(MyClassObj1.__doc__)
print(MyClassObj1.__module__)
print(os.__file__)
