class Parent:
    def add(self, a, b):
        c = a + b
        print("C =", c)

class Child( Parent ):
    def mult(self, a, b):
        c = a * b
        print("C =", c)

c = Child()
c.add(2,3)
c.mult(2,3)
