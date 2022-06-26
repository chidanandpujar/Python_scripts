class A:
    pass
class B(A):
    pass
b = B()
print(isinstance(b,B))
print(isinstance(b,A))
a = 5
print(isinstance(a, int))
print(isinstance(a, float))
