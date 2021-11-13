class Parent:
    def add(self,a,b):
        c = a + b
        print("c=",c)

class child(Parent):
    def mult(self,a,b):
        c = a * b
        print("c=",c)

c = child()
c.mult(2,3)
c.add(2,3)
