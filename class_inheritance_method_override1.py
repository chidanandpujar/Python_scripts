class A:
    def f(self):
        print("Inside A f()")
class B(A):
    def f(self):
        print("Inside B f()")

b = B()
b.f()
