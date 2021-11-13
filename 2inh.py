class A:
    def f(self):
        print("Inside A fn()")

class B(A):
    def f(self):
        print("Inside B fn()")


b = B()
b.f()
