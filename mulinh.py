class Base1:
    x=10
    def b1(self):
        print("Inside b1, class Base1")
class Base2:
    y=20
    def b2(self):
        print("Inside b2, class Base2")
class Derived(Base1,Base2):
    pass

d = Derived()
d.b1()
d.b2()
print(d.x)
print(d.y)
