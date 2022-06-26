class A:
    pass
class B(A):
    pass
b = B()
print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(bool,int))
