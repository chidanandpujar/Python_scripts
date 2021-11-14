class A:
    def f(self):
        print("f() in A")
class B:
    def f(self):
        print("f() in B")
class D(A,B):
    pass

class E(B,A):
    pass


print(D.mro())
print(E.mro())

d = D()
d.f()

e = E()
e.f()

